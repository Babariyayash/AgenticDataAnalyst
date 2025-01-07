from langchain_core.messages import HumanMessage
from typing import List
from dataclasses import dataclass
from langgraph.graph import StateGraph
from agent.graph.state import AgentState
from agent.graph.nodes import call_model, call_tools, route_to_tools
from agent.data_models import InputData


class PythonChatbot:
    def __init__(self):
        super().__init__()
        self.reset_chat()
        self.graph = self.create_graph()

    def create_graph(self):
        workflow = StateGraph(AgentState)
        workflow.add_node('agent', call_model)
        workflow.add_node('tools', call_tools)

        workflow.add_conditional_edges('agent', route_to_tools)

        workflow.add_edge('tools', 'agent')
        workflow.set_entry_point('agent')
        return workflow.compile()

    def user_sent_message(self, user_query, input_data: List[InputData]):
        print("User Query:", user_query)  # Log the user query
        print("Input Data:", input_data)  # Log the input data

        starting_image_paths_set = set(sum(self.output_image_paths.values(), []))
        input_state = {
            "messages": self.chat_history + [HumanMessage(content=user_query)],
            "output_image_paths": list(starting_image_paths_set),
            "input_data": input_data,
        }

        # Invoke the graph and get the result
        result = self.graph.invoke(input_state, {"recursion_limit": 25})

        # Debugging: Print the graph result
        print("Graph Result:", result)

        self.chat_history = result["messages"]
        new_image_paths = set(result["output_image_paths"]) - starting_image_paths_set
        self.output_image_paths[len(self.chat_history) - 1] = list(new_image_paths)

        if "intermediate_outputs" in result:
            self.intermediate_outputs.extend(result["intermediate_outputs"])

        # Extract the last AI message content
        last_message = self.chat_history[-1]
        return getattr(last_message, "content", "No response generated.")

    def reset_chat(self):
        self.chat_history = []
        self.intermediate_outputs = []
        self.output_image_paths = {}
