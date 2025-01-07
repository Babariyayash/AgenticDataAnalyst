from langchain_core.tools import tool
from langchain_core.messages import AIMessage
from typing import Annotated, Tuple
from langgraph.prebuilt import InjectedState
import sys
from io import StringIO
import os
import pandas as pd

persistent_vars = {}
plotly_saving_code = """import pickle
import uuid
import plotly

for figure in plotly_figures:
    pickle_filename = f"images/plotly_figures/pickle/{uuid.uuid4()}.pickle"
    with open(pickle_filename, 'wb') as f:
        pickle.dump(figure, f)
"""


@tool(parse_docstring=True)
def complete_python_task(
        graph_state: Annotated[dict, InjectedState], thought: str, python_code: str
) -> Tuple[str, dict]:
    """
    Executes Python code dynamically within a controlled environment.

    Args:
        graph_state (dict): The current graph state, including input data and variables.
        thought (str): User's reasoning or intent behind the task.
        python_code (str): Python code to execute.

    Returns:
        Tuple[str, dict]: Output from the execution and the updated state.
    """
    current_variables = graph_state.get("current_variables", {})

    # Load datasets into current_variables
    for input_dataset in graph_state["input_data"]:
        if input_dataset.variable_name not in current_variables:
            current_variables[input_dataset.variable_name] = pd.read_csv(input_dataset.data_path)

    # Ensure directory for saving figures
    if not os.path.exists("images/plotly_figures/pickle"):
        os.makedirs("images/plotly_figures/pickle")

    # Prepare for code execution
    current_image_pickle_files = os.listdir("images/plotly_figures/pickle")
    try:
        # Capture stdout
        old_stdout = sys.stdout
        sys.stdout = StringIO()

        # Execute the code dynamically
        exec_globals = globals().copy()
        exec_globals.update(persistent_vars)
        exec_globals.update(current_variables)
        exec_globals.update({"plotly_figures": []})

        exec(python_code, exec_globals)

        # Capture stdout
        output = sys.stdout.getvalue()

        # Restore stdout
        sys.stdout = old_stdout

        # Save persistent variables
        persistent_vars.update({k: v for k, v in exec_globals.items() if k not in globals()})

        # Check for generated plots
        updated_state = {
            "intermediate_outputs": [{"thought": thought, "code": python_code, "output": output}],
            "current_variables": persistent_vars
        }

        if 'plotly_figures' in exec_globals:
            exec(plotly_saving_code, exec_globals)
            new_image_files = [
                file for file in os.listdir("images/plotly_figures/pickle")
                if file not in current_image_pickle_files
            ]
            if new_image_files:
                updated_state["output_image_paths"] = new_image_files

            persistent_vars["plotly_figures"] = []

        return output, updated_state

    except Exception as e:
        return str(e), {"intermediate_outputs": [{"thought": thought, "code": python_code, "output": str(e)}]}
