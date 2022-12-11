#####################################################################
#Import et clear
####################################################################
from genericpath import exists
from os import listdir
from os.path import isfile, join
import os.path
import os
from random import random
#from xml.sax.xmlreader import AttributesImpl
from termcolor import colored
import getpass
import requests as req
import cmd_fonction as cmdf
from datetime import datetime
from ftplib import FTP
import uuid
import subprocess
import sys
import webbrowser
import secure_id
os.system("clear")
#########################################################################
#Admin, commande et chargement
#########################################################################
if (len(sys.argv)==2 and sys.argv[1]=="admin") or (len(sys.argv)==1 and sys.argv[0]=="admin"):
    admin=1
else:
    admin=0
cmdf.charg()
mdpt="6"
com={"help":"Voici la liste des commandes de Cmd OS :""\nhelp - Afficher la liste des commandes"
     "\ninfo - Afficher les infos sur un programme / utliser sys pour voir la version du système / utiliser 'info app (fichier python)' pour afficher les caractéristiques d'un fichier python du dossier app"
     "\nstore - Affiche les différentes applications installables : \n   install - installer un module \n   uninstall - desinstaller un module""\n   list - affiche les différents modules installés"
     "\ncd - changer de dossier""\ndir - permet de voir les fichiers/dossiers"
     "\nopendir - ouvrir un dossier"
     "\nmdp - Voir si le mot de passe est actif ou non :\n   act - active le mot de passe\n   disact - desactive le mot de passe"
     "\nren - renomer un fichier"
     "\nupdate :""\n   upgrade - mettre à jour le système en téléchargant la dernière version""\n   check - vérifier si une nouvelle mise à jour est disponible"
     "\nadmin - active ou désactive le mode admin"
     "\nlog - affiche les logs (il faut être connecté en tant qu'administrateur pour utiliser cette commande)""\n   show - affiche les logs""\n   delete - supprime les logs"
     "\ndetail - affiche les propriétés d'un fichier ou dossier sous forme de os.stat_result"
     "\nshell (version raccourci : sh) - ouvre le cmd"
     "\nexecute - permet d'éxécuter des fonctions exterieures au système"}
############################################
#App
############################################
app={"random":"0",
     "time":"0",
     "music":"0",
     "uuid":"0",
     "image":"0",
     "browser":"0",
     "print":"0",
     "maths":"0",
     "download":"0",
     "prompt":"0"}
############################################
#Import app depuis txt
############################################
def appinitext():
    if not os.path.exists("save_txt/random.txt"):
        randomtext=open("save_txt/random.txt","w")
        randomtext.write(app["random"])
        randomtext.close()
    else:
        import module.random
        randomtext=open("save_txt/random.txt",'r')
        data=randomtext.readlines()
        app.update({"random":str(data[0])})
        randomtext.close()
    if not os.path.exists("save_txt/time.txt"):
        timetext=open("save_txt/time.txt","w")
        timetext.write(app["time"])
        timetext.close()
    else:
        import module.time
        timetext=open("save_txt/time.txt",'r')
        data=timetext.readlines()
        app.update({"time":str(data[0])})
        timetext.close()
    if not os.path.exists("save_txt/music.txt"):
        musictext=open("save_txt/music.txt","w")
        musictext.write(app["music"])
        musictext.close()
    else:
        import module.music
        musictext=open("save_txt/music.txt",'r')
        data=musictext.readlines()
        app.update({"music":str(data[0])})
        musictext.close()
    if not os.path.exists("save_txt/uuid.txt"):
        uuidtext=open("save_txt/uuid.txt","w")
        uuidtext.write(app["uuid"])
        uuidtext.close()
    else:
        import module.uuid
        uuidtext=open("save_txt/uuid.txt",'r')
        data=uuidtext.readlines()
        app.update({"uuid":str(data[0])})
        uuidtext.close()
    if not os.path.exists("save_txt/image.txt"):
        imagetext=open("save_txt/image.txt","w")
        imagetext.write(app["image"])
        imagetext.close()
    else:
        import module.image
        imagetext=open("save_txt/image.txt",'r')
        data=imagetext.readlines()
        app.update({"image":str(data[0])})
        imagetext.close()
    if not os.path.exists("save_txt/browser.txt"):
        browsertext=open("save_txt/browser.txt","w")
        browsertext.write(app["browser"])
        browsertext.close()
    else:
        import module.browser
        browsertext=open("save_txt/browser.txt",'r')
        data=browsertext.readlines()
        app.update({"browser":str(data[0])})
        browsertext.close()
    if not os.path.exists("save_txt/print.txt"):
        printtext=open("save_txt/print.txt","w")
        printtext.write(app["print"])
        printtext.close()
    else:
        import module.print
        printtext=open("save_txt/print.txt",'r')
        data=printtext.readlines()
        app.update({"print":str(data[0])})
        printtext.close()
    if not os.path.exists("save_txt/maths.txt"):
        mathstext=open("save_txt/maths.txt","w")
        mathstext.write(app["maths"])
        mathstext.close()
    else:
        import module.maths
        mathstext=open("save_txt/maths.txt",'r')
        data=mathstext.readlines()
        app.update({"maths":str(data[0])})
        mathstext.close()
    if not os.path.exists("save_txt/download.txt"):
        downloadtext=open("save_txt/download.txt","w")
        downloadtext.write(app["download"])
        downloadtext.close()
    else:
        import module.download
        downloadtext=open("save_txt/download.txt",'r')
        data=downloadtext.readlines()
        app.update({"download":str(data[0])})
        downloadtext.close()
    if not os.path.exists("save_txt/prompt.txt"):
        prompttext=open("save_txt/prompt.txt","w")
        prompttext.write(app["prompt"])
        prompttext.close()
    else:
        import module.prompt
        prompttext=open("save_txt/prompt.txt",'r')
        data=prompttext.readlines()
        app.update({"prompt":str(data[0])})
        prompttext.close()
