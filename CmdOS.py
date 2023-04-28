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
from termcolor import colored
import requests as req
import cmd_fonction
from datetime import datetime
from ftplib import FTP
import ftplib
import subprocess
import sys
import webbrowser
import secure_id
import indecode
import psycopg2
import shutil
import platform
cmd_fonction.clear()
#########################################################################
#Admin, commande
#########################################################################
if (len(sys.argv)==2 and sys.argv[1]=="admin") or (len(sys.argv)==1 and sys.argv[0]=="admin"):
    admin=1
else:
    admin=0
a=0
help="Voici la liste des commandes de CmdOS :"+"\nhelp - Afficher la liste des commandes :\n   help <commande>"+"\ninfo - Afficher les infos sur un programme\n   utliser sys / system pour voir la version du système\n   utiliser 'info app (fichier python)' pour afficher les caractéristiques d'un fichier python du dossier app"+"\nstore - Affiche les différentes applications installables : \n   install - installer un module \n   uninstall - desinstaller un module""\n   list - affiche les différents modules installés"+"\ncd - changer de dossier :\n   cd <chemin absolu>\n   cd <dossier à ouvrir>\n   cd .. : ouvre le dossier parent"+"\ndir - permet de voir les fichiers/dossiers"+"\nuser - Voir vos identifiants :\n   name - modifie votre nom d'utilisateur\n   password - modifie votre mot de passe\n   disconnect - déconnecte votre compte de l'appareil\n   delete - supprime totalement votre compte\n   reset - change votre clé de cryptage"+"\nren - renomer un fichier"+"\ndel - supprimer un fichier / dossier"+"\nupdate :""\n   upgrade - mettre à jour le système en téléchargant la dernière version""\n   check - vérifier si une nouvelle mise à jour est disponible"+"\nadmin - active ou désactive le mode admin"+"\nlog - affiche l'état des logs (il faut être connecté en tant qu'administrateur pour utiliser cette commande)""\n   enable - active les logs""\n   disable - désactive les logs""\n   delete - supprime les logs"+"\ndetail - affiche les propriétés d'un fichier ou dossier sous forme de os.stat_result"+"\nshell (version raccourci : sh) - ouvre le cmd"+"\nexecute - permet d'éxécuter des fonctions exterieures au système"+"\nunlog - déconnecte l'utilisateur"+"\nmkdir - crée un dossier"
com={
     "help":"help - Afficher la liste des commandes :\n   help <commande>",
     "info":"info - Afficher les infos sur un programme\n   utliser sys / system pour voir la version du système\n   utiliser 'info app (fichier python)' pour afficher les caractéristiques d'un fichier python du dossier app",
     "store":"store - Affiche les différentes applications installables : \n   install - installer un module \n   uninstall - desinstaller un module""\n   list - affiche les différents modules installés",
     "cd":"cd - changer de dossier :\n   cd <chemin absolu>\n   cd <dossier à ouvrir>\n   cd .. : ouvre le dossier parent",
     "dir":"dir - permet de voir les fichiers/dossiers",
     "user":"user - Voir vos identifiants :\n   name - modifie votre nom d'utilisateur\n   password - modifie votre mot de passe\n   disconnect - déconnecte votre compte de l'appareil\n   delete - supprime totalement votre compte\n   reset - change votre clé de cryptage",
     "ren":"ren - renomer un fichier",
     "del":"del - supprimer un fichier / dossier",
     "update":"update :""\n   upgrade - mettre à jour le système en téléchargant la dernière version""\n   check - vérifier si une nouvelle mise à jour est disponible",
     "admin":"admin - active ou désactive le mode admin",
     "log":"log - affiche l'état des logs (il faut être connecté en tant qu'administrateur pour utiliser cette commande)""\n   enable - active les logs""\n   disable - désactive les logs""\n   delete - supprime les logs",
     "detail":"detail - affiche les propriétés d'un fichier ou dossier sous forme de os.stat_result",
     "shell":"shell (version raccourci : sh) - ouvre le cmd",
     "execute":"execute - permet d'éxécuter des fonctions exterieures au système",
     "unlog":"unlog - déconnecte l'utilisateur",
     "mkdir":"mkdir - crée un dossier"
     }
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
#Import app depuis txt et adresseapp
############################################
adresseapp=os.path.realpath(__file__)
adresseapp=os.path.dirname(adresseapp)
def appinitext(repname):
    global adresseapp
    if not os.path.exists(adresseapp+"/user/"+repname+"/save_module/random.txt"):
        randomtext=open(adresseapp+"/user/"+repname+"/save_module/random.txt","w")
        randomtext.write(app["random"])
        randomtext.close()
    else:
        randomtext=open(adresseapp+"/user/"+repname+"/save_module/random.txt",'r')
        data=randomtext.readlines()
        app.update({"random":str(data[0])})
        randomtext.close()
        if data[0]=="1":
            import module.random
    if not os.path.exists(adresseapp+"/user/"+repname+"/save_module/time.txt"):
        timetext=open(adresseapp+"/user/"+repname+"/save_module/time.txt","w")
        timetext.write(app["time"])
        timetext.close()
    else:
        timetext=open(adresseapp+"/user/"+repname+"/save_module/time.txt",'r')
        data=timetext.readlines()
        app.update({"time":str(data[0])})
        timetext.close()
        if data[0]=="1":
            import module.time
    if not os.path.exists(adresseapp+"/user/"+repname+"/save_module/music.txt"):
        musictext=open(adresseapp+"/user/"+repname+"/save_module/music.txt","w")
        musictext.write(app["music"])
        musictext.close()
    else:
        musictext=open(adresseapp+"/user/"+repname+"/save_module/music.txt",'r')
        data=musictext.readlines()
        app.update({"music":str(data[0])})
        musictext.close()
        if data[0]=="1":
            import module.music
    if not os.path.exists(adresseapp+"/user/"+repname+"/save_module/uuid.txt"):
        uuidtext=open(adresseapp+"/user/"+repname+"/save_module/uuid.txt","w")
        uuidtext.write(app["uuid"])
        uuidtext.close()
    else:
        uuidtext=open(adresseapp+"/user/"+repname+"/save_module/uuid.txt",'r')
        data=uuidtext.readlines()
        app.update({"uuid":str(data[0])})
        uuidtext.close()
        if data[0]=="1":
            import module.uuid
    if not os.path.exists(adresseapp+"/user/"+repname+"/save_module/image.txt"):
        imagetext=open(adresseapp+"/user/"+repname+"/save_module/image.txt","w")
        imagetext.write(app["image"])
        imagetext.close()
    else:
        imagetext=open(adresseapp+"/user/"+repname+"/save_module/image.txt",'r')
        data=imagetext.readlines()
        app.update({"image":str(data[0])})
        imagetext.close()
        if data[0]=="1":
            import module.image
    if not os.path.exists(adresseapp+"/user/"+repname+"/save_module/browser.txt"):
        browsertext=open(adresseapp+"/user/"+repname+"/save_module/browser.txt","w")
        browsertext.write(app["browser"])
        browsertext.close()
    else:
        browsertext=open(adresseapp+"/user/"+repname+"/save_module/browser.txt",'r')
        data=browsertext.readlines()
        app.update({"browser":str(data[0])})
        browsertext.close()
        if data[0]=="1":
            import module.browser
    if not os.path.exists(adresseapp+"/user/"+repname+"/save_module/print.txt"):
        printtext=open(adresseapp+"/user/"+repname+"/save_module/print.txt","w")
        printtext.write(app["print"])
        printtext.close()
    else:
        printtext=open(adresseapp+"/user/"+repname+"/save_module/print.txt",'r')
        data=printtext.readlines()
        app.update({"print":str(data[0])})
        printtext.close()
        if data[0]=="1":
            import module.print
    if not os.path.exists(adresseapp+"/user/"+repname+"/save_module/maths.txt"):
        mathstext=open(adresseapp+"/user/"+repname+"/save_module/maths.txt","w")
        mathstext.write(app["maths"])
        mathstext.close()
    else:
        mathstext=open(adresseapp+"/user/"+repname+"/save_module/maths.txt",'r')
        data=mathstext.readlines()
        app.update({"maths":str(data[0])})
        mathstext.close()
        if data[0]=="1":
            import module.maths
    if not os.path.exists(adresseapp+"/user/"+repname+"/save_module/download.txt"):
        downloadtext=open(adresseapp+"/user/"+repname+"/save_module/download.txt","w")
        downloadtext.write(app["download"])
        downloadtext.close()
    else:
        downloadtext=open(adresseapp+"/user/"+repname+"/save_module/download.txt",'r')
        data=downloadtext.readlines()
        app.update({"download":str(data[0])})
        downloadtext.close()
        if data[0]=="1":
            import module.download
    if not os.path.exists(adresseapp+"/user/"+repname+"/save_module/prompt.txt"):
        prompttext=open(adresseapp+"/user/"+repname+"/save_module/prompt.txt","w")
        prompttext.write(app["prompt"])
        prompttext.close()
    else:
        prompttext=open(adresseapp+"/user/"+repname+"/save_module/prompt.txt",'r')
        data=prompttext.readlines()
        app.update({"prompt":str(data[0])})
        prompttext.close()
        if data[0]=="1":
            import module.prompt
    return app
