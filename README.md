# LLM workshop

### Open AI API keys

https://platform.openai.com/api-keys

### Setting up Miniconda and Python

Create an new environment:

`conda create -n llm python=3.10`

List all the existing environments:

`conda env list`

Activate the environment:

`conda activate llm`

Install the dependencies – part 1:

`pip install langchain==0.1.0 openai==1.7.2 langchain-openai==0.0.2 langchain-community==0.0.12 langchainhub==0.1.14 python-dotenv`

Install the dependencies – part 2:

`pip install langchain_chroma colorama`

### Something went wrong?

Delete the environment and start again:

`conda deactivate`

`conda remove --name llm --all`
