# LLM workshop

### Setting up Miniconda and Python

Create a new environment:

`conda create -n llm python=3.10`

Activate the environment:

`conda activate llm`

Install the dependencies – part 1:

`pip install langchain==0.1.0 openai==1.7.2 langchain-openai==0.0.2 langchain-community==0.0.12 langchainhub==0.1.14 python-dotenv`

Install the dependencies – part 2:

`pip install langchain_chroma colorama`

### Open AI API keys

Create a new Open AI API key:

https://platform.openai.com/api-keys

Create an new file `.env` in the main project directory and add the following content:

`OPENAI_API_KEY=` followed by the API key

### Running the application

To run the basic LLM, execute the following:

`python src/llm.py`

To run the LLM with RAG, execute the following:

`python src/llm_with_rag.py`

To run the LLM with Agent Executor, execute the following:

`python src/llm_with_agent.py`

### Something went wrong?

Delete the environment and start again:

`conda deactivate`

`conda remove --name llm --all`
