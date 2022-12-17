import simpleaudio as sa
import os
from termcolor import colored
def execute(displaysplit,rep,adresse):
    music=rep.split()
    if displaysplit==1:
        print(music)
    if len(music)==2 and music[1]=="store":
        print("Voici votre musique :")
        fichiers = os.listdir(adresse+"/music")
        longueur=len(fichiers)
        for element in range(longueur):
            print(" ",fichiers[element])
    elif len(music)==3:
        if music[1]=="play":
            fichiers = os.listdir(adresse+"/music")
            musicplay=rep[11::]
            if musicplay in fichiers:
                musicd=adresse+"/music/"+musicplay
                wave_object = sa.WaveObject.from_wave_file(musicd)
                print(colored(("Le son suivant va être lu : "+musicplay),"blue",attrs=["bold"]))
                play_object = wave_object.play()
            else:
                print(colored("Ce fichier n'existe pas","yellow",attrs=["bold"]))
        else:
            print(colored("La commande est mal formulée","red",attrs=["bold"]))
    else:
        print(colored("La commande est mal formulée","red",attrs=["bold"]))