############################################
#Info
############################################
info={"sys":"CmdOS v2.10 - Basé en Python",
      "system":"CmdOS v2.10 - Basé en Python",
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
if not(os.path.exists(adresse+"/README.md") and os.path.exists(adresse+"/__pycache__") and os.path.exists(adresse+"/module") and os.path.exists(adresse+"/app") and os.path.exists(adresse+"/user") and os.path.exists(adresse+"/logs")):
    print(colored("Le système ne peut pas fonctionner dans son intégrité car certain dosssier/fichier ne sont pas présents.\nVeulliez vous assurez que les dossier suivant existe:  __pycache__, app, user, module, logs et README.md.","red",attrs=["bold"]))
    quit()
############################################
#Connexion
############################################
print(colored("""CmdOS v2.10""","green",attrs=["bold"])) 
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
version="2.10"
invit=0
##########################
#Fonction Cmd
##########################
def cmd(admin,charginstall,displaysplit,logserver,repname,mdpt,adresseuser,key,log,invit=0):
#################################
#Variable, module
#################################
    global adresse,app,mdptext,repmdp,connect,version,a,adresseapp
    store="Bienvenue dans le store de CmdOS, voici les modules disponibles :"+"\nrandom - générer un nombre aléatoire"+"\ntime - attendre un temps"+"\nmusic - permet de jouer un son"+"\nuuid - générer des identifiants aléatoire"+"\nimage - permet d'afficher une image"+"\nbrowser - permet d'afficher une page web"+"\nprint - permet d'afficher du texte en couleur dans la console"+"\ndownload - permet de télécharger une page web"+"\nprompt - permet d'éxécuter des commandes de l'invite de commande"+"\nPour installer un module, faites <<store install>> suivie du nom du module"+"\nPour desinstaller un module, faites <<store uninstall>> suivie du nom du module"+"\nPour voir la liste des modules installés faites <<store list>>"
    while True:
        if invit==0:
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
            demande=colored(repname,"green",attrs=["bold"])+colored("@","green",attrs=["bold"])+colored(platform.uname().node+"."+platform.uname().system,"cyan",attrs=["bold"])+":"+colored(adresse,"blue",attrs=["bold"])+" >>> "
        else:
            demande=colored(repname,"green",attrs=["bold"])+colored("(admin)","red",attrs=["bold"])+colored("@","green",attrs=["bold"])+colored(platform.uname().node+"."+platform.uname().system,"cyan",attrs=["bold"])+":"+colored(adresse,"blue",attrs=["bold"])+" >>> "
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
                id2=str(secure_id.sid2())
                id=id2+"-"+repname
                if logserver==1:
                    contenttxt=open(adresseuser+"/content.txt","w")
                    contenttxt.write(indecode.code(repname+"(admin)@"+platform.uname().node+"."+platform.uname().system+" "+heure+" "+version+" "+rep,key))
                    contenttxt.close()
                    contenttxt=open(adresseuser+"/content.txt","rb")
                    connect.storbinary("STOR "+id,contenttxt)
                    contenttxt.close()
                if log==1:
                    logadd=id2+" "+repname+"(admin)@"+platform.uname().node+"."+platform.uname().system+" "+heure+" "+version+" "+rep
                    logtxt=open(adresseapp+"/logs/"+repname+".txt","a")
                    logtxt.write(logadd+"\n")
                    logtxt.close()
            else:
                heure=str(datetime.now())
                id2=str(secure_id.sid2())
                id=id2+"-"+repname
                if logserver==1:
                    contenttxt=open(adresseuser+"/content.txt","w")
                    contenttxt.write(indecode.code(repname+"@"+platform.uname().node+"."+platform.uname().system+" "+heure+" "+version+" "+rep,key))
                    contenttxt.close()
                    contenttxt=open(adresseuser+"/content.txt","rb")
                    connect.storbinary("STOR "+id,contenttxt)
                    contenttxt.close()
                if log==1:
                    logadd=id2+" "+repname+"@"+platform.uname().node+"."+platform.uname().system+" "+heure+" "+version+" "+rep
                    logtxt=open(adresseapp+"/logs/"+repname+".txt","a")
                    logtxt.write(logadd+"\n")
                    logtxt.close()
        except ftplib.error_temp:
            host="ftp-cmdos.alwaysdata.net"
            user="cmdos"
            password="CmdOS2008)"
            connect=FTP(host,user,password)
            connect.sendcmd('CWD www')
            connect.sendcmd("CWD command")
        except:
            pass
        if rep=="help":
            i=Result(text=help,rt="stdout")
            i.print()
        elif rep.startswith("help "):
            aide=rep[5::]
            if aide in com:
                print(com[aide])
            else:
                i=Result("commande",rt="notfound",object=aide,module="help")
                i.print()
#################################
#Store
#################################
        elif rep=="store":
            if invit==0:
                i=Result(store,rt="stdout")
                i.print()
            else:
                i=Result(text="Le mode invité désactive cette commande",rt="error",module="system")
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
#Create dir
#################################
        elif rep.startswith("mkdir"):
            mkdir=rep.split()
            if displaysplit==1:
                Result.split()
            if len(mkdir)==2:
                namedir=mkdir[1]
                try:
                    os.path.normpath(namedir)
                    os.makedirs(adresse+"/"+namedir)
                except:
                    i=Result(module="mkdir",text="Le dossier existe déja ou contient des caractères interdits tel que : '/'",rt="error")
                    i.print()   
            else:
                i=Result(module="mkdir",text="La commande est mal formulée",rt="error")
                i.print()   
#################################
#Admin
#################################
        elif rep.startswith("admin"):
            if invit==0:
                admin1=rep.split()
                if displaysplit==1:
                    Result.split()
                if len(admin1)==2 and cmd_fonction.connect()==True:
                    if admin1[1]=="on":
                        if admin==0:
                            print("Vous êtes sur le point de passer en mode admin.\n\nEn tapant votre mot de passe, vous prenez conscience que :\n1)Vous vous engagez à ne pas abusez des pouvoirs qu'il vous confère\n2)Un grand pouvoir implique de grandes responsabilités\n3)Vous serez admin sur tous les appareils où vous êtes connectés\n")
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
                    i=Result("La commande est mal formulée ou vous n'êtes pas connecté à internet","error",module="admin")
                    i.print()
            else:
                i=Result(text="Le mode invité désactive cette commande",rt="error",module="system")
                i.print()
#################################
#Supprimer
#################################
        elif rep.startswith("del"):
            if invit==0:
                supr=rep.split()
                if displaysplit==1:
                    Result.split()
                if len(supr)==2:
                    fichiers = os.listdir(adresse)
                    if supr[1] in fichiers:
                        del_1=adresse+"/"+supr[1]
                        try:
                            if not os.path.isdir(del_1):
                                os.remove(del_1)
                            elif os.path.isdir(del_1) and os.listdir(del_1)==[]:
                                os.rmdir(del_1)
                            elif os.path.isdir(del_1) and not os.listdir(del_1)==[]:
                                shutil.rmtree(del_1)
                            else:
                                i=Result(text="Une erreur est survenue, vérifier que vous avez les permissions pour supprimer ce ficher",rt="error",module="system")
                                i.print()
                        except:
                            i=Result(text="Une erreur est survenue, vérifier que vous avez les permissions pour supprimer ce ficher",rt="error",module="system")
                            i.print()
                    else:
                        i=Result(module="del",object=supr[1],rt="notfound",text=None)
                        i.print()
                else:
                    i=Result("La commande est mal formulée","error",module="del")
                    i.print()
            else:
                i=Result(text="Le mode invité désactive cette commande",rt="error",module="system")
                i.print()
#################################
#Renommer
#################################
        elif rep.startswith("ren"):
            if invit==0:
                ren=rep[4::]
                fichiers = os.listdir(adresse)
                if ren in fichiers:
                    ren2=adresse+"/"+ren
                    ren3=input("Nouveau nom : ")
                    try:
                        os.rename(ren2, ren3)
                    except:
                        i=Result(text="Une erreur est survenue, vérifier que vous avez les permissions pour renommer ce ficher",rt="error",module="system")
                        i.print()
                else:
                    i=Result(module="ren",object=ren,rt="notfound",text=None)
                    i.print()
            else:
                i=Result(text="Le mode invité désactive cette commande",rt="error",module="system")
                i.print()
#################################
#Cd : change directory
#################################
        elif rep.startswith("cd"):
            cd=rep.split()
            if displaysplit==1:
                Result.split()
            if len(cd)>=2:
                if rep[3::]=="..":
                    adresse=os.path.dirname(adresse)
                elif rep[3::]=="~":
                    if invit==0:
                        adresse=adresseuser
                    else:
                        i=Result(text="Le mode invité désactive cette commande",rt="error",module="system")
                        i.print()
                elif os.path.isabs(os.path.join(adresse,rep[3::])) or os.path.isabs(rep[3::]):
                    if rep[3::].startswith("/") and os.path.exists(rep[3::]):
                        adresse=rep[3::]
                    elif os.path.exists(os.path.join(adresse,rep[3::])):
                        adresse=os.path.join(adresse,rep[3::])
                    else:
                        i=Result("Le dossier n'est pas valide","error",module="cd")
                        i.print()                        
                else:
                    i=Result("Le dossier n'est pas valide","error",module="cd")
                    i.print()
            else:
                i=Result("La commande est mal formulée","error",module="cd")
                i.print()
#################################
#Dir : directory
#################################
        elif rep=="dir":
            try:
                fichiers = os.listdir(adresse)
                longueur=len(fichiers)
                i=Result("Voici les fichiers/dossiers dans ce dossier :",rt="stdout")
                i.print()
                for element in range(longueur):
                    i=Result(" "+fichiers[element],rt="stdout")
                    i.print()
            except:
                i=Result(text="Une erreur est survenue, vérifier que vous avez les permissions pour voir le contenu de ce dossier",rt="error",module="system")
                i.print()
#################################
#Logs
#################################
        elif rep.startswith("log"):
            if invit==0:
                if admin==1:
                    log1=rep.split()
                    if displaysplit==1:
                        Result.split()
                    if len(log1)==2 and type(log1[1])==str:
                        if log1[1]=="enable":
                            logtxt=open("user/"+repname+"/log.txt","w")
                            logtxt.write("1")
                            logtxt.close()
                            log=1
                            i=Result("Les logs sont activés sur votre compte local","important")
                            i.print()
                        elif log1[1]=="disable":
                            logtxt=open("user/"+repname+"/log.txt","w")
                            logtxt.write("0")
                            logtxt.close()
                            log=0
                            i=Result("Les logs sont désactivés sur votre compte local","important")
                            i.print()
                        elif log1[1]=="delete":
                            logtxt=open("logs/"+repname+".txt","w")
                            logtxt.write("")
                            logtxt.close()
                            i=Result("Les logs ont bien été supprimé","important")
                            i.print()
                        else:
                            i=Result("La commande est mal formulée","error",module="log")
                            i.print()
                    elif len(log1)==1:
                        if log==1:
                            i=Result("Les logs sont activés sur votre compte local","important")
                            i.print()
                        else:
                            i=Result("Les logs sont déactivés sur votre compte local","important")
                            i.print()
                    else:
                        i=Result("La commande est mal formulée","error",module="log")
                        i.print()
                else:
                    i=Result("Vous devez être connecté en tant qu'administrateur pour utiliser cette commande","error",module="log")
                    i.print()
            else:
                i=Result(text="Le mode invité désactive cette commande",rt="error",module="system")
                i.print()
#################################
#Store install
#################################
        elif rep.startswith("store install "):
            if invit==0:
                install=rep[14::]
                if install in app: 
                    app.update({install:"1"})
                    if charginstall==1:
                        cmd_fonction.charg(0.3,colored("Installation du module...","blue",attrs=["bold"]))
                        print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                        print("""Taper "help" pour plus d'information""")
                    install2=colored("Le module ","blue",attrs=["bold"])+colored(install,"blue",attrs=["bold","underline"])+colored(" a bien été installé","blue",attrs=["bold"])
                    i=Result(install2,"stdout")
                    i.print()
                    if install=="random":
                        import module.random
                        appt=open(adresseapp+"/user/"+repname+"/save_module/random.txt","w")
                        appt.write(app.get("random"))
                        appt.close()
                    if install=="time":
                        import module.time
                        appt=open(adresseapp+"/user/"+repname+"/save_module/time.txt","w")
                        appt.write(app.get("time"))
                        appt.close()
                    if install=="music":
                        import module.music
                        appt=open(adresseapp+"/user/"+repname+"/save_module/music.txt","w")
                        appt.write(app.get("music"))
                        appt.close()
                    if install=="uuid":
                        import module.uuid
                        appt=open(adresseapp+"/user/"+repname+"/save_module/uuid.txt","w")
                        appt.write(app.get("uuid"))
                        appt.close()
                    if install=="image":
                        import module.image
                        appt=open(adresseapp+"/user/"+repname+"/save_module/image.txt","w")
                        appt.write(app.get("image"))
                        appt.close()
                    if install=="browser":
                        import module.browser
                        appt=open(adresseapp+"/user/"+repname+"/save_module/browser.txt","w")
                        appt.write(app.get("browser"))
                        appt.close()
                    if install=="print":
                        import module.print
                        appt=open(adresseapp+"/user/"+repname+"/save_module/print.txt","w")
                        appt.write(app.get("print"))
                        appt.close()
                    if install=="maths":
                        import module.maths
                        appt=open(adresseapp+"/user/"+repname+"/save_module/maths.txt","w")
                        appt.write(app.get("maths"))
                        appt.close()
                    if install=="download":
                        import module.download
                        appt=open(adresseapp+"/user/"+repname+"/save_module/download.txt","w")
                        appt.write(app.get("download"))
                        appt.close()
                    if install=="prompt":
                        import module.prompt
                        appt=open(adresseapp+"/user/"+repname+"/save_module/prompt.txt","w")
                        appt.write(app.get("prompt"))
                        appt.close()
                else:
                    i=Result(module="store",object="module",rt="notfound",text=None)
                    i.print()
            else:
                i=Result(text="Le mode invité désactive cette commande",rt="error",module="system")
                i.print()
#################################
#Execute
#################################
        elif rep.startswith("execute"):
            impor=rep.split()
            if displaysplit==1:
                Result.split()
            if len(impor)==3:
                command="""import termcolor\ntry:\n    from app."""+impor[1]+""" import *\n    """+impor[2]+"""()\nexcept ModuleNotFoundError:\n    print(termcolor.colored("L'app ou la fonction indiquée n'existe pas","yellow",attrs=["bold"]))\nexcept NameError:\n    print(termcolor.colored("L'app ou la fonction indiquée n'existe pas","yellow",attrs=["bold"]))"""
                subprocess.run([sys.executable, "-c",command])
            else:
                i=Result("La commande est mal formulée","error",module="execute")
                i.print()
#################################
#Shell
#################################
        elif rep=="shutdown" or rep=="sh" or rep=="shell":
            cmd_fonction.clear()
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
                    i=Result(module="info",object=info_command[1],rt="notfound",text=None)
                    i.print()
            else:
                i=Result("La commande est mal formulée","error",module="info")
                i.print()
#################################
#Store uninstall
#################################
        elif rep.startswith("store uninstall "):
            if invit==0:
                uninstall=rep[16::]
                if uninstall in app:
                    app.update({uninstall:"0"})
                    uninstall1=colored("Le module ","blue",attrs=["bold"])+colored(uninstall,"blue",attrs=["bold","underline"])+colored(" a bien été desinstallé","blue",attrs=["bold"])
                    i=Result(uninstall1,"stdout")
                    i.print()
                    if uninstall=="random":
                        appt=open(adresseapp+"/user/"+repname+"/save_module/random.txt","w")
                        appt.write(app.get("random"))
                        appt.close()
                    if uninstall=="time":
                        appt=open(adresseapp+"/user/"+repname+"/save_module/time.txt","w")
                        appt.write(app.get("time"))
                        appt.close()
                    if uninstall=="music":
                        appt=open(adresseapp+"/user/"+repname+"/save_module/music.txt","w")
                        appt.write(app.get("music"))
                        appt.close()
                    if uninstall=="uuid":
                        appt=open(adresseapp+"/user/"+repname+"/save_module/uuid.txt","w")
                        appt.write(app.get("uuid"))
                        appt.close()
                    if uninstall=="image":
                        appt=open(adresseapp+"/user/"+repname+"/save_module/image.txt","w")
                        appt.write(str(app.get("image")))
                        appt.close()
                    if uninstall=="browser":
                        appt=open(adresseapp+"/user/"+repname+"/save_module/browser.txt","w")
                        appt.write(str(app.get("browser")))
                        appt.close()
                    if uninstall=="print":
                        appt=open(adresseapp+"/user/"+repname+"/save_module/print.txt","w")
                        appt.write(str(app.get("print")))
                        appt.close()
                    if uninstall=="maths":
                        appt=open(adresseapp+"/user/"+repname+"/save_module/maths.txt","w")
                        appt.write(str(app.get("maths")))
                        appt.close()
                    if uninstall=="download":
                        appt=open(adresseapp+"/user/"+repname+"/save_module/download.txt","w")
                        appt.write(str(app.get("download")))
                        appt.close()
                    if uninstall=="prompt":
                        appt=open(adresseapp+"/user/"+repname+"/save_module/prompt.txt","w")
                        appt.write(str(app.get("prompt")))
                        appt.close()
                else:
                    i=Result(module="store",object="module",rt="notfound",text=None)
                    i.print()
            else:
                i=Result(text="Le mode invité désactive cette commande",rt="error",module="system")
                i.print()
#################################
#Compte modification
#################################
        elif rep.startswith("user"):
            if invit==0:
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
                        if user[1]=="name" and cmd_fonction.connect()==True:
                            answer=input("Taper votre nouveau nom d'utilisateur (pas plus de 50 caractères) : ")
                            try:
                                if not len(answer)>=50:
                                    commandsql="UPDATE utilisateur SET nom='"+str(answer)+"' WHERE nom='"+str(repname)+"';"
                                    cur.execute(commandsql)
                                    commandsql="UPDATE settings SET nom='"+str(answer)+"' WHERE nom='"+str(repname)+"';"
                                    cur.execute(commandsql)
                                    connsql.commit()
                                    os.rename(adresseapp+"/user/"+repname,adresseapp+"/user/"+answer)
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
                        elif user[1]=="password" and cmd_fonction.connect()==True:
                            answer=input("Taper votre nouveau mot de passe (pas plus de 50 caractères) : ")
                            if not len(answer)>=50:
                                commandsql="UPDATE utilisateur SET mdp='"+str(indecode.code(answer))+"' WHERE nom='"+str(repname)+"';"
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
                                os.remove("logs/"+repname+".txt")
                                a=1
                                return
                        elif user[1]=="delete"  and cmd_fonction.connect()==True:
                            answer=input("Voulez vous vraiment supprimer votre compte ? (o/n) : ")
                            if answer=="o":
                                shutil.rmtree(adresseuser)
                                commandsql="DELETE FROM utilisateur WHERE nom='"+repname+"';"
                                cur.execute(commandsql)
                                connsql.commit()
                                commandsql="DELETE FROM settings WHERE nom='"+repname+"';"
                                cur.execute(commandsql)
                                connsql.commit()
                                os.remove("logs/"+repname+".txt")
                                a=1
                                return
                        elif user[1]=="reset" and cmd_fonction.connect()==True:
                            key=indecode.generate_key()
                            commandsql="UPDATE utilisateur SET mdp='"+str(indecode.code(mdpt,key))+"',key='"+key+"' WHERE nom='"+str(repname)+"';"
                            i=Result("Votre clé de cryptage à bien été changé","stdout")
                            i.print()
                        else:
                            i=Result("La commande est mal formulée ou vous n'êtes pas connecté à internet","error",module="user")
                            i.print()
                    else:
                        i=Result("La commande est mal formulée","error",module="user")
                        i.print()
                else:
                    i=Result("La commande est mal formulée","error",module="user")
                    i.print()
            else:
                i=Result(text="Le mode invité désactive cette commande",rt="error",module="system")
                i.print()
#################################
#Update
#################################
        elif rep.startswith("update"):
            if invit==0:
                update=rep.split()
                if displaysplit==1:
                    print(update)
                if len(update)==2:    
                    if update[1]=="upgrade":
                        if cmd_fonction.connect()==True:
                            i=Result(text="Vous allez télécharger le fichier zip contenant l'assistant pour mettre à jour CmdOS",rt="important")
                            i.print()
                            webbrowser.open("https://github.com/lolo859/get-cmdos/archive/refs/heads/main.zip")
                        else:
                            i=Result("Vous devez être connecté à internet pour mettre à jour CmdOS","error",module="update")
                            i.print()
                    elif update[1]=="check" and cmd_fonction.connect()==True:
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
                            i.print()
                            versionprint="La dernière version disponible est CmdOS "+verlist[0]+"\nVous pouvez mettre a jour le système avec update upgrade"
                            i=Result(versionprint,"important")
                            i.print()
                    else:
                        i=Result("La commande est mal formulée ou vous n'êtes pas connecté à internet","error",module="update")
                        i.print()
                else:
                    i=Result("La commande est mal formulée","error",module="update")
                    i.print()
            else:
                i=Result(text="Le mode invité désactive cette commande",rt="error",module="system")
                i.print()
#################################
#Store list
#################################
        elif rep=="store list":
            if invit==0:
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
            else:
                i=Result(text="Le mode invité désactive cette commande",rt="error",module="system")
                i.print()
#################################
#Clear
#################################
        elif rep=="clear":
            cmd_fonction.clear()
            print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
            print("""Taper "help" pour plus d'information""")
#################################
#log out : déconnexion
#################################
        elif rep=="unlog":
            a=1
            return
#################################
#Godmode
#################################
        elif rep=="godmode" and invit==0:
            if admin==1 and cmd_fonction.connect()==True:
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
                    print("invit='"+str(invit)+"'")
                    print("log="+str(log)+"")
                if godmode1=="sys.cmd.store.install.vanish_loading":
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
                    print("connect() - vérifie si on est connecté à internet")
                if godmode1=="sys.protocol.execute":
                    print("Cette fonction éxécute le protocole demandé (elle positionne automatiquement les arguments)")
                    input("Taper entrer pour exécuter")
                    godmode2=input("Quel protocole voulez vous éxécuter ? : ")
                    if godmode2=="appinitext":
                        app=appinitext(repname)
                    if godmode2=="cmd":
                        cmd(admin,charginstall,displaysplit,logserver,repname,mdpt,adresseuser,key,log)
                    if godmode2=="login":
                        login()
                    if godmode2=="clear":
                        cmd_fonction.clear()
                    if godmode2=="connect":
                        cmd_fonction.connect()
                if godmode1=="sys.cmd.display_split":
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
                if godmode1=="sys.cmd.report":
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
                if godmode1=="sys.protocol.reload":
                    print("Cette fonction réimporte les différents dépendances")
                    input("Taper entrer pour exécuter")
                    reload=input("Entrer votre choix (module/cmd_fonction) : ")
                    if reload=="module":
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
                    # if reload=="cmd_fonction":
                        # import cmd_fonction
            else:
                i=Result(module="godmode",rt="error",text="Vous devez être connecté en tant qu'administrateur et à internet pour utiliser le godmode")
                i.print()
###############################
#Module                       #
###############################
        elif rep.startswith("random") and invit==0:
            if app.get("random")=="1":
                module.random.execute(displaysplit,rep)
            else:
                i=Result(module="module",text="Ce module n'est pas installé ou n'est pas bien formulé",rt="error")
                i.print()
        elif rep.startswith("time") and invit==0:
            if app.get("time")=="1":
                module.time.execute(displaysplit,rep)
            else:
                i=Result(module="module",text="Ce module n'est pas installé ou n'est pas bien formulé",rt="error")
                i.print()
        elif rep.startswith("music") and invit==0:
            if app.get("music")=="1":
                module.music.execute(displaysplit,rep,adresse)
            else:
                i=Result(module="module",text="Ce module n'est pas installé ou n'est pas bien formulé",rt="error")
                i.print()
        elif rep=="uuid" and invit==0:
            if app.get("uuid")=="1":
                module.uuid.execute()
            else:
                i=Result(module="module",text="Ce module n'est pas installé ou n'est pas bien formulé",rt="error")
                i.print()
        elif rep.startswith("image") and invit==0:
            if app.get("image")=="1":
                module.image.execute(displaysplit,rep,adresse)
            else:
                i=Result(module="module",text="Ce module n'est pas installé ou n'est pas bien formulé",rt="error")
                i.print()
        elif rep.startswith("browser") and invit==0:
            if app.get("browser")=="1":
                module.browser.execute(displaysplit,rep)
            else:
                i=Result(module="module",text="Ce module n'est pas installé ou n'est pas bien formulé",rt="error")
                i.print()
        elif rep.startswith("print") and invit==0:
            if app.get("print")=="1":
                module.print.execute(displaysplit,rep)
            else:
                i=Result(module="module",text="Ce module n'est pas installé ou n'est pas bien formulé",rt="error")
                i.print()
        elif rep.startswith("maths") and invit==0:
            if app.get("maths")=="1":
                module.maths.execute(displaysplit,rep)
            else:
                i=Result(module="module",text="Ce module n'est pas installé ou n'est pas bien formulé",rt="error")
                i.print()
        elif rep.startswith("download") and invit==0:
            if app.get("download")=="1":
                module.download.execute(adresseuser,displaysplit,rep)
            else:
                i=Result(module="module",text="Ce module n'est pas installé ou n'est pas bien formulé",rt="error")
                i.print()
        elif rep.startswith("prompt") and invit==0:
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
    cmd_fonction.clear()
    print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
    while True:
        if len(os.listdir(adresse+"/user"))==0:
            compte=input("Vouler vous vous connecter (1), créer un compte (2), activer le mode invité (3) ou annuler (4) ? : ")
            cmd_fonction.clear()
            print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
            if compte=="1":
                if cmd_fonction.connect():
                    valida="no"
                    while valida!="ok":
                        repname=input("Taper votre nom d'utilisateur : ")
                        repmdp=input("Taper votre mot de passe : ")
                        cur.execute("SELECT * FROM utilisateur WHERE nom='"+repname+"';")
                        repsqluser=cur.fetchall()
                        cur.execute("SELECT * FROM settings WHERE nom='"+repname+"';")
                        repsqlset=cur.fetchall()
                        if repsqluser==[]:
                            cmd_fonction.clear()
                            print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                            print(colored("Le compte n'existe pas","red",attrs=["bold"]))
                        else:
                            repsqluser=list(repsqluser[0])
                            repsqlset=list(repsqlset[0])
                            if repmdp==indecode.decode(repsqluser[1],repsqluser[3]):
                                os.makedirs(adresseapp+"/user/"+repname+"/image")
                                os.makedirs(adresseapp+"/user/"+repname+"/music")
                                os.makedirs(adresseapp+"/user/"+repname+"/save_module")
                                os.makedirs(adresseapp+"/user/"+repname+"/download")
                                logtxt=open(adresseapp+"/logs/"+repname+".txt","w")
                                logtxt.close()
                                logtxt=open(adresseapp+"/user/"+repname+"/log.txt","w")
                                logtxt.write("1")
                                logtxt.close()
                                app=appinitext(repname)
                                adresse=adresse+"/user/"+repname
                                adresseuser=adresse
                                valida="ok"
                            else:
                                cmd_fonction.clear()
                                print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                                print(colored("Le mot de passe n'est pas correct","red",attrs=["bold"]))
                    mdpt=indecode.decode(repsqluser[1],repsqluser[3])
                    admin=repsqluser[2]
                    displaysplit=repsqlset[1]
                    logserver=repsqlset[3]
                    charginstall=repsqlset[2]
                    key=repsqluser[3]
                    log=1
                    cmd_fonction.clear()
                    print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                    print("""Taper "help" pour plus d'information""")
                    cmd(admin,charginstall,displaysplit,logserver,repname,mdpt,adresseuser,key,log)
                    return
                else:
                    cmd_fonction.clear()
                    print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                    print(colored("Vous devez être connecté à internet pour vous connecter","red",attrs=["bold"]))
            elif compte=="2":
                if cmd_fonction.connect():
                    valida="no"
                    while valida!="ok":
                        repname=input("Entrer un nom d'utilisateur (pas plus de 50 caractères) : ")
                        repmdp=input("Entrer un mot de passe (pas plus de 50 caractères) : ")
                        if not len(repname)>=50 and not len(repmdp)>=50:
                            if repmdp=="shutdown":
                                cmd_fonction.clear()
                                print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                                print(colored("Le mot de passe ne peut pas être 'shutdown'","red",attrs=["bold"]))
                            elif repname in ["1","2","3","4"]:
                                cmd_fonction.clear()
                                print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                                print(colored("Le nom d'utilisateur ne peut pas être 1, 2, 3 ou 4","red",attrs=["bold"]))
                            else:
                                try:
                                    key=indecode.generate_key()
                                    commandsql="INSERT INTO utilisateur VALUES ('"+str(repname)+"','"+str(indecode.code(repmdp,key))+"',0,'"+key+"');"
                                    cur.execute(commandsql)
                                    connsql.commit()
                                    commandsql="INSERT INTO settings VALUES ('"+str(repname)+"',0,1,1);"
                                    cur.execute(commandsql)
                                    connsql.commit()
                                    os.makedirs(adresseapp+"/user/"+repname+"/image")
                                    os.makedirs(adresseapp+"/user/"+repname+"/music")
                                    os.makedirs(adresseapp+"/user/"+repname+"/save_module")
                                    os.makedirs(adresseapp+"/user/"+repname+"/download")
                                    logtxt=open(adresseapp+"/logs/"+repname+".txt","w")
                                    logtxt.close()
                                    logtxt=open(adresseapp+"/user/"+repname+"/log.txt","w")
                                    logtxt.write("1")
                                    logtxt.close()
                                    app=appinitext(repname)
                                    adresse=adresse+"/user/"+repname
                                    adresseuser=adresse
                                    valida="ok"
                                except psycopg2.errors.UniqueViolation:
                                    cmd_fonction.clear()
                                    print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                                    print(colored("Le nom d'utilisateur est déja pris","red",attrs=["bold"]))
                        else:
                            cmd_fonction.clear()
                            print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                            print(colored("Une valeur entrée n'est pas valide","red",attrs=["bold"]))
                    mdpt=repmdp
                    admin=0
                    displaysplit=0
                    logserver=1
                    charginstall=1
                    log=1
                    cmd_fonction.clear()
                    print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                    print("""Taper "help" pour plus d'information""")
                    cmd(admin,charginstall,displaysplit,logserver,repname,mdpt,adresseuser,key,log)
                    return
                else:
                    cmd_fonction.clear()
                    print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                    print(colored("Vous devez être connecté à internet pour vous connecter","red",attrs=["bold"]))
            elif compte=="3":
                mdpt=0
                admin=0
                displaysplit=0
                logserver=0
                charginstall=0
                invit=1
                repname="Guest"
                log=0
                adresseuser=adresse
                key=indecode.generate_key()
                cmd_fonction.clear()
                print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                print("""Taper "help" pour plus d'information""")
                cmd(admin,charginstall,displaysplit,logserver,repname,mdpt,adresseuser,key,log,invit)
                return
            elif compte=="4":
                cmd_fonction.clear()
                exit()
            else:
                cmd_fonction.clear()
                print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                print(colored("La valeur entrée n'est pas valide","red",attrs=["bold"]))
        else:
            while True:
                print("Selectionner une option ou taper le nom d'un compte existant sur la machine : \n 1 - Ajouter un compte existant\n 2 - Créer un compte\n 3 - Démarrer le mode invité\n 4 - Eteindre")
                fichiers=os.listdir(adresse+"/user")
                longueur=len(fichiers)
                for element in range(longueur):
                    print(" "+fichiers[element]+" - se connecter avec ce compte")
                rep=input("Votre choix : ")
                cmd_fonction.clear()
                print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                if rep=="1":
                    valida="no"
                    if cmd_fonction.connect():
                        while valida!="ok":
                            repname=input("Taper votre nom d'utilisateur : ")
                            repmdp=input("Taper votre mot de passe : ")
                            cur.execute("SELECT * FROM utilisateur WHERE nom='"+repname+"';")
                            repsqluser=cur.fetchall()
                            cur.execute("SELECT * FROM settings WHERE nom='"+repname+"';")
                            repsqlset=cur.fetchall()
                            if repsqluser==[]:
                                cmd_fonction.clear()
                                print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                                print(colored("Le compte n'existe pas","red",attrs=["bold"]))
                            else:
                                repsqluser=list(repsqluser[0])
                                repsqlset=list(repsqlset[0])
                                if repmdp==indecode.decode(repsqluser[1],repsqluser[3]):
                                    try:
                                        os.makedirs(adresseapp+"/user/"+repname+"/image")
                                        os.makedirs(adresseapp+"/user/"+repname+"/music")
                                        os.makedirs(adresseapp+"/user/"+repname+"/save_module")
                                        os.makedirs(adresseapp+"/user/"+repname+"/download")
                                        logtxt=open(adresseapp+"/logs/"+repname+".txt","w")
                                        logtxt.close()
                                        logtxt=open(adresseapp+"/user/"+repname+"/log.txt","w")
                                        logtxt.write("1")
                                        logtxt.close()
                                        app=appinitext(repname)
                                        adresse=adresse+"/user/"+repname
                                        adresseuser=adresse
                                        mdpt=repmdp
                                        log=1
                                        valida="ok"
                                    except FileExistsError:
                                        cmd_fonction.clear()
                                        print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                                        print(colored("Le compte est déja ajouté","red",attrs=["bold"]))
                                else:
                                    cmd_fonction.clear()
                                    print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                                    print(colored("Le mot de passe n'est pas correct","red",attrs=["bold"]))
                    else:
                        cmd_fonction.clear()
                        print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                        print(colored("Vous devez être connecté à internet pour vous connecter","red",attrs=["bold"]))
                elif rep=="2":
                    valida="no"
                    if cmd_fonction.connect():
                        while valida!="ok":
                            repname=input("Entrer un nom d'utilisateur (pas plus de 50 caractères) : ")
                            repmdp=input("Entrer un mot de passe (pas plus de 50 caractères) : ")
                            if not len(repname)>=50 and not len(repmdp)>=50:
                                if repmdp=="shutdown":
                                    cmd_fonction.clear()
                                    print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                                    print(colored("Le mot de passe ne peut pas être 'shutdown'","red",attrs=["bold"]))
                                elif repname in ["1","2","3","4"]:
                                    cmd_fonction.clear()
                                    print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                                    print(colored("Le nom d'utilisateur ne peut pas être 1, 2, 3 ou 4","red",attrs=["bold"]))
                                else:
                                    try:
                                        key=indecode.generate_key()
                                        commandsql="INSERT INTO utilisateur VALUES ('"+str(repname)+"','"+str(indecode.code(repmdp,key))+"',0,'"+key+"');"
                                        cur.execute(commandsql)
                                        connsql.commit()
                                        commandsql="INSERT INTO settings VALUES ('"+str(repname)+"',0,1,1);"
                                        cur.execute(commandsql)
                                        connsql.commit()
                                        os.makedirs(adresseapp+"/user/"+repname+"/image")
                                        os.makedirs(adresseapp+"/user/"+repname+"/music")
                                        os.makedirs(adresseapp+"/user/"+repname+"/save_module")
                                        os.makedirs(adresseapp+"/user/"+repname+"/download")
                                        logtxt=open(adresseapp+"/logs/"+repname+".txt","w")
                                        logtxt.close()
                                        logtxt=open(adresseapp+"/user/"+repname+"/log.txt","w")
                                        logtxt.write("1")
                                        logtxt.close()
                                        log=1
                                        app=appinitext(repname)
                                        adresse=adresse+"/user/"+repname
                                        adresseuser=adresse
                                        mdpt=repmdp
                                        cur.execute("SELECT * FROM utilisateur WHERE nom='"+repname+"';")
                                        repsqluser=cur.fetchall()
                                        cur.execute("SELECT * FROM settings WHERE nom='"+repname+"';")
                                        repsqlset=cur.fetchall()
                                        repsqluser=list(repsqluser[0])
                                        repsqlset=list(repsqlset[0])
                                        valida="ok"
                                    except psycopg2.errors.UniqueViolation:
                                        cmd_fonction.clear()
                                        print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                                        print(colored("Le nom d'utilisateur est déja pris","red",attrs=["bold"]))
                            else:
                                cmd_fonction.clear()
                                print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                                print(colored("Une valeur entrée n'est pas valide","red",attrs=["bold"]))
                    else:
                        cmd_fonction.clear()
                        print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                        print(colored("Vous devez être connecté à internet pour vous connecter","red",attrs=["bold"]))
                elif rep=="3":
                    mdpt=0
                    admin=0
                    displaysplit=0
                    logserver=0
                    charginstall=0
                    invit=1
                    repname="Guest"
                    log=0
                    adresseuser=adresse
                    key=indecode.generate_key()
                    cmd_fonction.clear()
                    print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                    print("""Taper "help" pour plus d'information""")
                    cmd(admin,charginstall,displaysplit,logserver,repname,mdpt,adresseuser,key,log,invit)
                    return
                elif rep=="4":
                    cmd_fonction.clear()
                    exit()
                elif rep in fichiers:
                    valida="no"
                    while valida!="ok":
                        repname=rep
                        print(colored("Taper shutdown pour éteindre"))
                        repmdp=input("Taper votre mot de passe : ")
                        if not repmdp=="shutdown":
                            if cmd_fonction.connect():
                                cur.execute("SELECT * FROM utilisateur WHERE nom='"+repname+"';")
                                repsqluser=cur.fetchall()
                                cur.execute("SELECT * FROM settings WHERE nom='"+repname+"';")
                                repsqlset=cur.fetchall()
                                repsqluser=list(repsqluser[0])
                                repsqlset=list(repsqlset[0])
                                if repmdp==indecode.decode(repsqluser[1],repsqluser[3]):
                                    mdpt=indecode.decode(repsqluser[1],repsqluser[3])
                                    adresse=adresse+"/user/"+repname
                                    adresseuser=adresse
                                    app=appinitext(repname)
                                    logtxt=open("user/"+repname+"/log.txt")
                                    data=logtxt.readlines()
                                    data=data[0]
                                    log=int(data)
                                    logtxt.close()
                                    valida="ok"
                                    break
                                else:
                                    cmd_fonction.clear()
                                    print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                                    print(colored("Le mot de passe n'est pas correct","red",attrs=["bold"]))
                            else:
                                cmd_fonction.clear()
                                print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                                print(colored("Vous devez être connecté à internet pour vous connecter","red",attrs=["bold"]))
                                break
                        else:
                            return
                else:
                    cmd_fonction.clear()
                    print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                    print(colored("La valeur entrée n'est pas valide","red",attrs=["bold"]))
                if valida=="ok":
                    admin=repsqluser[2]
                    displaysplit=repsqlset[1]
                    logserver=repsqlset[3]
                    charginstall=repsqlset[2]
                    key=repsqluser[3]
                    cmd_fonction.clear()
                    print(colored(("CmdOS v"+version),"green",attrs=["bold"]))
                    print("""Taper "help" pour plus d'information""")
                    a=0
                    cmd(admin,charginstall,displaysplit,logserver,repname,mdpt,adresseuser,key,log)
                    return
while True :
    login()
    if a==1:
        a=0
        adresse=os.path.realpath(__file__)
        adresse=os.path.dirname(adresse)
        login()
    else:
        break
connect.quit()
cur.close()
connsql.close()
cmd_fonction.clear()