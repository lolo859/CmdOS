from PIL import Image
import os
from termcolor import colored
def execute(displaysplit,rep,adresse):
    image=rep.split()
    if displaysplit==1:
        print(image)
    if len(image)==2 and image[1]=="store":
        print("Voici votre phototèque :")
        fichiers = os.listdir(adresse+"/image")
        longueur=len(fichiers)
        for element in range(longueur):
            print(" ",fichiers[element])
    elif len(image)==3:
        if image[1]=="display":
            fichiers = os.listdir(adresse+"/image")
            imgaffich=rep[14::]
            if imgaffich in fichiers:
                imgd=adresse+"/image/"+imgaffich
                im = Image.open(imgd)
                im.show()
            else:
                print(colored("Ce fichier n'existe pas","yellow",attrs=["bold"]))
        else:
            print(colored("La commande est mal formulé","red",attrs=["bold"]))
    else:
        print(colored("La commande est mal formulée","red",attrs=["bold"]))