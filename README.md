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

Install the dependencies:

`pip install -r requirements.txt`

### Something went wrong?

Delete the environment and start again:

`conda deactivate`

`conda remove --name llm --all`