appinitext()
############################################
#Info
############################################
info={"sys":"Cmd OS v2.0 - Basé en Python",
      "system":"Cmd OS v2.0 - Basé en Python",
      "time":"Module Time""\nVersion : 1.0""\nAuteur : système""\nPermission : displaysplit, rep",
      "random":"Module Random""\nVersion : 1.2""\nAuteur : système""\nPermission : displaysplit, rep",
      "music":"Module Music""\nVersion : 1.1""\nAuteur : système""\nPermission : displaysplit, rep, adresse""\nNote : basé avec le module simpleaudio",
      "uuid":"Module Uuid""\nVersion : 1.0""\nAuteur : système""\nPermission : displaysplit, rep""\nNote : basé avec le module uuid4",
      "image":"Module Image""\nVersion : 1.0""\nAuteur : système""\nPermission : displaysplit, rep, adresse""\nNote : basé avec le module PIL",
      "browser":"Module Browser""\nVersion : 1.0""\nAuteur : système""\nPermission : displaysplit, rep""\nNote : basé avec le module browser",
      "print":"Module Print""\nVersion : 1.0""\nAuteur : système""\nPermission : displaysplit, rep""\nNote : basé avec le module termcolor",
      "maths":"Module Maths""\nVersion : 1.1""\nPermission : displaysplit, rep""\nAuteur : système",
      "download":"Module Download""\nVersion : 1.0""\nAuteur : système""\nPermission : displaysplit, rep""\nNote : basé sur le module request",
      "prompt":"Module Prompt""\nVersion : 1.0""\nPermission : displaysplit, rep""\nAuteur : système"}
############################################
#Adresse
############################################
adresse=os.path.realpath(__file__)
adresse=os.path.dirname(adresse)
############################################
#Vérification
############################################
if not os.path.exists(adresse)==True:
    while not os.path.exists(adresse)==True:
        adresse=input("Le système n'a pas démmarrer correctement, veulliez rentrer le chemin absolu du dossier ou se trouve le fichier CmdOS.py : ")
if not(os.path.exists(adresse+"/image") and os.path.exists(adresse+"/music") and os.path.exists(adresse+"/README.md") and os.path.exists(adresse+"/gif") and os.path.exists(adresse+"/__pycache__") and os.path.exists(adresse+"/module") and os.path.exists(adresse+"/app") and os.path.exists(adresse+"/save_txt")):
    print(colored("Le système ne peut pas fonctionner dans son intégrité car certain dosssier/fichier ne sont pas présents.\nVeulliez vous assurez que les dossier suivant existe: image, music, __pycache__, gif et README.md.","red",attrs=["bold"]))
    quit()
############################################
#Mot de passe
############################################
if not os.path.exists(adresse+"/save_txt/mdp.txt"):
    mdptext=open("save_txt/mdp.txt","w")
    mdptext.write(mdpt)
    mdptext.close()
else:
    mdptext=open("save_txt/mdp.txt",'r')
    data=mdptext.readlines()
    mdpt=data[0]
    mdptext.close()
