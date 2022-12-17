import time
from termcolor import colored
def execute(displaysplit,rep):
    error=0
    temps=rep.split()
    if displaysplit==1:
        print(temps)
    try:
        temps[1]=float(temps[1])
    except:
        print(colored("Le module time n'accepte que des nombres","red",attrs=["bold"]))
        error=1
    if len(temps)==2 and type(temps[1])==float:
        temps_1=temps[1]
        time.sleep(temps_1)
    else:
        if error==0:
            print(colored("La commande est mal formulée","red",attrs=["bold"]))
    error=0