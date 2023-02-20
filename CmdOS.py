#####################################################################
#Import et clear
####################################################################
from cgitb import text
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
import ftplib
import uuid
import subprocess
import sys
import webbrowser
import secure_id
import psycopg2
import shutil
cmdf.clear()
#########################################################################
#Admin, commande
#########################################################################
if (len(sys.argv)==2 and sys.argv[1]=="admin") or (len(sys.argv)==1 and sys.argv[0]=="admin"):
    admin=1
else:
    admin=0
a=0
com={"help":"Voici la liste des commandes de Cmd OS :""\nhelp - Afficher la liste des commandes"
     "\ninfo - Afficher les infos sur un programme / utliser sys pour voir la version du système / utiliser 'info app (fichier python)' pour afficher les caractéristiques d'un fichier python du dossier app"
     "\nstore - Affiche les différentes applications installables : \n   install - installer un module \n   uninstall - desinstaller un module""\n   list - affiche les différents modules installés"
     "\ncd - changer de dossier :\n   cd <chemin absolu>\n   cd <dossier à ouvrir>\n   cd .. : ouvre le dossier parent"
     "\ndir - permet de voir les fichiers/dossiers"
     "\nuser - Voir vos identifiants :\n   user - modifie votre nom d'utilisateur\n   password - modifie votre mot de passe\n   disconnect - déconnecte votre compte de l'appareil\n   delete - supprime totalement votre compte"
     "\nren - renomer un fichier"
     "\nupdate :""\n   upgrade - mettre à jour le système en téléchargant la dernière version""\n   check - vérifier si une nouvelle mise à jour est disponible"
     "\nadmin - active ou désactive le mode admin"
     "\nlog - affiche les logs (il faut être connecté en tant qu'administrateur pour utiliser cette commande)""\n   show - affiche les logs""\n   delete - supprime les logs"
     "\ndetail - affiche les propriétés d'un fichier ou dossier sous forme de os.stat_result"
     "\nshell (version raccourci : sh) - ouvre le cmd"
     "\nexecute - permet d'éxécuter des fonctions exterieures au système"
     "\nunlog - déconnecte l'utilisateur"}
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
def appinitext(repname):
    if not os.path.exists("user/"+repname+"/save_module/random.txt"):
        randomtext=open("user/"+repname+"/save_module/random.txt","w")
        randomtext.write(app["random"])
        randomtext.close()
    else:
        import module.random
        randomtext=open("user/"+repname+"/save_module/random.txt",'r')
        data=randomtext.readlines()
        app.update({"random":str(data[0])})
        randomtext.close()
    if not os.path.exists("user/"+repname+"/save_module/time.txt"):
        timetext=open("user/"+repname+"/save_module/time.txt","w")
        timetext.write(app["time"])
        timetext.close()
    else:
        import module.time
        timetext=open("user/"+repname+"/save_module/time.txt",'r')
        data=timetext.readlines()
        app.update({"time":str(data[0])})
        timetext.close()
    if not os.path.exists("user/"+repname+"/save_module/music.txt"):
        musictext=open("user/"+repname+"/save_module/music.txt","w")
        musictext.write(app["music"])
        musictext.close()
    else:
        import module.music
        musictext=open("user/"+repname+"/save_module/music.txt",'r')
        data=musictext.readlines()
        app.update({"music":str(data[0])})
        musictext.close()
    if not os.path.exists("user/"+repname+"/save_module/uuid.txt"):
        uuidtext=open("user/"+repname+"/save_module/uuid.txt","w")
        uuidtext.write(app["uuid"])
        uuidtext.close()
    else:
        import module.uuid
        uuidtext=open("user/"+repname+"/save_module/uuid.txt",'r')
        data=uuidtext.readlines()
        app.update({"uuid":str(data[0])})
        uuidtext.close()
    if not os.path.exists("user/"+repname+"/save_module/image.txt"):
        imagetext=open("user/"+repname+"/save_module/image.txt","w")
        imagetext.write(app["image"])
        imagetext.close()
    else:
        import module.image
        imagetext=open("user/"+repname+"/save_module/image.txt",'r')
        data=imagetext.readlines()
        app.update({"image":str(data[0])})
        imagetext.close()
    if not os.path.exists("user/"+repname+"/save_module/browser.txt"):
        browsertext=open("user/"+repname+"/save_module/browser.txt","w")
        browsertext.write(app["browser"])
        browsertext.close()
    else:
        import module.browser
        browsertext=open("user/"+repname+"/save_module/browser.txt",'r')
        data=browsertext.readlines()
        app.update({"browser":str(data[0])})
        browsertext.close()
    if not os.path.exists("user/"+repname+"/save_module/print.txt"):
        printtext=open("user/"+repname+"/save_module/print.txt","w")
        printtext.write(app["print"])
        printtext.close()
    else:
        import module.print
        printtext=open("user/"+repname+"/save_module/print.txt",'r')
        data=printtext.readlines()
        app.update({"print":str(data[0])})
        printtext.close()
    if not os.path.exists("user/"+repname+"/save_module/maths.txt"):
        mathstext=open("user/"+repname+"/save_module/maths.txt","w")
        mathstext.write(app["maths"])
        mathstext.close()
    else:
        import module.maths
        mathstext=open("user/"+repname+"/save_module/maths.txt",'r')
        data=mathstext.readlines()
        app.update({"maths":str(data[0])})
        mathstext.close()
    if not os.path.exists("user/"+repname+"/save_module/download.txt"):
        downloadtext=open("user/"+repname+"/save_module/download.txt","w")
        downloadtext.write(app["download"])
        downloadtext.close()
    else:
        import module.download
        downloadtext=open("user/"+repname+"/save_module/download.txt",'r')
        data=downloadtext.readlines()
        app.update({"download":str(data[0])})
        downloadtext.close()
    if not os.path.exists("user/"+repname+"/save_module/prompt.txt"):
        prompttext=open("user/"+repname+"/save_module/prompt.txt","w")
        prompttext.write(app["prompt"])
        prompttext.close()
    else:
        import module.prompt
        prompttext=open("user/"+repname+"/save_module/prompt.txt",'r')
        data=prompttext.readlines()
        app.update({"prompt":str(data[0])})
        prompttext.close()
    return app