repmdp=""
############################################
#Connexion
############################################
print(colored("""Cmd OS v2.0""","green",attrs=["bold"])) 
host="ftp-cmdos.alwaysdata.net"
user="cmdos"
password="CmdOS2008)"
connect=FTP(host,user,password)
connect.sendcmd('CWD www')
connect.sendcmd("CWD command")
##########################
#Fonction Cmd
##########################
def cmd():
#################################
#Variable, module
#################################
    global adresse,mdpt,app,mdptext,repmdp,admin
    log=["Voici les logs :"]
    charginstall=1
    displaysplit=0
    logserver=1
    store="Bienvenue dans le store de Cmd OS, voici les modules disponibles :"+"\nrandom - générer un nombre aléatoire"+"\ntime - attendre un temps"+"\nmusic - permet de jouer un son"+"\nuuid - générer des identifiants aléatoire"+"\nimage - permet d'afficher une image"+"\nbrowser - permet d'afficher une page web"+"\nprint - permet d'afficher du texte en couleur dans la console"+"\ndownload - permet de télécharger une page web"+"\nprompt - permet d'éxécuter des commandes de l'invite de commande"+"\nPour installer un module, faites <<store install>> suivie du nom du module"+"\nPour desinstaller un module, faites <<store uninstall>> suivie du nom du module"+"\nPour voir la liste des modules installés faites <<store list>>"
    while True:
        version="2.0"
        if app["random"]=="1":
            import module.random
        if app["time"]=="1":
            import module.time
        if app["music"]=="1":
            import module.music
        if app["uuid"]=="1":
            import module.uuid
        if app["image"]=="1":
            import module.image
        if app["browser"]=="1":
            import module.browser
        if app["print"]=="1":
            import module.print
        if app["maths"]=="1":
            import module.maths
        if app["download"]=="1":
            import module.download
        if app["prompt"]=="1":
            import module.prompt
#################################
#Gestion entrée utilisateur
#################################
        if admin==0:
            demande=colored(getpass.getuser(),"green",attrs=["bold"])+" "+colored(adresse,"blue",attrs=["bold"])+" >>> "
        else:
            demande=colored(getpass.getuser(),"green",attrs=["bold"])+colored("(admin)","red",attrs=["bold"])+" "+colored(adresse,"blue",attrs=["bold"])+" >>> "
        rep=input(demande)
#################################
#Ajout de commande a log
#################################
        if admin==1:
            heure=str(datetime.now())
            if logserver==1:
                id=str(secure_id.sid2())
                contenttxt=open("content.txt","w")
                contenttxt.write(getpass.getuser()+"(admin) "+heure+" "+version+" "+rep)
                contenttxt.close()
                contenttxt=open("content.txt","rb")
                connect.storbinary("STOR "+id,contenttxt)
                contenttxt.close()
                log.append(id+" "+colored(getpass.getuser(),"green",attrs=["bold"])+colored("(admin) ","red",attrs=["bold"])+colored(heure,"blue",attrs=["bold"])+" "+rep)
            else:
                log.append(colored(getpass.getuser(),"green",attrs=["bold"])+colored("(admin) ","red",attrs=["bold"])+colored(heure,"blue",attrs=["bold"])+" "+rep)
        else:
            heure=str(datetime.now())
            if logserver==1:
                id=str(secure_id.sid2())
                contenttxt=open("content.txt","w")
                contenttxt.write(getpass.getuser()+" "+heure+" "+version+" "+rep)
                contenttxt.close()
                contenttxt=open("content.txt","rb")
                connect.storbinary("STOR "+id,contenttxt)
                contenttxt.close()
                log.append(id+" "+colored(getpass.getuser(),"green",attrs=["bold"])+" "+colored(heure,"blue",attrs=["bold"])+" "+rep)
            else:
                log.append(colored(getpass.getuser(),"green",attrs=["bold"])+" "+colored(heure,"blue",attrs=["bold"])+" "+rep)
        if rep in com:
            print(com[rep])
#################################
#Store
#################################
        elif rep=="store":
            print(store)
#################################
#Detail
#################################
        elif rep.startswith("detail"):
            detail1=rep.split()
            if displaysplit==1:
                print(detail1)
            if len(detail1)>1:
                detail2=rep[7::]
                fichiers = os.listdir(adresse)
                if detail2 in fichiers:
                    detail3=adresse+"/"+detail2
                    print(os.stat(detail3))
                else:
                    print(colored("Le fichier/dossier n'existe pas","yellow",attrs=["bold"]))
            else:
                print(colored("La commande est mal formulée",'red',attrs=["bold"]))
