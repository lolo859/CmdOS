import os
from termcolor import colored
def execute(displaysplit,rep):
    prompt=rep.split()
    if displaysplit==1:
        print(prompt)
    if len(prompt)==1:
        print(colored("La commande est mal formulée","red",attrs=["bold"]))
    else:
        os.system(rep[7::])