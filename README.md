# Agentic Data Analysis Project

## Overview
This project, **Agentic Data Analysis**, leverages cutting-edge technologies like LangGraph, Streamlit, and LangChain to provide an interactive platform for data exploration and visualization. The project empowers users to upload datasets, query them dynamically, and generate insightful visualizations in real time.

## Features
1. **Dynamic Dataset Querying**:
   - Upload datasets and interactively query them.
   - Perform custom operations to extract insights.

2. **Visualization**:
   - Generate dynamic visualizations with Plotly.
   - Support for bar charts, line charts, scatter plots, and more.

3. **Agent Integration**:
   - Use LangGraph agents to facilitate workflow orchestration.
   - Automate data processing and visualization tasks.

4. **Interactive UI**:
   - Built with Streamlit for a responsive and user-friendly interface.

## Technologies Used
- **LangGraph**: Workflow orchestration for advanced agent interactions.
- **Streamlit**: Simplified development of interactive web applications.
- **LangChain**: Integration of language models to enhance agent workflows.
- **Pandas**: Data manipulation and analysis.
- **Plotly**: Interactive and dynamic visualizations.

## Installation and Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/agentic-data-analysis.git
   ```
2. Navigate to the project directory:
   ```bash
   cd agentic-data-analysis
   ```
3. Create a virtual environment and activate it:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # For Windows: .venv\Scripts\activate
   ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run
1. Start the Streamlit application:
   ```bash
   streamlit run python_visualisation_agent.py
   ```
2. Access the application in your browser at `http://localhost:8501`.

## Demo Video
[Click here to watch the demo video](#)

## Directory Structure
```
agentic-data-analysis/
├── graph/
│   ├── state.py          # Manages shared state for workflows
│   ├── nodes.py          # Defines LangGraph nodes for model/tool execution
│   ├── tools.py          # Implements tools for task execution and visualization
├── prompts/
│   ├── main_prompt.md    # Defines LangGraph agent roles and behavior
├── backend.py            # Main workflow management for LangGraph agents
├── data_models.py        # Defines data models
├── python_visualisation_agent.py  # Streamlit entry point
├── requirements.txt      # Dependencies
├── README.md             # Project documentation
```

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a Pull Request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact
For questions or feedback, please contact:
- **Name**: Your Name
- **Email**: your.email@example.com
- **GitHub**: [your-username](https://github.com/your-username)

