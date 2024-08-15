from chatbot import review_chain
from colorama import Fore, init

init()

prompt = input(Fore.BLUE + "\n>>> ")

answer = review_chain.invoke(prompt)

print(f"{Fore.GREEN}\n{answer}\n")

"""

Try the following prompts:

Has anyone complained about communication with the hospital staff?

What does Catherine Yang think about the hospital staff?

What do patients think about Wallace-Hamilton hospital?

What do patients think about Michael Smith?

How many patients reviewed Michael Smith?

How many patients provided feedback about Michael Smith?

"""