#################################
#Admin
#################################
        elif rep.startswith("admin"):
            admin1=rep.split()
            if displaysplit==1:
                print(admin1)
            if len(admin1)==2:
                if admin1[1]=="on":
                    if admin==0:
                        demande=colored("Taper votre mot de passe : ","blue",attrs=["bold"])
                        repmdp=input(demande)
                        if repmdp==mdpt:
                            admin=1
                        else:
                            print(colored("Le mot de passe est incorrect","red",attrs=["bold"]))
                    else:
                        print(colored("Le mode admin est déja activé","yellow",attrs=["bold"]))
                elif admin1[1]=="off":
                    if admin==1:
                        admin=0
                    else:
                        print(colored("Le mode admin est déja désactivé","yellow",attrs=["bold"]))
                else:
                    print(colored("La commande est mal formulée","red",attrs=["bold"]))
            else:
                print(colored("La commande est mal formulée","red",attrs=["bold"]))
#################################
#Supprimer
#################################
        elif rep.startswith("del"):
            supr=rep.split()
            if displaysplit==1:
                print(supr)
            if len(supr)==2:
                fichiers = os.listdir(adresse)
                if supr[1] in fichiers:
                    del_1=adresse+"/"+supr[1]
                    os.remove(del_1)
                else:
                    print(colored("Le fichier/dossier n'existe pas","yellow",attrs=["bold"]))
            else:
                print(colored("La commande n'est pas bien formulée","red",attrs=["bold"]))
#################################
#Ouvrir un dossier
#################################
        elif rep.startswith("opendir"):
            opendir=rep.split()
            if displaysplit==1:
                print(opendir)
            if len(opendir)==2:
                if type(opendir[1])==str:
                    fichiers = os.listdir(adresse)
                    if opendir[1] in fichiers and not "." in opendir[1]:
                        if not adresse=="/":
                            adresse=adresse+"/"+opendir[1]
                        else:
                            adresse=adresse+opendir[1]
                    else:
                        print(colored("Ce dossier est n'existe pas","yellow",attrs=["bold"]))
                else:
                    print(colored("La commande est mal formulée","red",attrs=["bold"]))
            else:
                print(colored("La commande est mal formulée","red",attrs=["bold"]))
#################################
#Renommer
#################################
        elif rep.startswith("ren"):
            ren=rep[4::]
            if displaysplit==1:
                print(ren)
            fichiers = os.listdir(adresse)
            if ren in fichiers:
                ren2=adresse+"/"+ren
                ren3=input("Nouveau nom : ")
                os.rename(ren2, ren3)
            else:
                print(colored("Le fichier/dossier n'existe pas","yellow",attrs=["bold"]))
#################################
#Cd : change directory
#################################
        elif rep.startswith("cd"):
            cd=rep.split()
            if displaysplit==1:
                print(cd)
            if len(cd)>=2:
                if type(cd[1])==str and os.path.exists(cd[1]):
                    if len(cd)==3:
                        adresse=cd[1]+cd[2]
                    elif len(cd)==4:
                        adresse=cd[1]+cd[2]+cd[3]
                    else:
                        adresse=cd[1]
                else:
                    print(colored("Le dossier n'est pas valide","yellow",attrs=["bold"]))
            else:
                print(colored("La commande est mal formulée","red",attrs=["bold"]))
#################################
#Dir : directory
#################################
        elif rep=="dir":
            fichiers = os.listdir(adresse)
            longueur=len(fichiers)
            print("Voici les fichiers/dossiers dans ce dossier :")
            for element in range(longueur):
                print(" ",fichiers[element])
#################################
#Logs
#################################
        elif rep.startswith("log"):
            if admin==1:
                log1=rep.split()
                if displaysplit==1:
                    print(log1)
                if len(log1)==2 and type(log1[1])==str:
                    if log1[1]=="show":
                        for lettre in log:
                            print(lettre)
                    elif log1[1]=="delete":
                        log=["Voici les logs :"]
                        print(colored("Les logs ont bien été supprimé","blue",attrs=["bold"]))
                    else:
                        print(colored("La commande est mal formulée","red",attrs=["bold"]))
                else:
                    print(colored("La commande est mal formulée","red",attrs=["bold"]))
            else:
                print(colored("Vous devez être connecté en tant qu'administrateur pour utiliser cette commande","red",attrs=["bold"]))