############################################
#Info
############################################
info={"sys":"CmdOS v2.4 - Basé en Python",
      "system":"CmdOS v2.4 - Basé en Python",
      "time":"Module Time""\nVersion : 1.0""\nAuteur : système""\nPermission : displaysplit, rep",
      "random":"Module Random""\nVersion : 1.2""\nAuteur : système""\nPermission : displaysplit, rep",
      "music":"Module Music""\nVersion : 1.2""\nAuteur : système""\nPermission : displaysplit, rep, adresse""\nNote : basé avec le module simpleaudio",
      "uuid":"Module Uuid""\nVersion : 1.0""\nAuteur : système""\nPermission : displaysplit, rep""\nNote : basé avec le module uuid4",
      "image":"Module Image""\nVersion : 1.0""\nAuteur : système""\nPermission : displaysplit, rep, adresse""\nNote : basé avec le module PIL",
      "browser":"Module Browser""\nVersion : 1.0""\nAuteur : système""\nPermission : displaysplit, rep""\nNote : basé avec le module browser",
      "print":"Module Print""\nVersion : 1.0""\nAuteur : système""\nPermission : displaysplit, rep""\nNote : basé avec le module termcolor",
      "maths":"Module Maths""\nVersion : 1.1""\nPermission : displaysplit, rep""\nAuteur : système",
      "download":"Module Download""\nVersion : 1.1""\nAuteur : système""\nPermission : adresseuser, displaysplit, rep""\nNote : basé sur le module request",
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
if not(os.path.exists(adresse+"/README.md") and os.path.exists(adresse+"/__pycache__") and os.path.exists(adresse+"/module") and os.path.exists(adresse+"/app") and os.path.exists(adresse+"/user")):
    print(colored("Le système ne peut pas fonctionner dans son intégrité car certain dosssier/fichier ne sont pas présents.\nVeulliez vous assurez que les dossier suivant existe:  __pycache__, app, module et README.md.","red",attrs=["bold"]))
    quit()
############################################
#Connexion
############################################
print(colored("""CmdOS v2.4""","green",attrs=["bold"])) 
host="ftp-cmdos.alwaysdata.net"
user="cmdos"
password="CmdOS2008)"
connect=FTP(host,user,password)
connect.sendcmd('CWD www')
connect.sendcmd("CWD command")
connsql = psycopg2.connect(user = "cmdos",password = "CmdOS2008)",host = "postgresql-cmdos.alwaysdata.net",port = "5432",database = "cmdos_user")
cur = connsql.cursor()
charginstall=1
displaysplit=0
logserver=1
version="2.4"
##########################
#Fonction Cmd
##########################
def cmd(admin,charginstall,displaysplit,logserver,repname,mdpt,adresseuser):
#################################
#Variable, module
#################################
    global adresse,app,mdptext,repmdp,connect,version,a
    log=["Voici les logs :"]
    store="Bienvenue dans le store de CmdOS, voici les modules disponibles :"+"\nrandom - générer un nombre aléatoire"+"\ntime - attendre un temps"+"\nmusic - permet de jouer un son"+"\nuuid - générer des identifiants aléatoire"+"\nimage - permet d'afficher une image"+"\nbrowser - permet d'afficher une page web"+"\nprint - permet d'afficher du texte en couleur dans la console"+"\ndownload - permet de télécharger une page web"+"\nprompt - permet d'éxécuter des commandes de l'invite de commande"+"\nPour installer un module, faites <<store install>> suivie du nom du module"+"\nPour desinstaller un module, faites <<store uninstall>> suivie du nom du module"+"\nPour voir la liste des modules installés faites <<store list>>"
    while True:
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
###########################################
#Gestion entrée utilisateur et result
###########################################
        if admin==0:
            demande=colored(repname,"green",attrs=["bold"])+colored("@","green",attrs=["bold"])+colored(adresse,"blue",attrs=["bold"])+" >>> "
        else:
            demande=colored(repname,"green",attrs=["bold"])+colored("(admin)","red",attrs=["bold"])+colored("@","green",attrs=["bold"])+colored(adresse,"blue",attrs=["bold"])+" >>> "
        rep=input(demande)
        class Result():
            def __init__(self,text,rt,module=None,object=None):
                self.resultType=rt
                self.module=module
                self.text=text
                self.object=object
            def print(self):
                ResultType=["error","stdout","notfound","advert","important","version"]
                if self.resultType in ResultType:
                    if self.resultType=="error":
                        print(colored((self.module+" : "+self.text),"red",attrs=["bold"]))
                    if self.resultType=="stdout":
                        print(self.text)
                    if self.resultType=="notfound":
                        texte=self.module+" : L'élément '"+self.object+"' n'existe pas, n'a pas pu être trouvé ou n'est pas du type attendu"
                        print(colored(texte,"yellow",attrs=["bold"]))
                    if self.resultType=="advert":
                        print(colored(self.text,"yellow",attrs=["bold"]))
                    if self.resultType=="important":
                        print(colored(self.text,"blue",attrs=["bold"]))
            def split():
                print(rep.split())
            def version():
                print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
#################################
#Ajout de commande a log
#################################
        try:
            if admin==1:
                heure=str(datetime.now())
                if logserver==1:
                    id=str(secure_id.sid2())
                    contenttxt=open("content.txt","w")
                    contenttxt.write(repname+"(admin) "+heure+" "+version+" "+rep)
                    contenttxt.close()
                    contenttxt=open("content.txt","rb")
                    connect.storbinary("STOR "+id,contenttxt)
                    contenttxt.close()
                    log.append(id+" "+colored(repname,"green",attrs=["bold"])+colored("(admin) ","red",attrs=["bold"])+colored(heure,"blue",attrs=["bold"])+" "+rep)
                else:
                    log.append(colored(repname,"green",attrs=["bold"])+colored("(admin) ","red",attrs=["bold"])+colored(heure,"blue",attrs=["bold"])+" "+rep)
            else:
                heure=str(datetime.now())
                if logserver==1:
                    id=str(secure_id.sid2())
                    contenttxt=open("content.txt","w")
                    contenttxt.write(repname+" "+heure+" "+version+" "+rep)
                    contenttxt.close()
                    contenttxt=open("content.txt","rb")
                    connect.storbinary("STOR "+id,contenttxt)
                    contenttxt.close()
                    log.append(id+" "+colored(repname,"green",attrs=["bold"])+" "+colored(heure,"blue",attrs=["bold"])+" "+rep)
                else:
                    log.append(colored(repname,"green",attrs=["bold"])+" "+colored(heure,"blue",attrs=["bold"])+" "+rep)
        except ftplib.error_temp:
            host="ftp-cmdos.alwaysdata.net"
            user="cmdos"
            password="CmdOS2008)"
            connect=FTP(host,user,password)
            connect.sendcmd('CWD www')
            connect.sendcmd("CWD command")
        if rep in com:
            i=Result(text=com[rep],rt="stdout")
            i.print()
#################################
#Store
#################################
        elif rep=="store":
            i=Result(store,rt="stdout")
            i.print()
#################################
#Detail
#################################
        elif rep.startswith("detail"):
            detail1=rep.split()
            if displaysplit==1:
                Result.split()
            if len(detail1)>1:
                detail2=rep[7::]
                fichiers = os.listdir(adresse)
                if detail2 in fichiers:
                    detail3=adresse+"/"+detail2
                    i=Result(os.stat(detail3),rt="stdout")
                    i.print()
                else:
                    i=Result(module="detail",object=detail2,rt="notfound",text=None)
                    i.print()
            else:
                i=Result(module="detail",text="La commande est mal formulée",rt="error")
                i.print()
#################################
#Admin
#################################
        elif rep.startswith("admin"):
            admin1=rep.split()
            if displaysplit==1:
                Result.split()
            if len(admin1)==2:
                if admin1[1]=="on":
                    if admin==0:
                        demande=colored("Taper votre mot de passe : ","blue",attrs=["bold"])
                        repmdp=input(demande)
                        if repmdp==mdpt:
                            admin=1
                            commandsql="UPDATE utilisateur SET admin='1' WHERE nom='"+repname+"';"
                            cur.execute(commandsql)
                            connsql.commit()
                        else:
                            i=Result(module="admin",text="Le mot de passe est incorrect",rt="error")
                            i.print()
                    else:
                       i=Result(text="Le mode admin est déja activé",rt="important")
                       i.print()
                elif admin1[1]=="off":
                    if admin==1:
                        admin=0
                        commandsql="UPDATE utilisateur SET admin='0' WHERE nom='"+repname+"';"
                        cur.execute(commandsql)
                        connsql.commit()
                    else:
                        i=Result("Le mode admin est déja désactivé","important")
                        i.print()
                else:
                    i=Result("La commande est mal formulée","error",module="admin")
                    i.print()
            else:
                i=Result("La commande est mal formulée","error",module="admin")
                i.print()
#################################
#Supprimer
#################################
        elif rep.startswith("del"):
            supr=rep.split()
            if displaysplit==1:
                Result.split()
            if len(supr)==2:
                fichiers = os.listdir(adresse)
                if supr[1] in fichiers:
                    del_1=adresse+"/"+supr[1]
                    os.remove(del_1)
                else:
                    i=Result(module="del",object=supr[1],rt="notfound",text=None)
                    i.print()
            else:
                i=Result("La commande est mal formulée","error",module="del")
                i.print()
#################################
#Renommer
#################################
        elif rep.startswith("ren"):
            ren=rep[4::]
            fichiers = os.listdir(adresse)
            if ren in fichiers:
                ren2=adresse+"/"+ren
                ren3=input("Nouveau nom : ")
                os.rename(ren2, ren3)
            else:
                i=Result(module="ren",object=ren,rt="notfound",text=None)
                i.print()
#################################
#Cd : change directory
#################################
        elif rep.startswith("cd"):
            cd=rep.split()
            if displaysplit==1:
                Result.split()
            if len(cd)>=2:
                if not rep[3::]=="..":
                    if os.path.exists(rep[3::]) and rep[3::].find("/")==True:
                        adresse=rep[3::]
                    elif rep[3::].find("/"):
                        fichiers=os.listdir(adresse)
                        if rep[3::] in fichiers and os.path.isdir(os.path.join(adresse,rep[3::])):
                            adresse=os.path.join(adresse,rep[3::])
                        else:
                            i=Result(module="cd",object=rep[3::],rt="notfound",text=None)
                            i.print()
                    else:
                        i=Result("Le dossier n'est pas valide","error",module="cd")
                        i.print()
                else:
                    adresse=os.path.dirname(adresse)
            else:
                i=Result("La commande est mal formulée","error",module="cd")
                i.print()
#################################
#Dir : directory
#################################
        elif rep=="dir":
            fichiers = os.listdir(adresse)
            longueur=len(fichiers)
            i=Result("Voici les fichiers/dossiers dans ce dossier :",rt="stdout")
            i.print()
            for element in range(longueur):
                i=Result(" "+fichiers[element],rt="stdout")
                i.print()
#################################
#Logs
#################################
        elif rep.startswith("log"):
            if admin==1:
                log1=rep.split()
                if displaysplit==1:
                    Result.split()
                if len(log1)==2 and type(log1[1])==str:
                    if log1[1]=="show":
                        for lettre in log:
                            i=Result(lettre,rt="stdout")
                    elif log1[1]=="delete":
                        log=["Voici les logs :"]
                        i.Result("Les logs ont bien été supprimé","important")
                        i.print()
                    else:
                        i=Result("La commande est mal formulée","error",module="log")
                        i.print()
                else:
                    i=Result("La commande est mal formulée","error",module="log")
                    i.print()
            else:
                i=Result("Vous devez être connecté en tant qu'administrateur pour utiliser cette commande","error",module="log")
                i.print()
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
                i=Result(install2,"stdout")
                i.print()
                if install=="random":
                    import module.random
                    appt=open("user/"+repname+"/save_module/random.txt","w")
                    appt.write(app.get("random"))
                    appt.close()
                if install=="time":
                    import module.time
                    appt=open("user/"+repname+"/save_module/time.txt","w")
                    appt.write(app.get("time"))
                    appt.close()
                if install=="music":
                    import module.music
                    appt=open("user/"+repname+"/save_module/music.txt","w")
                    appt.write(app.get("music"))
                    appt.close()
                if install=="uuid":
                    import module.uuid
                    appt=open("user/"+repname+"/save_module/uuid.txt","w")
                    appt.write(app.get("uuid"))
                    appt.close()
                if install=="image":
                    import module.image
                    appt=open("user/"+repname+"/save_module/image.txt","w")
                    appt.write(app.get("image"))
                    appt.close()
                if install=="browser":
                    import module.browser
                    appt=open("user/"+repname+"/save_module/browser.txt","w")
                    appt.write(app.get("browser"))
                    appt.close()
                if install=="print":
                    import module.print
                    appt=open("user/"+repname+"/save_module/print.txt","w")
                    appt.write(app.get("print"))
                    appt.close()
                if install=="maths":
                    import module.maths
                    appt=open("user/"+repname+"/save_module/maths.txt","w")
                    appt.write(app.get("maths"))
                    appt.close()
                if install=="download":
                    import module.download
                    appt=open("user/"+repname+"/save_module/download.txt","w")
                    appt.write(app.get("download"))
                    appt.close()
                if install=="prompt":
                    import module.prompt
                    appt=open("user/"+repname+"/save_module/prompt.txt","w")
                    appt.write(app.get("prompt"))
                    appt.close()
            else:
                i=Result(module="store",object="module",rt="notfound",text=None)
                i.print()
#################################
#Execute
#################################
        elif rep.startswith("execute"):
            impor=rep.split()
            if displaysplit==1:
                Result.split()
            if len(impor)==3:
                command="from app."+impor[1]+" import *\ntry:\n    "+impor[2]+"()\nexcept ModuleNotFoundError or NameError:\n    pass"
                subprocess.run([sys.executable, "-c",command])
            else:
                i=Result("La commande est mal formulée","error",module="execute")
                i.print()
#################################
#Shell
#################################
        elif rep=="shutdown" or rep=="sh" or rep=="shell":
            cmdf.clear()
            sys.exit()
#################################
#Info
#################################
        elif rep.startswith("info"):
            info_command=rep.split()
            if displaysplit==1:
                print(info_command)
            if len(info_command)==2 or len(info_command)==3:
                if info_command[1] in info:
                    i=Result(info[info_command[1]],"stdout")
                    i.print()
                elif info_command[1]=="app" and len(info_command)==3:
                    command="from termcolor import colored\ntry:\n    import app."+info_command[2]+"\n    print(app."+info_command[2]+""".__annotations__)\nexcept ModuleNotFoundError or NameError:\n    print(colored("L'app indiquée n'existe pas","yellow",attrs=["bold"]))"""
                    subprocess.run([sys.executable, "-c",command])
                else:
                    i=Result(module="info",object="module / app",rt="notfound",text=None)
                    i.print()
            else:
                i=Result("La commande est mal formulée","error",module="info")
                i.print()
#################################
#Store uninstall
#################################
        elif rep.startswith("store uninstall "):
            uninstall=rep[16::]
            if uninstall in app:
                app.update({uninstall:"0"})
                uninstall1=colored("Le module ","blue",attrs=["bold"])+colored(uninstall,"blue",attrs=["bold","underline"])+colored(" a bien été desinstallé","blue",attrs=["bold"])
                i=Result(uninstall1,"stdout")
                i.print()
                if uninstall=="random":
                    appt=open("user/"+repname+"/save_module/random.txt","w")
                    appt.write(app.get("random"))
                    appt.close()
                if uninstall=="time":
                    appt=open("user/"+repname+"/save_module/time.txt","w")
                    appt.write(app.get("time"))
                    appt.close()
                if uninstall=="music":
                    appt=open("user/"+repname+"/save_module/music.txt","w")
                    appt.write(app.get("music"))
                    appt.close()
                if uninstall=="uuid":
                    appt=open("user/"+repname+"/save_module/uuid.txt","w")
                    appt.write(app.get("uuid"))
                    appt.close()
                if uninstall=="image":
                    appt=open("user/"+repname+"/save_module/image.txt","w")
                    appt.write(str(app.get("image")))
                    appt.close()
                if uninstall=="browser":
                    appt=open("user/"+repname+"/save_module/browser.txt","w")
                    appt.write(str(app.get("browser")))
                    appt.close()
                if uninstall=="print":
                    appt=open("user/"+repname+"/save_module/print.txt","w")
                    appt.write(str(app.get("print")))
                    appt.close()
                if uninstall=="maths":
                    appt=open("user/"+repname+"/save_module/maths.txt","w")
                    appt.write(str(app.get("maths")))
                    appt.close()
                if uninstall=="download":
                    appt=open("user/"+repname+"/save_module/download.txt","w")
                    appt.write(str(app.get("download")))
                    appt.close()
                if uninstall=="prompt":
                    appt=open("user/"+repname+"/save_module/prompt.txt","w")
                    appt.write(str(app.get("prompt")))
                    appt.close()
            else:
                i=Result(module="store",object="module",rt="notfound",text=None)
                i.print()
#################################
#Compte modification
#################################
        elif rep.startswith("user"):
            user=rep.split()
            if displaysplit==1:
                print(user)
            if len(user)==1:
                i=Result(("Votre nom d'utilisateur : "+repname),"important")
                i.print()
                i=Result(("Votre mot de passe : "+mdpt),"important")
                i.print()
            elif len(user)==2:
                if type(user[1])==str:
                    if user[1]=="name":
                        answer=input("Taper votre nouveau nom d'utilisateur (pas plus de 50 caractères) : ")
                        try:
                            if not len(answer)>=50:
                                commandsql="UPDATE utilisateur SET nom='"+str(answer)+"' WHERE nom='"+str(repname)+"';"
                                cur.execute(commandsql)
                                commandsql="UPDATE settings SET nom='"+str(answer)+"' WHERE nom='"+str(repname)+"';"
                                cur.execute(commandsql)
                                connsql.commit()
                                os.rename("user/"+repname,"user/"+answer)
                                adr=adresse.split("/")
                                num=len(adr)-1
                                adr[num]=answer
                                adresse="/"+"/".join(adr)
                                repname=answer
                            else:
                                i=Result("Le nom d'utilisateur est invalide",rt="error",module="user")
                                i.print()
                        except psycopg2.errors.UniqueViolation:
                            i=Result("Le nom d'utilisateur est déja pris",rt="error",module="user")
                            i.print()
                    elif user[1]=="password":
                        answer=input("Taper votre nouveau mot de passe (pas plus de 50 caractères) : ")
                        if not len(answer)>=50:
                            commandsql="UPDATE utilisateur SET mdp='"+str(answer)+"' WHERE nom='"+str(repname)+"';"
                            cur.execute(commandsql)
                            connsql.commit()
                            mdpt=answer
                        else:
                            i=Result("Le mot de passe est invalide",rt="error",module="user")
                            i.print()
                    elif user[1]=="disconnect":
                        answer=input("Voulez vous vraiment déconnecter votre compte ? (o/n) : ")
                        if answer=="o":
                            shutil.rmtree(adresseuser)
                            a=1
                            return
                    elif user[1]=="delete":
                        answer=input("Voulez vous vraiment supprimer votre compte ? (o/n) : ")
                        if answer=="o":
                            shutil.rmtree(adresseuser)
                            commandsql="DELETE FROM utilisateur WHERE nom='"+repname+"';"
                            cur.execute(commandsql)
                            connsql.commit()
                            commandsql="DELETE FROM settings WHERE nom='"+repname+"';"
                            cur.execute(commandsql)
                            connsql.commit()
                            a=1
                            return
                    else:
                        i=Result("La commande est mal formulée","error",module="user")
                        i.print()
                else:
                    i=Result("La commande est mal formulée","error",module="user")
                    i.print()
            else:
                i=Result("La commande est mal formulée","error",module="user")
                i.print()
#################################
#Update
#################################
        elif rep.startswith("update"):
            update=rep.split()
            if displaysplit==1:
                print(update)
            if len(update)==2:    
                if update[1]=="upgrade":
                    i=Result(text="Vous allez télécharger le fichier zip contenant l'assistant pour mettre à jour CmdOS",rt="important")
                    i.print()
                    webbrowser.open("https://github.com/lolo859/get-cmdos/archive/refs/heads/main.zip")
                elif update[1]=="check":
                    versiontxt=req.get("https://biotech-online.pagesperso-orange.fr/Mathias/cmdversion",allow_redirects=True)
                    open("cmdversion.txt","wb").write(versiontxt.content)
                    vertxt=open("cmdversion.txt","r")
                    verlist=vertxt.readlines()
                    vertxt.close()
                    if str(verlist[0])==version:
                        versionprint="CmdOS "+version
                        Result.version()
                        i=Result("Votre système est à jour",rt="important")
                        i.print()
                    elif str(verlist[0])<version:
                        versionprint="Vous êtes actuellement sur la version de développement "+version
                        i=Result(versionprint,"important")
                        i.print()
                        i=Result("Cette version peut être instable",rt="advert")
                        i.print()
                        i=Result("Vous pouvez retourner à la version public avec update upgrade","important")
                        i.print()
                    else:
                        i=Result("Votre système n'est pas a jour","advert")
                        i.prinr()
                        versionprint="La dernière version disponible est CmdOS "+verlist[0]+"\nVous pouvez mettre a jour le système avec update upgrade"
                        i=Result(versionprint,"important")
                        i.print()
                else:
                    i=Result("La commande est mal formulée","error",module="update")
                    i.print()
            else:
                i=Result("La commande est mal formulée","error",module="update")
                i.print()
#################################
#Store list
#################################
        elif rep=="store list":
            if app.get("random")=="1":
                i=Result("Le module random est installé",rt="stdout")
                i.print()
            else:
                i=Result("Le module random n'est pas installé",rt="stdout")
                i.print()
            if app.get("time")=="1":
                i=Result("Le module time est installé",rt="stdout")
                i.print()
            else:
                i=Result("Le module time n'est pas installé",rt="stdout")
                i.print()
            if app.get("music")=="1":
                i=Result("Le module music est installé",rt="stdout")
                i.print()
            else:
                i=Result("Le module music n'est pas installé",rt="stdout")
                i.print()
            if app.get("uuid")=="1":
                i=Result("Le module uuid est installé",rt="stdout")
                i.print()
            else:
                i=Result("Le module uuid n'est pas installé",rt="stdout")
                i.print()
            if app.get("image")=="1":
                i=Result("Le module image est installé",rt="stdout")
                i.print()
            else:
                i=Result("Le module image n'est pas installé",rt="stdout")
                i.print()
            if app.get("browser")=="1":
                i=Result("Le module browser est installé",rt="stdout")
                i.print()
            else:
                i=Result("Le module browser n'est pas installé",rt="stdout")
                i.print()
            if app.get("print")=="1":
                i=Result("Le module print est installé",rt="stdout")
                i.print()
            else:
                i=Result("Le module print n'est pas installé",rt="stdout")
                i.print()
            if app.get("maths")=="1":
                i=Result("Le module maths est installé",rt="stdout")
                i.print()
            else:
                i=Result("Le module maths n'est pas installé",rt="stdout")
                i.print()
            if app.get("download")=="1":
                i=Result("Le module download est installé",rt="stdout")
                i.print()
            else:
                i=Result("Le module download n'est pas installé",rt="stdout")
                i.print()
            if app.get("prompt")=="1":
                i=Result("Le module prompt est installé",rt="stdout")
                i.print()
            else:
                i=Result("Le module prompt n'est pas installé",rt="stdout")
                i.print()
#################################
#Clear
#################################
        elif rep=="clear":
            cmdf.clear()
#################################
#log out : déconnexion
#################################
        elif rep=="unlog":
            a=1
            return
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
                    print("app="+str(app)+"")
                    print("adresse='"+adresse+"'")
                    print("version="+version+"")
                    print("godmode1='"+godmode1+"'")
                    print("adresseuser='"+adresseuser+"'")
                if godmode1=="sys.store.install.vanish_loading":
                    print("Cette fonction permet de masquer le chargement lors de l'installation d'un module")
                    input("Taper entrer pour exécuter")
                    vanish_loading="Entrer votre choix (valeur actuelle : "+str(charginstall)+") : "
                    godmode2=input(vanish_loading)
                    if int(godmode2)==1 or int(godmode2)==0 :
                        charginstall=int(godmode2)
                        commandsql="UPDATE settings SET loading_install="+str(charginstall)+" WHERE nom='"+repname+"';"
                        cur.execute(commandsql)
                        connsql.commit()
                    else:
                        print("La valeur entrée n'est pas correcte")
                if godmode1=="sys.protocol.list":
                    print("Cette fonction permet de voir quel protocole système fait quelle action")
                    input("Taper entrer pour exécuter")
                    print("login() - protocole qui demande le mot de passe et lance le protocole cmd()")
                    print("cmd() - protocole qui gère les interactions avec l'utilisateur")
                    print("appinitext() - protocole qui récupère les modules installés ou non")
                    print("charg(chrag1=0.1,t=colored(\"Démarrage du système...\",\"blue\",attrs=[\"bold\"])) - protocole qui permet un chargement visuel")
                    print("clear() - protocole qui efface l'invite de commande")
                if godmode1=="sys.protocol.execute":
                    print("Cette fonction éxécute le protocole demandé (elle positionne automatiquement les arguments)")
                    input("Taper entrer pour exécuter")
                    godmode2=input("Quel protocole voulez vous éxécuter ? : ")
                    if godmode2=="appinitext":
                        app=appinitext(repname)
                    if godmode2=="cmd":
                        cmd(admin,charginstall,displaysplit,logserver,repname,mdpt,adresseuser)
                    if godmode2=="login":
                        login()
                    if godmode2=="clear":
                        cmdf.clear()
                if godmode1=="sys.protocol.cmd.display_split":
                    print("Cette fonction permet d'afficher le split de la variable rep lors du traitement de la commande")
                    input("Taper entrer pour exécuter")
                    display_split="Entrer votre choix (valeur actuelle : "+str(displaysplit)+") : "
                    godmode3=input(display_split)
                    if int(godmode3)==1 or int(godmode3)==0 :
                        displaysplit=int(godmode3)
                        commandsql="UPDATE settings SET display_split="+str(charginstall)+" WHERE nom='"+repname+"';"
                        cur.execute(commandsql)
                        connsql.commit()
                    else:
                        print("La valeur entrée n'est pas correcte")
                if godmode1=="sys.report":
                    print("Cette fonction permet d'activer/désactiver l'enregistrement des commandes sur le serveur de support")
                    input("Taper entrer pour exécuter")
                    report="Entrer votre choix (valeur actuelle : "+str(logserver)+") : "
                    godmode4=input(report)
                    if int(godmode4)==1 or int(godmode4)==0 :
                        logserver=int(godmode4)
                        commandsql="UPDATE settings SET log_server="+str(logserver)+" WHERE nom='"+repname+"';"
                        cur.execute(commandsql)
                        connsql.commit()
                    else:
                        print("La valeur entrée n'est pas correcte")
                if godmode1=="sys.class.list":
                    print("Cette fonction fait la liste des classes systèmes")
                    input("Taper entrer pour exécuter")
                    print("Result() - permet l'affichage des résultats / erreurs des différentes commandes")
            else:
                Result.error("godmode","Vous devez être connecté en tant qu'administrateur pour utiliser le godmode")
###############################
#Module                       #
###############################
        elif rep.startswith("random"):
            if app.get("random")=="1":
                module.random.execute(displaysplit,rep)
            else:
                i=Result(module="module",text="Ce module n'est pas installé ou n'est pas bien formulé",rt="error")
                i.print()
        elif rep.startswith("time"):
            if app.get("time")=="1":
                module.time.execute(displaysplit,rep)
            else:
                i=Result(module="module",text="Ce module n'est pas installé ou n'est pas bien formulé",rt="error")
                i.print()
        elif rep.startswith("music"):
            if app.get("music")=="1":
                module.music.execute(displaysplit,rep,adresse)
            else:
                i=Result(module="module",text="Ce module n'est pas installé ou n'est pas bien formulé",rt="error")
                i.print()
        elif rep=="uuid":
            if app.get("uuid")=="1":
                module.uuid.execute()
            else:
                i=Result(module="module",text="Ce module n'est pas installé ou n'est pas bien formulé",rt="error")
                i.print()
        elif rep.startswith("image"):
            if app.get("image")=="1":
                module.image.execute(displaysplit,rep,adresse)
            else:
                i=Result(module="module",text="Ce module n'est pas installé ou n'est pas bien formulé",rt="error")
                i.print()
        elif rep.startswith("browser"):
            if app.get("browser")=="1":
                module.browser.execute(displaysplit,rep)
            else:
                i=Result(module="module",text="Ce module n'est pas installé ou n'est pas bien formulé",rt="error")
                i.print()
        elif rep.startswith("print"):
            if app.get("print")=="1":
                module.print.execute(displaysplit,rep)
            else:
                i=Result(module="module",text="Ce module n'est pas installé ou n'est pas bien formulé",rt="error")
                i.print()
        elif rep.startswith("maths"):
            if app.get("maths")=="1":
                module.maths.execute(displaysplit,rep)
            else:
                i=Result(module="module",text="Ce module n'est pas installé ou n'est pas bien formulé",rt="error")
                i.print()
        elif rep.startswith("download"):
            if app.get("download")=="1":
                module.download.execute(adresseuser,displaysplit,rep)
            else:
                i=Result(module="module",text="Ce module n'est pas installé ou n'est pas bien formulé",rt="error")
                i.print()
        elif rep.startswith("prompt"):
            if app.get("prompt")=="1":
                module.prompt.execute(displaysplit,rep)
            else:
                i=Result(module="module",text="Ce module n'est pas installé ou n'est pas bien formulé",rt="error")
                i.print() 
#################################
#Commande n'existe pas
#################################
        else:
            if not rep=="":
                error="cette commande n'existe pas : essayer help"
                i=Result(text=error,rt="error",module="system")
                i.print()
#################################
#Login
#################################
def login():
    global adresse
    adresse=os.path.realpath(__file__)
    adresse=os.path.dirname(adresse)
    valida="no"
    repsql=[]
    cmdf.clear()
    print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
    while True:
        if len(os.listdir(adresse+"/user"))==0:
            compte=input("Vouler vous vous connecter (1), créer un compte (2) ou annuler (3) ? : ")
            os.system('clear')
            print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
            if compte=="1":
                valida="no"
                while valida!="ok":
                    repsql=[]
                    repname=input("Taper votre nom d'utilisateur : ")
                    repmdp=input("Taper votre mot de passe : ")
                    cur.execute("SELECT * FROM all_users WHERE all_users.nom='"+repname+"';")
                    repsql=cur.fetchall()
                    if repsql==[]:
                        os.system('clear')
                        print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                        print(colored("Le compte n'existe pas","red",attrs=["bold"]))
                    else:
                        repsql=list(repsql[0])
                        if repmdp==repsql[0]:
                            os.makedirs("user/"+repname+"/image")
                            os.makedirs("user/"+repname+"/music")
                            os.makedirs("user/"+repname+"/save_module")
                            os.makedirs("user/"+repname+"/download")
                            app=appinitext(repname)
                            adresse=adresse+"/user/"+repname
                            adresseuser=adresse
                            valida="ok"
                        else:
                            os.system('clear')
                            print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                            print(colored("Le mot de passe n'est pas correct","red",attrs=["bold"]))
                mdpt=repsql[0]
                admin=repsql[2]
                displaysplit=repsql[4]
                logserver=repsql[3]
                charginstall=repsql[5]
                cmdf.clear()
                print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                print("""Taper "help" pour plus d'information""")
                cmd(admin,charginstall,displaysplit,logserver,repname,mdpt,adresseuser)
                return
            elif compte=="2":
                valida="no"
                while valida!="ok":
                    repname=input("Entrer un nom d'utilisateur (pas plus de 50 caractères) : ")
                    repmdp=input("Entrer un mot de passe (pas plus de 50 caractères) : ")
                    if not len(repname)>=50 and not len(repmdp)>=50:
                        if repmdp=="shutdown":
                            os.system('clear')
                            print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                            print(colored("Le mot de passe ne peut pas être 'shutdown'","red",attrs=["bold"]))
                        else:
                            try:
                                commandsql="INSERT INTO utilisateur VALUES ('"+str(repname)+"','"+str(repmdp)+"',0);"
                                cur.execute(commandsql)
                                connsql.commit()
                                commandsql="INSERT INTO settings VALUES ('"+str(repname)+"',0,1,1);"
                                cur.execute(commandsql)
                                connsql.commit()
                                os.makedirs("user/"+repname+"/image")
                                os.makedirs("user/"+repname+"/music")
                                os.makedirs("user/"+repname+"/save_module")
                                os.makedirs("user/"+repname+"/download")
                                app=appinitext(repname)
                                adresse=adresse+"/user/"+repname
                                adresseuser=adresse
                                valida="ok"
                            except psycopg2.errors.UniqueViolation:
                                os.system('clear')
                                print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                                print(colored("Le nom d'utilisateur est déja pris","red",attrs=["bold"]))
                    else:
                        os.system('clear')
                        print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                        print(colored("Une valeur entrée n'est pas valide","red",attrs=["bold"]))
                mdpt=repmdp
                admin=0
                displaysplit=0
                logserver=1
                charginstall=1
                cmdf.clear()
                print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                print("""Taper "help" pour plus d'information""")
                cmd(admin,charginstall,displaysplit,logserver,repname,mdpt,adresseuser)
                return
            elif compte=="3":
                break
            else:
                os.system('clear')
                print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                print(colored("La valeur entrée n'est pas valide","red",attrs=["bold"]))
        else:
            while True:
                print("Selectionner une option ou taper le nom d'un compte existant sur la machine : \n 1 - Ajouter un compte existant\n 2 - Créer un compte\n 3 - Eteindre")
                fichiers=os.listdir("user")
                longueur=len(os.listdir("user"))
                for element in range(longueur):
                    print(" "+fichiers[element]+" - se connecter avec ce compte")
                rep=input("Votre choix : ")
                cmdf.clear()
                print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                if rep=="1":
                    valida="no"
                    while valida!="ok":
                        repsql=[]
                        repname=input("Taper votre nom d'utilisateur : ")
                        repmdp=input("Taper votre mot de passe : ")
                        cur.execute("SELECT * FROM all_users WHERE all_users.nom='"+repname+"';")
                        repsql=cur.fetchall()
                        if repsql==[]:
                            os.system('clear')
                            print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                            print(colored("Le compte n'existe pas","red",attrs=["bold"]))
                        else:
                            repsql=list(repsql[0])
                            if repmdp==repsql[0]:
                                try:
                                    os.makedirs("user/"+repname+"/image")
                                    os.makedirs("user/"+repname+"/music")
                                    os.makedirs("user/"+repname+"/save_module")
                                    os.makedirs("user/"+repname+"/download")
                                    app=appinitext(repname)
                                    adresse=adresse+"/user/"+repname
                                    adresseuser=adresse
                                    mdpt=repsql[0]
                                    valida="ok"
                                except FileExistsError:
                                    os.system('clear')
                                    print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                                    print(colored("Le compte est déja ajouté","red",attrs=["bold"]))
                            else:
                                os.system('clear')
                                print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                                print(colored("Le mot de passe n'est pas correct","red",attrs=["bold"]))
                elif rep=="2":
                    valida="no"
                    while valida!="ok":
                        repname=input("Entrer un nom d'utilisateur (pas plus de 50 caractères) : ")
                        repmdp=input("Entrer un mot de passe (pas plus de 50 caractères) : ")
                        if not len(repname)>=50 and not len(repmdp)>=50:
                            if repmdp=="shutdown":
                                os.system('clear')
                                print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                                print(colored("Le mot de passe ne peut pas être 'shutdown'","red",attrs=["bold"]))
                            else:
                                try:
                                    commandsql="INSERT INTO utilisateur VALUES ('"+str(repname)+"','"+str(repmdp)+"',0);"
                                    cur.execute(commandsql)
                                    connsql.commit()
                                    commandsql="INSERT INTO settings VALUES ('"+str(repname)+"',0,1,1);"
                                    cur.execute(commandsql)
                                    connsql.commit()
                                    os.makedirs("user/"+repname+"/image")
                                    os.makedirs("user/"+repname+"/music")
                                    os.makedirs("user/"+repname+"/save_module")
                                    os.makedirs("user/"+repname+"/download")
                                    app=appinitext(repname)
                                    adresse=adresse+"/user/"+repname
                                    adresseuser=adresse
                                    mdpt=repmdp
                                    cur.execute("SELECT * FROM all_users WHERE all_users.nom='"+repname+"';")
                                    repsql=cur.fetchall()
                                    repsql=list(repsql[0])
                                    valida="ok"
                                except psycopg2.errors.UniqueViolation:
                                    os.system('clear')
                                    print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                                    print(colored("Le nom d'utilisateur est déja pris","red",attrs=["bold"]))
                        else:
                            os.system('clear')
                            print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                            print(colored("Une valeur entrée n'est pas valide","red",attrs=["bold"]))
                elif rep=="3":
                    return
                elif rep in fichiers:
                    valida="no"
                    while valida!="ok":
                        repsql=[]
                        repname=rep
                        print(colored("Taper shutdown pour éteindre"))
                        repmdp=input("Taper votre mot de passe : ")
                        if not repmdp=="shutdown":
                            cur.execute("SELECT * FROM all_users WHERE all_users.nom='"+repname+"';")
                            repsql=cur.fetchall()
                            repsql=list(repsql[0])
                            if repmdp==repsql[0]:
                                mdpt=repmdp
                                adresse=adresse+"/user/"+repname
                                adresseuser=adresse
                                app=appinitext(repname)
                                valida="ok"
                                break
                            else:
                                os.system('clear')
                                print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                                print(colored("Le mot de passe n'est pas correct","red",attrs=["bold"]))
                        else:
                            return
                else:
                    os.system('clear')
                    print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                    print(colored("La valeur entrée n'est pas valide","red",attrs=["bold"]))
                if valida=="ok":
                    admin=repsql[2]
                    displaysplit=repsql[4]
                    logserver=repsql[3]
                    charginstall=repsql[5]
                    cmdf.clear()
                    print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                    print("""Taper "help" pour plus d'information""")
                    a=0
                    cmd(admin,charginstall,displaysplit,logserver,repname,mdpt,adresseuser)
                    return
while True :
    login()
    if a==1:
        a=0
        adresse=os.path.realpath(__file__)
        adresse=os.path.dirname(adresse)
        print(adresse)
        login()
    else:
        break
connect.quit()
cur.close()
connsql.close()
cmdf.clear()