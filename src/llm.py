from langchain.schema.messages import HumanMessage, SystemMessage
from chatbot import chat_model
from colorama import Fore, init

init()

prompt = input(Fore.BLUE + "\n>>> ")

messages = [
    SystemMessage(
      content="""You're an assistant knowledgeable about
      healthcare. Only answer healthcare-related questions."""
    ),
    HumanMessage(content=prompt),
]

answer = chat_model.invoke(messages)

print(f"{Fore.GREEN}\n{answer.content}\n")

"""

Try the following prompts:

What is the NHS?

What is blood pressure?

Who is the prime minister of the UK?

"""