#################################
#Store install
#################################
        elif rep.startswith("store install "):
            install=rep[14::]
            if install in app: 
                app.update({install:"1"})
                if charginstall==1:
                    cmdf.charg(0.3,colored("Installation du module...","blue",attrs=["bold"]))
                install2=colored("Le module ","blue",attrs=["bold"])+colored(install,"blue",attrs=["bold","underline"])+colored(" a bien été installé","blue",attrs=["bold"])
                print(install2)
                if install=="random":
                    import module.random
                    appt=open("save_txt/random.txt","w")
                    appt.write(app.get("random"))
                    appt.close()
                if install=="time":
                    import module.time
                    appt=open("save_txt/time.txt","w")
                    appt.write(app.get("time"))
                    appt.close()
                if install=="music":
                    import module.music
                    appt=open("save_txt/music.txt","w")
                    appt.write(app.get("music"))
                    appt.close()
                if install=="uuid":
                    import module.uuid
                    appt=open("save_txt/uuid.txt","w")
                    appt.write(app.get("uuid"))
                    appt.close()
                if install=="image":
                    import module.image
                    appt=open("save_txt/image.txt","w")
                    appt.write(app.get("image"))
                    appt.close()
                if install=="browser":
                    import module.browser
                    appt=open("save_txt/browser.txt","w")
                    appt.write(app.get("browser"))
                    appt.close()
                if install=="print":
                    import module.print
                    appt=open("save_txt/print.txt","w")
                    appt.write(app.get("print"))
                    appt.close()
                if install=="maths":
                    import module.maths
                    appt=open("save_txt/maths.txt","w")
                    appt.write(app.get("maths"))
                    appt.close()
                if install=="download":
                    import module.download
                    appt=open("save_txt/download.txt","w")
                    appt.write(app.get("download"))
                    appt.close()
                if install=="prompt":
                    import module.prompt
                    appt=open("save_txt/prompt.txt","w")
                    appt.write(app.get("prompt"))
                    appt.close()
            else:
                print(colored("Le module que vous essayez d'installer n'existe pas","red",attrs=["bold"]))
#################################
#Execute
#################################
        elif rep.startswith("execute"):
            impor=rep.split()
            if displaysplit==1:
                print(impor)
            if len(impor)==3:
                command="from app."+impor[1]+" import *\ntry:\n    "+impor[2]+"()\nexcept ModuleNotFoundError or NameError:\n    pass"
                subprocess.run([sys.executable, "-c",command])
            else:
                print(colored("La commande est mal formulée","red",attrs=["bold"]))
#################################
#Shell
#################################
        elif rep=="shutdown" or rep=="sh" or rep=="shell":
            break
#################################
#Info
#################################
        elif rep.startswith("info"):
            info_command=rep.split()
            if displaysplit==1:
                print(info_command)
            if len(info_command)==2 or len(info_command)==3:
                if info_command[1] in info:
                    print(info[info_command[1]])
                elif info_command[1]=="app" and len(info_command)==3:
                    command="from termcolor import colored\ntry:\n    import app."+info_command[2]+"\n    print(app."+info_command[2]+""".__annotations__)\nexcept ModuleNotFoundError or NameError:\n    print(colored("L'app indiquée n'existe pas","yellow",attrs=["bold"]))"""
                    subprocess.run([sys.executable, "-c",command])
                else:
                    print(colored("Le module/app n'existe pas","yellow",attrs=["bold"]))
            else:
                print(colored("La commande est mal formulé","red",attrs=["bold"]))
#################################
#Store uninstall
#################################
        elif rep.startswith("store uninstall "):
            uninstall=rep[16::]
            if uninstall in app:
                if app.get(uninstall)=="1":
                    app.update({uninstall:"0"})
                    uninstall1=colored("Le module ","blue",attrs=["bold"])+colored(uninstall,"blue",attrs=["bold","underline"])+colored(" a bien été desinstallé","blue",attrs=["bold"])
                    print(uninstall1)
                    if uninstall=="random":
                        appt=open("save_txt/random.txt","w")
                        appt.write(app.get("random"))
                        appt.close()
                    if uninstall=="time":
                        appt=open("save_txt/time.txt","w")
                        appt.write(app.get("time"))
                        appt.close()
                    if uninstall=="music":
                        appt=open("save_txt/music.txt","w")
                        appt.write(app.get("music"))
                        appt.close()
                    if uninstall=="uuid":
                        appt=open("save_txt/uuid.txt","w")
                        appt.write(app.get("uuid"))
                        appt.close()
                    if uninstall=="image":
                        appt=open("save_txt/image.txt","w")
                        appt.write(str(app.get("image")))
                        appt.close()
                    if uninstall=="browser":
                        appt=open("save_txt/browser.txt","w")
                        appt.write(str(app.get("browser")))
                        appt.close()
                    if uninstall=="print":
                        appt=open("save_txt/print.txt","w")
                        appt.write(str(app.get("print")))
                        appt.close()
                    if uninstall=="maths":
                        appt=open("save_txt/maths.txt","w")
                        appt.write(str(app.get("maths")))
                        appt.close()
                    if uninstall=="download":
                        appt=open("save_txt/download.txt","w")
                        appt.write(str(app.get("download")))
                        appt.close()
                    if uninstall=="prompt":
                        appt=open("save_txt/prompt.txt","w")
                        appt.write(str(app.get("prompt")))
                        appt.close()
                else:
                    print(colored("Le module que vous essayez de désinstaller n'est pas installée","yellow",attrs=["bold"]))
            else:
                print(colored("Le module que vous voulez desinstaller n'existe pas","yellow",attrs=["bold"]))
