from termcolor import colored
def execute(displaysplit,rep):
    error=0
    if len(rep)>=9:
        colorp={"b":"blue","g":"green","r":"red","w":"white","y":"yellow","m":"magenta","c":"cyan"}
        if rep[6] in colorp:
            colorprint=colorp.get(rep[6])
        else:
            print(colored("Cette couleur n'est pas prise en charge","yellow",attrs=["bold"]))
            error=1
        print1=rep[8::]
        if error==0:
            print(colored(print1,colorprint))
    else:
        print(colored("La commande est mal formulée","red",attrs=["bold"]))