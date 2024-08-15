
from chatbot import execution_details, hospital_agent_executor
from colorama import Fore, init

init()

prompt = input(Fore.BLUE + "\n>>> ")

answer = hospital_agent_executor.invoke({"input": prompt})

output = answer["output"]

print(f"{Fore.GREEN}\n{output}")

details = execution_details(answer)

print(f"{Fore.YELLOW}\n{details}\n")

"""

What is the current wait time at Wallace-Hamilton hospital?

What is the current wait time at Addenbrooke's hospital?

What do patients think about Wallace-Hamilton hospital?

"""