#################################
#Mot de passe modification
#################################
        elif rep.startswith("mdp"):
            mdp=rep.split()
            if displaysplit==1:
                print(mdp)
            if len(mdp)==1:
                if not mdpt=="6":
                    mdpdise="Le mot de passe est : "+mdpt
                    print(colored(mdpdise,"blue",attrs=["bold"]))
                else:
                    print(colored("Le mot de passe est désactivé","blue",attrs=["bold"]))
            elif len(mdp)==2:
                if type(mdp[1])==str:
                    if mdp[1]=="act":
                        if mdpt=="6":
                            mdpt=input("Taper votre nouveau mot de passe : ")
                            mdptext=open("save_txt/mdp.txt","w")
                            mdptext.write(mdpt)
                            mdptext.close()
                        else:
                            print(colored("Le mot de passe est déja activé","yellow",attrs=["bold"]))
                    elif mdp[1]=="disact":
                        if not mdpt=="6":
                            print(colored("Le mot de passe a bien été désactivé","blue",attrs=["bold"]))
                            mdpt="6"
                            mdptext=open("save_txt/mdp.txt","w")
                            mdptext.write(mdpt)
                            mdptext.close()
                        else:
                            print(colored("Le mot de passe est déja desactivé","yellow",attrs=["bold"]))
                    else:
                        print(colored("La commande n'est pas bien formulée","red",attrs=["bold"]))
                else:
                    print(colored("La commande n'est pas bien formulée","red",attrs=["bold"]))
            else:
                print(colored("La commande n'est pas bien formulée","red",attrs=["bold"]))
#################################
#Update
#################################
        elif rep.startswith("update"):
            update=rep.split()
            if displaysplit==1:
                print(update)
            if len(update)==2:    
                if update[1]=="upgrade":
                    print(colored("Vous allez télécharger le fichier zip contenant les fichiers d'installation\nExtrayer dans le dossier de fonctionnement de ce fichier python puis supprimmer tous les fichiers de l'ancienne version\nEnfin, démmarer le fichier CmdOS.py et indiquer le chemin d'accès du dossier de l'ancienne version","blue"))
                    webbrowser.open("https://github.com/lolo859/CmdOS/archive/refs/heads/main.zip")
                elif update[1]=="check":
                    versiontxt=req.get("https://biotech-online.pagesperso-orange.fr/Mathias/cmdversion",allow_redirects=True)
                    open("cmdversion.txt","wb").write(versiontxt.content)
                    vertxt=open("cmdversion.txt","r")
                    verlist=vertxt.readlines()
                    vertxt.close()
                    if str(verlist[0])==version:
                        versionprint="CmdOS "+version
                        print(colored(versionprint,"green",attrs=["bold"]))
                        print(colored("Votre système est à jour","blue",attrs=["bold"]))
                    elif str(verlist[0])<version:
                        versionprint="Vous êtes actuellement sur la version de développement "+version
                        print(colored(versionprint,"blue",attrs=["bold"]))
                        print(colored("Cette version peut être instable","yellow",attrs=["bold"]))
                        print(colored("Vous pouvez retourner à la version public avec update upgrade","blue",attrs=["bold"]))
                    else:
                        print(colored("Votre système n'est pas a jour","yellow",attrs=["bold"]))
                        versionprint="La dernière version disponible est CmdOS "+verlist[0]
                        print(colored(versionprint,"yellow",attrs=["bold"]))
                        print(colored("Vous pouvez mettre a jour le système avec update upgrade","blue",attrs=["bold"]))
                else:
                    print(colored("La commande est mal formulée","red",attrs=["bold"]))
            else:
                print(colored("La commande est mal formulée","red",attrs=["bold"]))
