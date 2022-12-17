import random
from termcolor import colored
def execute(displaysplit,rep):
    error=0
    aleatoire=rep.split()
    if displaysplit==1:
        print(aleatoire)
    if len(aleatoire)==3:
        try:
            aleatoire[1]=int(aleatoire[1])
            aleatoire[2]=int(aleatoire[2])
            random_1=aleatoire[1]
            random_2=aleatoire[2]
        except:
            print(colored("La commande n'accepte que des nombres","yellow",attrs=["bold"]))
            error=1
        if error==0:
            print("Le nombre est",random.randint(random_1,random_2))
    else:
        print(colored("La commande est mal formulée","red",attrs=["bold"]))
    error=0