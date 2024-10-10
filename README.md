# Simple LangChain Text Generator with Streamlit
This project demonstrates a basic implementation of a text generator using LangChain's OpenAI integration (`gpt-3.5-turbo`) and a simple user interface powered by Streamlit. Users can input prompts, and the application will generate responses based on the OpenAI GPT model.

## Requirements
To run this project, you’ll need the following libraries:

- `langchain` - for interacting with OpenAI’s GPT models using LangChain.
- `openai` - the Python package for interacting with OpenAI’s API.
- `streamlit` - a web app framework to display the interface.


## Installation
Steps to install and run your project.
1. Clone Repository 

```bash
git clone <repository-url>
cd <project-directory>
```
2. Set up a Python environment
3. Install the required packages

```bash 
pip install langchain openai streamlit
```
4. Set up your OpenAI API key
You can set your OpenAI API key in the environment variable `OPENAI_API_KEY`.

```bash 
export OPENAI_API_KEY='openai-api-key'
# On Windows: set OPENAI_API_KEY=your-openai-api-key
```
## How to Run
1. Run the streamlit app
```bash
streamlit run app.py
```

2. Interact with the app:

- Open your browser and navigate to the displayed URL (usually `http://localhost:8501`).
- Enter a prompt in the text area and click "Generate Text" to get a response generated by the GPT model.