#################################
#Store list
#################################
        elif rep=="store list":
            if app.get("random")=="1":
                print(colored("Le module random est installé","blue",attrs=["bold"]))
            else:
                print(colored("Le module random n'est pas installé","blue",attrs=["bold"]))
            if app.get("time")=="1":
                print(colored("Le module time est installé","blue",attrs=["bold"]))
            else:
                print(colored("Le module time n'est pas installé","blue",attrs=["bold"]))
            if app.get("music")=="1":
                print(colored("Le module music est installé","blue",attrs=["bold"]))
            else:
                print(colored("Le module music n'est pas installé","blue",attrs=["bold"]))
            if app.get("uuid")=="1":
                print(colored("Le module uuid est installé","blue",attrs=["bold"]))
            else:
                print(colored("Le module uuid n'est pas installé","blue",attrs=["bold"]))
            if app.get("image")=="1":
                print(colored("Le module image est installé","blue",attrs=["bold"]))
            else:
                print(colored("Le module image n'est pas installé","blue",attrs=["bold"]))
            if app.get("browser")=="1":
                print(colored("Le module browser est installé","blue",attrs=["bold"]))
            else:
                print(colored("Le module browser n'est pas installé","blue",attrs=["bold"]))
            if app.get("print")=="1":
                print(colored("Le module print est installé","blue",attrs=["bold"]))
            else:
                print(colored("Le module print n'est pas installé","blue",attrs=["bold"]))
            if app.get("maths")=="1":
                print(colored("Le module maths est installé","blue",attrs=["bold"]))
            else:
                print(colored("Le module maths n'est pas installé","blue",attrs=["bold"]))
            if app.get("download")=="1":
                print(colored("Le module download est installé","blue",attrs=["bold"]))
            else:
                print(colored("Le module download n'est pas installé","blue",attrs=["bold"]))
            if app.get("prompt")=="1":
                print(colored("Le module prompt est installé","blue",attrs=["bold"]))
            else:
                print(colored("Le module prompt n'est pas installé","blue",attrs=["bold"]))
#################################
#Clear
#################################
        elif rep=="clear":
            os.system("clear")
#################################
#Godmode
#################################
        elif rep=="godmode":
            if admin==1:
                print(colored("Le godmode est un ensemble de fonctions et de paramètres conçus pour les dévéloppeurs, n'y toucher seulement si vous savez ce que vous faites","yellow",attrs=["bold"]))
                godmode1=input(colored("Quelle fonction voulez vous activer/utilisez ? : ","blue",attrs=["bold"]))
                if godmode1=="sys.variables":
                    print("Cette fonction permet d'afficher la valeur des variables systèmes")
                    input("Taper entrer pour exécuter")
                    print("mdpt='"+mdpt+"'")
                    print("app='"+str(app)+"'")
                    print("adresse='"+adresse+"'")
                    print("repmdp='"+repmdp+"'")
                    print("version='"+version+"'")
                    print("godmode1='"+godmode1+"'")
                if godmode1=="sys.store.install.vanish_loading":
                    print("Cette fonction permet de masquer le chargement lors de l'installation d'un module")
                    input("Taper entrer pour exécuter")
                    vanish_loading="Entrer votre choix (valeur actuelle : "+str(charginstall)+") : "
                    godmode2=input(vanish_loading)
                    if int(godmode2)==1 or int(godmode2)==0 :
                        charginstall=int(godmode2)
                    else:
                        print("La valeur entrée n'est pas correcte")
                if godmode1=="sys.protocol.list":
                    print("Cette fonction permet de voir quel protocole système fait quelle action")
                    input("Taper entrer pour exécuter")
                    print("login() - protocole qui demande le mot de passe et lance le protocole cmd()")
                    print("cmd() - protocole qui gère les interactions avec l'utilisateur")
                    print("appinitext() - protocole qui récupère les modules installés ou non")
                    print("charg(chrag1=0.1,t=colored(\"Démarrage du système...\",\"blue\",attrs=[\"bold\"])) - protocole qui permet un chargement visuel")
                if godmode1=="sys.protocol.execute":
                    print("Cette fonction éxécute le protocole demandé (elle positionne automatiquement les arguments)")
                    input("Taper entrer pour exécuter")
                    godmode2=input("Quel protocole voulez vous éxécuter ? : ")
                    if godmode2=="appintext":
                        appinitext()
                    if godmode2=="cmd":
                        cmd()
                    if godmode2=="login":
                        login()
                if godmode1=="sys.protocol.cmd.display_split":
                    print("Cette fonction permet d'afficher le split de la variable rep lors du traitement de la commande")
                    input("Taper entrer pour exécuter")
                    display_split="Entrer votre choix (valeur actuelle : "+str(displaysplit)+") : "
                    godmode3=input(display_split)
                    if int(godmode3)==1 or int(godmode3)==0 :
                        displaysplit=int(godmode3)
                    else:
                        print("La valeur entrée n'est pas correcte")
                if godmode1=="sys.report":
                    print("Cette fonction permet d'activer/désactiver l'enregistrement des commandes sur le serveur de support")
                    input("Taper entrer pour exécuter")
                    report="Entrer votre choix (valeur actuelle : "+str(logserver)+") : "
                    godmode4=input(report)
                    if int(godmode4)==1 or int(godmode4)==0 :
                        logserver=int(godmode4)
                    else:
                        print("La valeur entrée n'est pas correcte")
            else:
                print(colored("Vous devez être connecté en tant qu'administrateur pour utiliser le godmode","red",attrs=["bold"]))
###############################
#Module                       #
###############################
        elif rep.startswith("random"):
            if app.get("random")=="1":
                module.random.execute(displaysplit,rep)
            else:
                print(colored("Ce module n'est pas installé ou n'est pas bien formulé","red",attrs=["bold"]))
        elif rep.startswith("time"):
            if app.get("time")=="1":
                module.time.execute(displaysplit,rep)
            else:
                print(colored("Ce module n'est pas installé ou n'est pas bien formulé","red",attrs=["bold"]))
        elif rep.startswith("music"):
            if app.get("music")=="1":
                module.music.execute(displaysplit,rep,adresse)
            else:
                print(colored("Ce module n'est pas installé ou n'est pas bien formulé","red",attrs=["bold"]))
        elif rep=="uuid":
            if app.get("uuid")=="1":
                module.uuid.execute()
            else:
                print(colored("Ce module n'est pas installé ou n'est pas bien formulé","red",attrs=["bold"]))
        elif rep.startswith("image"):
            if app.get("image")=="1":
                module.image.execute(displaysplit,rep,adresse)
            else:
                print(colored("Ce module n'est pas installé ou n'est pas bien formulé","red",attrs=["bold"]))
        elif rep.startswith("browser"):
            if app.get("browser")=="1":
                module.browser.execute(displaysplit,rep)
            else:
                print(colored("Ce module n'est pas installé ou n'est pas bien formulé","red",attrs=["bold"]))
        elif rep.startswith("print"):
            if app.get("print")=="1":
                module.print.execute(displaysplit,rep)
            else:
                print(colored("Ce module n'est pas installé ou n'est pas bien formulé","red",attrs=["bold"]))
        elif rep.startswith("maths"):
            if app.get("maths")=="1":
                module.maths.execute(displaysplit,rep)
            else:
                print(colored("Ce module n'est pas installé ou n'est pas bien formulé","red",attrs=["bold"]))
        elif rep.startswith("download"):
            if app.get("download")=="1":
                module.download.execute(displaysplit,rep)
            else:
                print(colored("Ce module n'est pas installé ou n'est pas bien formulé","red",attrs=["bold"]))
        elif rep.startswith("prompt"):
            if app.get("prompt")=="1":
                module.prompt.execute(displaysplit,rep)
            else:
                print(colored("Ce module n'est pas installé ou n'est pas bien formulé","red",attrs=["bold"])) 
#################################
#Commande n'existe pas
#################################
        else:
            if not rep=="":
                print(rep,": cette commande n'existe pas : essayer help")
#################################
#Login
#################################
def login():
    if not mdpt=="6":
        print("Taper",colored("shutdown",attrs=["bold"]),"pour éteindre")
        repmdp=input("Taper votre mot de passe : ")
        if repmdp==mdpt:
            os.system("clear")
            print(colored("""Cmd OS v2.0""","green",attrs=["bold"])) 
            print("""Taper""",colored("help",attrs=["bold"]),"""pour plus d'information""")
            cmd()
            return
        elif repmdp=="shutdown":
            return
        else:
            print("Le mot de passe est incorrect")
            os.system("clear")
    else:
        print("""Taper "help" pour plus d'information""")
        cmd()
        return
while True :
    login()
    break
connect.quit()
os.system("clear")