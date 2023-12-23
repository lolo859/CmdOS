#####################################################################
#Boot et clear
#####################################################################
import os
os.chdir(os.path.dirname(__file__))
try:
    from system.shellter_main import clear
    from system.shellter_core import initialise
    from system.sysdefender import analyse_module
except ModuleNotFoundError:
    print("Erreur : le boot n'as pas pu être lancé, veuiller utiliser get-cmdos pour réinstaller CmdOS")
    quit()
clear()
print("start boot...")
print("start import...")
from genericpath import exists
from os import listdir
from os.path import isfile, join
import os.path
import os
i=1
print("import "+str(i)+"/22")
i=i+1
from random import random
print("import "+str(i)+"/22")
i=i+1
from termcolor import colored
print("import "+str(i)+"/22")
i=i+1
import requests as req
print("import "+str(i)+"/22")
i=i+1
import system.shellter_main
print("import "+str(i)+"/22")
i=i+1
from datetime import datetime
print("import "+str(i)+"/22")
i=i+1
from ftplib import FTP
print("import "+str(i)+"/22")
i=i+1
import ftplib
print("import "+str(i)+"/22")
i=i+1
import subprocess
print("import "+str(i)+"/22")
i=i+1
import sys
print("import "+str(i)+"/22")
i=i+1
import webbrowser
print("import "+str(i)+"/22")
i=i+1
import secure_id
print("import "+str(i)+"/22")
i=i+1
import indecode
print("import "+str(i)+"/22")
i=i+1
import urllib
print("import "+str(i)+"/22")
i=i+1
import zipfile
print("import "+str(i)+"/22")
i=i+1
import psycopg2
print("import "+str(i)+"/22")
i=i+1
import shutil
print("import "+str(i)+"/22")
i=i+1
import platform
print("import "+str(i)+"/22")
i=i+1
import time
print("import "+str(i)+"/22")
i=i+1
import sys
print("import "+str(i)+"/22")
i=i+1
import psutil
print("import "+str(i)+"/22")
i=i+1
import hashint
print("import "+str(i)+"/22")
i=i+1
print("import finish")
print("boot shellter...")
charginstall,displaysplit,logserver,version,invit,a,help,com,connect,cur,connsql,adresse,adresseapp,Result,check_update,autoclear,online,notfoundbehaviour=system.shellter_main.main()
print("starting login() protocol...")
ids=initialise(adresseapp)
##########################
#Fonction Cmd
##########################
def cmd(admin,charginstall,displaysplit,logserver,repname,mdpt,adresseuser,key,log,color,invit=0):
#################################
#Variable, module
#################################
    global adresse,repmdp,connect,version,a,adresseapp,Result,cur,connsql,connect,help,com,ids,check_update,autoclear,notfoundbehaviour
    while True:
###########################################
#Gestion entrée utilisateur
###########################################
        if admin==0:
            demande=colored(repname,"green",attrs=["bold"])+colored("@","green",attrs=["bold"])+colored(platform.uname().node+"."+platform.uname().system,"cyan",attrs=["bold"])+":"+colored(adresse,"blue",attrs=["bold"])+" >>> "
        else:
            demande=colored(repname,"green",attrs=["bold"])+colored("(admin)","red",attrs=["bold"])+colored("@","green",attrs=["bold"])+colored(platform.uname().node+"."+platform.uname().system,"cyan",attrs=["bold"])+":"+colored(adresse,"blue",attrs=["bold"])+" >>> "
        rep=input(demande)
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
                    logtxt.write("adresseapp='"+adresseapp+"'\n")
                    logtxt.write("os.getcwd()='"+str(os.getcwd())+"'\n")
                    logtxt.write("invit="+str(invit)+"\n")
                    logtxt.write("log="+str(log)+"\n")
                    logtxt.write("check_update="+str(check_update)+"\n")
                    logtxt.write("autoclear="+str(autoclear)+"\n")
                    logtxt.write("color="+str(color)+"\n")
                    logtxt.write("notfoundbehaviour='"+str(notfoundbehaviour)+"'\n")
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
                    logtxt.write("adresseapp='"+adresseapp+"'\n")
                    logtxt.write("os.getcwd()='"+str(os.getcwd())+"'\n")
                    logtxt.write("invit="+str(invit)+"\n")
                    logtxt.write("log="+str(log)+"\n")
                    logtxt.write("check_update="+str(check_update)+"\n")
                    logtxt.write("autoclear="+str(autoclear)+"\n")
                    logtxt.write("color="+str(color)+"\n")
                    logtxt.write("notfoundbehaviour='"+str(notfoundbehaviour)+"'\n")
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
#################################
#Check update,autoclear and command
#################################
        if check_update==1 and (not rep=="sh" or not rep=="shell") and system.shellter_main.connectt():
            versiontxt=req.get("https://cmdos.alwaysdata.net/cmdversion.txt",allow_redirects=True)
            open("cmdversion.txt","wb").write(versiontxt.content)
            vertxt=open("cmdversion.txt","r")
            vercheck=vertxt.readlines()[0]
            vertxt.close()
            if vercheck>version:
                printver=1
            else:
                printver=0
        else:
            printver=0
        if autoclear=="1":
            system.shellter_main.clear()
            Result.version()
            print("""Taper "help" pour plus d'information""")
#################################
#Help
#################################
        if rep=="help":
            i=Result(text=help,rt="stdout")
            i.print(ids,adresseapp,color)
        elif rep.startswith("help "):
            aide=rep[5::]
            if aide in com:
                print(com[aide])
            else:
                i=Result("commande",rt="notfound",object=aide,module="help")
                i.print(ids,adresseapp,color)
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
                    i=Result(os.stat(detail3),rt="stdout")
                    i.print(ids,adresseapp,color)
                else:
                    i=Result(module="detail",object=detail2,rt="notfound",text=None)
                    i.print(ids,adresseapp,color)
            else:
                i=Result(module="detail",text="La commande est mal formulée",rt="error")
                i.print(ids,adresseapp,color)
#################################
#Create dir
#################################
        elif rep.startswith("mkdir"):
            if invit==0:
                mkdir=rep.split()
                if displaysplit==1:
                    print(mkdir)
                if len(mkdir)==2:
                    namedir=mkdir[1]
                    try:
                        os.path.normpath(namedir)
                        os.makedirs(adresse+"/"+namedir)
                    except:
                        i=Result(module="mkdir",text="Le dossier existe déja ou contient des caractères interdits tel que : '/'",rt="error")
                        i.print(ids,adresseapp,color)   
                else:
                    i=Result(module="mkdir",text="La commande est mal formulée",rt="error")
                    i.print(ids,adresseapp,color)  
            else:
                i=Result(text="Le mode invité désactive cette commande",rt="error",module="system")
                i.print(ids,adresseapp,color)
#################################
#Move file
#################################
        elif rep.startswith("move"):
            if invit==0:
                move=rep.split()
                if displaysplit==1:
                    print(move)
                if len(move)>=3:
                    if move[1] in os.listdir(adresse) and os.path.exists(rep[6+len(move[1])::]) and os.path.isdir(rep[6+len(move[1])::]):
                        try:
                            shutil.move(adresse+"/"+move[1],rep[6+len(move[1])::]+"/"+move[1])
                        except:
                            i=Result(text="Une erreur est survenue, vérifier que vous avez les permissions pour voir le contenu de ce dossier",rt="error",module="move")
                            i.print(ids,adresseapp,color)
                    else:
                        i=Result("commande",rt="notfound",object="dossier/fichier",module="move")
                        i.print(ids,adresseapp,color)
                else:
                    i=Result(module="move",text="La commande est mal formulée",rt="error")
                    i.print(ids,adresseapp,color)  
            else:
                i=Result(text="Le mode invité désactive cette commande",rt="error",module="system")
                i.print(ids,adresseapp,color)
#################################
#Copy
#################################
        elif rep.startswith("copy"):
            if invit==0:
                move=rep.split()
                if displaysplit==1:
                    print(move)
                if len(move)>=3:
                    if move[1] in os.listdir(adresse) and os.path.exists(rep[6+len(move[1])::]) and os.path.isdir(rep[6+len(move[1])::]):
                        try:
                            shutil.copy2(adresse+"/"+move[1],rep[6+len(move[1])::]+"/"+move[1])
                        except:
                            i=Result(text="Une erreur est survenue, vérifier que vous avez les permissions pour voir le contenu de ce dossier",rt="error",module="copy")
                            i.print(ids,adresseapp,color)
                    else:
                        i=Result("commande",rt="notfound",object="dossier/fichier",module="move")
                        i.print(ids,adresseapp,color)
                else:
                    i=Result(module="move",text="La commande est mal formulée",rt="error")
                    i.print(ids,adresseapp,color)   
            else:
                i=Result(text="Le mode invité désactive cette commande",rt="error",module="system")
                i.print(ids,adresseapp,color)
#################################
#Admin
#################################
        elif rep.startswith("admin"):
            if invit==0:
                admin1=rep.split()
                if displaysplit==1:
                    print(admin1)
                if len(admin1)==2:
                    if admin1[1]=="on":
                        if admin==0:
                            if key=="local":
                                print("Vous êtes sur le point de passer en mode admin.\n\nEn tapant votre mot de passe, vous prenez conscience que :\n1)Vous vous engagez à ne pas abusez des pouvoirs qu'il vous confère\n2)Un grand pouvoir implique de grandes responsabilités\n")
                            else:
                                print("Vous êtes sur le point de passer en mode admin.\n\nEn tapant votre mot de passe, vous prenez conscience que :\n1)Vous vous engagez à ne pas abusez des pouvoirs qu'il vous confère\n2)Un grand pouvoir implique de grandes responsabilités\n3)Vous serez admin sur tous les appareils où vous êtes connectés\n")
                            demande=colored("Taper votre mot de passe : ","blue",attrs=["bold"])
                            repmdp=input(demande)
                            if repmdp==mdpt:
                                if key=="local":
                                    admin=1
                                    open(adresseapp+"/user/"+repname+"/admin.txt","w").write("1")
                                elif system.shellter_main.connectt()==True:
                                    if connsql==None or cur==None:
                                        connsql = psycopg2.connect(user = "cmdos",password = "CmdOS2008)",host = "postgresql-cmdos.alwaysdata.net",port = "5432",database = "cmdos_user")
                                        cur = connsql.cursor()
                                    admin=1
                                    commandsql="UPDATE utilisateur SET admin='1' WHERE nom='"+repname+"';"
                                    cur.execute(commandsql)
                                    connsql.commit()
                                else:
                                    i=Result(module="admin",text="Une erreur est survenue, veuillez vérifier votre connexion internet.",rt="error")
                                    i.print(ids,adresseapp,color)
                            else:
                                i=Result(module="admin",text="Le mot de passe est incorrect",rt="error")
                                i.print(ids,adresseapp,color)
                        else:
                            i=Result(text="Le mode admin est déja activé sur ce compte",rt="important")
                            i.print(ids,adresseapp,color)
                    elif admin1[1]=="off":
                        if admin==1:
                            if key=="local":
                                admin=0
                                open(adresseapp+"/user/"+repname+"/admin.txt","w").write("0")
                            elif system.shellter_main.connectt()==True:
                                if connsql==None or cur==None:
                                    connsql = psycopg2.connect(user = "cmdos",password = "CmdOS2008)",host = "postgresql-cmdos.alwaysdata.net",port = "5432",database = "cmdos_user")
                                    cur = connsql.cursor()
                                admin=0
                                commandsql="UPDATE utilisateur SET admin='0' WHERE nom='"+repname+"';"
                                cur.execute(commandsql)
                                connsql.commit()
                            else:
                                i=Result(module="admin",text="Une erreur est survenue, veuillez vérifier votre connexion internet.",rt="error")
                                i.print(ids,adresseapp,color)
                        else:
                            i=Result("Le mode admin est déja désactivé","important")
                            i.print(ids,adresseapp,color)
                    else:
                        i=Result("La commande est mal formulée","error",module="admin")
                        i.print(ids,adresseapp,color)
                else:
                    i=Result("La commande est mal formulée","error",module="admin")
                    i.print(ids,adresseapp,color)
            else:
                i=Result(text="Le mode invité désactive cette commande",rt="error",module="system")
                i.print(ids,adresseapp,color)
#################################
#Supprimer
#################################
        elif rep.startswith("del"):
            if invit==0:
                supr=rep.split()
                if displaysplit==1:
                    print(supr)
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
                                i.print(ids,adresseapp,color)
                        except:
                            i=Result(text="Une erreur est survenue, vérifier que vous avez les permissions pour supprimer ce ficher",rt="error",module="system")
                            i.print(ids,adresseapp,color)
                    else:
                        i=Result(module="del",object=supr[1],rt="notfound",text=None)
                        i.print(ids,adresseapp,color)
                else:
                    i=Result("La commande est mal formulée","error",module="del")
                    i.print(ids,adresseapp,color)
            else:
                i=Result(text="Le mode invité désactive cette commande",rt="error",module="system")
                i.print(ids,adresseapp,color)
#################################
#Renommer
#################################
        elif rep.startswith("ren"):
            if invit==0:
                ren=rep[4::]
                fichiers = os.listdir(adresse)
                if ren in fichiers:
                    ren2=adresse+"/"+ren
                    ren3=adresse+"/"+input("Nouveau nom : ")
                    try:
                        os.rename(ren2, ren3)
                    except:
                        i=Result(text="Une erreur est survenue, vérifier que vous avez les permissions pour renommer ce ficher",rt="error",module="system")
                        i.print(ids,adresseapp,color)
                else:
                    i=Result(module="ren",object=ren,rt="notfound",text=None)
                    i.print(ids,adresseapp,color)
            else:
                i=Result(text="Le mode invité désactive cette commande",rt="error",module="system")
                i.print(ids,adresseapp,color)
#################################
#Cd : change directory
#################################
        elif rep.startswith("cd"):
            cd=rep.split()
            if displaysplit==1:
                print(cd)
            if len(cd)>=2:
                if rep[3::]=="..":
                    adresse=os.path.dirname(adresse)
                elif rep[3::]=="~":
                    if invit==0:
                        adresse=adresseuser
                    else:
                        i=Result(text="Le mode invité désactive cette commande",rt="error",module="system")
                        i.print(ids,adresseapp,color)
                elif os.path.isabs(rep[3::]) and os.path.exists(rep[::3]):
                    adresse=rep[3::]
                elif os.path.exists(os.path.join(adresse,rep[3::])) and os.path.isdir(os.path.join(adresse,rep[3::])):
                    adresse=os.path.join(adresse,rep[3::])
                else:
                    i=Result("Le dossier n'est pas valide","error",module="cd")
                    i.print(ids,adresseapp,color)
            else:
                i=Result("La commande est mal formulée","error",module="cd")
                i.print(ids,adresseapp,color)
#################################
#Create file
#################################
        elif rep.startswith("mktxt"):
            if invit==0:
                tex=rep.split()
                if displaysplit==1:
                    print(tex)
                if len(tex)>=3:
                    try:
                        contenu=rep[7+len(tex[1])::]
                        text=open(adresse+"/"+tex[1],"w")
                        text.write(contenu)
                        text.close()
                    except:
                        i=Result(text="Une erreur est survenue, vérifier que vous avez les permissions pour voir le contenu de ce dossier",rt="error",module="mktxt")
                        i.print(ids,adresseapp,color)
                else:
                    i=Result("La commande est mal formulée","error",module="mktxt")
                    i.print(ids,adresseapp,color)
            else:
                i=Result(text="Le mode invité désactive cette commande",rt="error",module="system")
                i.print(ids,adresseapp,color)
#################################
#Dir : directory
#################################
        elif rep=="dir":
            try:
                if os.listdir(adresse)==[]:
                    i=Result("Le dossier est vide",rt="stdout")
                    i.print(ids,adresseapp,color)
                else:
                    fichiers = os.listdir(adresse)
                    longueur=len(fichiers)
                    i=Result("Voici les fichiers/dossiers dans ce dossier :",rt="stdout")
                    i.print(ids,adresseapp,color)
                    for element in range(longueur):
                        i=Result(" "+fichiers[element],rt="stdout")
                        i.print(ids,adresseapp,color)
            except:
                i=Result(text="Une erreur est survenue, vérifier que vous avez les permissions pour voir le contenu de ce dossier",rt="error",module="dir")
                i.print(ids,adresseapp,color)
#################################
#Cat
#################################
        elif rep.startswith("cat"):
            cat=rep[4::]
            if os.path.exists(adresse+"/"+cat) and cat in os.listdir(adresse):
                try:
                    cat1=open(adresse+"/"+cat,"r").readlines()
                    for i in cat1:
                        print(i)
                except:
                    i=Result(text="Une erreur est survenue, vérifier que vous avez les permissions pour voir le contenu de ce dossier",rt="error",module="cat")
                    i.print(ids,adresseapp,color)
            else:
                i=Result(module="cat",object=cat,rt="notfound",text=None)
                i.print(ids,adresseapp,color)
#################################
#Logs
#################################
        elif rep.startswith("log"):
            if invit==0:
                if admin==1:
                    log1=rep.split()
                    if displaysplit==1:
                        print(log1)
                    if len(log1)==2 and type(log1[1])==str:
                        if log1[1]=="enable":
                            logtxt=open(adresseapp+"/user/"+repname+"/log.txt","w")
                            logtxt.write("1")
                            logtxt.close()
                            log=1
                            i=Result("Les logs sont activés sur votre compte local","important")
                            i.print(ids,adresseapp,color)
                        elif log1[1]=="disable":
                            logtxt=open(adresseapp+"/user/"+repname+"/log.txt","w")
                            logtxt.write("0")
                            logtxt.close()
                            log=0
                            i=Result("Les logs sont désactivés sur votre compte local","important")
                            i.print(ids,adresseapp,color)
                        elif log1[1]=="delete":
                            logtxt=open("logs/"+repname+".txt","w")
                            logtxt.write("")
                            logtxt.close()
                            i=Result("Les logs ont bien été supprimé","important")
                            i.print(ids,adresseapp,color)
                        else:
                            i=Result("La commande est mal formulée","error",module="log")
                            i.print(ids,adresseapp,color)
                    elif len(log1)==1:
                        if log==1:
                            i=Result("Les logs sont activés sur votre compte local","important")
                            i.print(ids,adresseapp,color)
                        else:
                            i=Result("Les logs sont déactivés sur votre compte local","important")
                            i.print(ids,adresseapp,color)
                    else:
                        i=Result("La commande est mal formulée","error",module="log")
                        i.print(ids,adresseapp,color)
                else:
                    i=Result("Vous devez être connecté en tant qu'administrateur pour utiliser cette commande","error",module="log")
                    i.print(ids,adresseapp,color)
            else:
                i=Result(text="Le mode invité désactive cette commande",rt="error",module="system")
                i.print(ids,adresseapp,color)
#################################
#Store install
#################################
        elif rep.startswith("store install "):
            if invit==0:
                if system.shellter_main.connectt():
                    try:
                        install=rep[14::]
                        cur.execute("SELECT link FROM module WHERE name='"+install+"';")
                        data=cur.fetchall()
                        if not data==[]:
                            if not install in os.listdir(adresseapp+"/module"):
                                data=list(data[0])
                                data=data[0]
                                print("Récupération des fichiers du module...")
                                filename, headers = urllib.request.urlretrieve(data+"/archive/refs/heads/main.zip", filename=adresseapp+"/"+install+".zip")
                                print("Dépaquetage en cours...")
                                with zipfile.ZipFile(adresseapp+"/"+install+".zip","r") as zipref:
                                    zipref.extractall(adresseapp)
                                os.remove(adresseapp+"/"+install+".zip")
                                list_file=os.listdir(adresseapp+"/"+install+"-main")
                                os.makedirs(adresseapp+"/module/"+install)
                                for file in list_file:
                                    print("Déplacement du fichier "+file+" depuis "+adresseapp+"/"+install+"-main/"+file+" vers "+adresseapp+"/module/"+install)
                                    shutil.move(adresseapp+"/"+install+"-main/"+file,adresseapp+"/module/"+install)
                                os.rmdir(adresseapp+"/"+install+"-main")
                                i=Result("Le module "+install+" a bien été installé","stdout")
                            else:
                                i=Result(text="Le module est déja installé",rt="error",module="store")
                                i.print(ids,adresseapp,color)  
                        else:
                            i=Result(module="store",object=install,rt="notfound",text=None)
                            i.print(ids,adresseapp,color)
                    except:
                        i=Result(text="Une erreur est survenue, veulliez vérifier votre connexion Internet.",rt="error",module="store")
                        i.print(ids,adresseapp,color)  
                else:
                    i=Result(text="Il faut être connecté à Internet pour utiliser cette commande",rt="error",module="store")
                    i.print(ids,adresseapp,color)   
            else:
                i=Result(text="Le mode invité désactive cette commande",rt="error",module="system")
                i.print(ids,adresseapp,color)
#################################
#Shell
#################################
        elif rep=="shutdown" or rep=="sh" or rep=="shell":
            system.shellter_main.clear()
            quit()
#################################
#Store uninstall
#################################
        elif rep.startswith("store uninstall "):
            if invit==0:
                uninstall=rep[16::]
                try:
                    shutil.rmtree(adresseapp+"/module/"+uninstall)
                except:
                    i=Result(module="store",object=uninstall,rt="notfound",text=None)
                    i.print(ids,adresseapp,color)
            else:
                i=Result(text="Le mode invité désactive cette commande",rt="error",module="system")
                i.print(ids,adresseapp,color)
#################################
#store
#################################
        elif rep=="store":
            if system.shellter_main.connectt():
                try:
                    cur.execute("SELECT * FROM module;")
                    data=cur.fetchall()
                    data=list(data)
                    i=Result("Voici tous les modules disponibles :","stdout")
                    i.print(ids,adresseapp,color)
                    for i in range(len(data)):
                        i=Result(text="#"+str(i+1)+" "+data[i][0]+" : "+data[i][4],rt="stdout")
                        i.print(ids,adresseapp,color)
                except:
                    i=Result(text="Une erreur est survenue, veulliez vérifier votre connexion Internet.",rt="error",module="store")
                    i.print(ids,adresseapp,color)  
            else:
                i=Result(text="Il faut être connecté à Internet pour utiliser cette commande",rt="error",module="store")
                i.print(ids,adresseapp,color)      
#################################
#store info
#################################
        elif rep.startswith("store info"):
            if system.shellter_main.connectt():
                try:
                    cur.execute("SELECT * FROM module WHERE name='"+rep[11::]+"';")
                    data=cur.fetchall()
                    if not data==[]:
                        data=list(data[0])
                        i=Result("Information sur le module:","stdout")
                        i.print(ids,adresseapp,color)
                        i=Result(text=("Nom : "+data[0]),rt="stdout")
                        i.print(ids,adresseapp,color)
                        i=Result(text=("Auteur : "+data[1]),rt="stdout")
                        i.print(ids,adresseapp,color)
                        i=Result(text=("Taille : "+data[2]),rt="stdout")
                        i.print(ids,adresseapp,color)
                        i=Result(text=("Dernière version : "+data[3]),rt="stdout")
                        i.print(ids,adresseapp,color)
                        i=Result(text=("Description : "+data[4]),rt="stdout")
                        i.print(ids,adresseapp,color)
                        i=Result(text=("Autorisation : "+data[5]),rt="stdout")
                        i.print(ids,adresseapp,color)
                        i=Result(text=("Lien vers le github : "+data[6]),rt="stdout")
                        i.print(ids,adresseapp,color)
                    else:
                        i=Result(text="Ce module n'existe pas",rt="error",module="store")
                        i.print(ids,adresseapp,color) 
                except:
                    i=Result(text="Une erreur est survenue, veulliez vérifier votre connexion Internet.",rt="error",module="store")
                    i.print(ids,adresseapp,color)  
            else:
                i=Result(text="Il faut être connecté à Internet pour utiliser cette commande",rt="error",module="store")
                i.print(ids,adresseapp,color)
#################################
#Sys
#################################
        elif rep.startswith("sys"):
            if invit==0:
                sys1=rep.split()
                if displaysplit==1:
                    print(sys1)
                if len(sys1)>=2:
                    if sys1[1]=="update" and len(sys1)==3: 
                        if sys1[2]=="upgrade":
                            if system.shellter_main.connectt()==True:
                                i=Result(text="Vous allez télécharger le fichier zip contenant l'assistant pour mettre à jour CmdOS",rt="important")
                                i.print(ids,adresseapp,color)
                                webbrowser.open("https://github.com/lolo859/get-cmdos/archive/refs/heads/main.zip")
                            else:
                                i=Result("Vous devez être connecté à internet pour mettre à jour CmdOS","error",module="sys.update")
                                i.print(ids,adresseapp,color)
                        elif sys1[2]=="check" and system.shellter_main.connectt()==True:
                            versiontxt=req.get("https://cmdos.alwaysdata.net/cmdversion.txt",allow_redirects=True)
                            open("cmdversion.txt","wb").write(versiontxt.content)
                            vertxt=open("cmdversion.txt","r")
                            verlist=vertxt.readlines()
                            vertxt.close()
                            if str(verlist[0])==version:
                                versionprint="CmdOS "+version
                                Result.version(color)
                                i=Result("Votre système est à jour",rt="important")
                                i.print(ids,adresseapp,color)
                            elif str(verlist[0])<version:
                                versionprint="Vous êtes actuellement sur la version de développement "+version
                                i=Result(versionprint,"important")
                                i.print(ids,adresseapp,color)
                                i=Result("Cette version peut être instable",rt="advert")
                                i.print(ids,adresseapp,color)
                                i=Result("Vous pouvez retourner à la version public avec update upgrade","important")
                                i.print(ids,adresseapp,color)
                            else:
                                i=Result("Votre système n'est pas a jour","advert")
                                i.print(ids,adresseapp,color)
                                versionprint="La dernière version disponible est CmdOS "+verlist[0]+"\nVous pouvez mettre a jour le système avec update upgrade"
                                i=Result(versionprint,"important")
                                i.print(ids,adresseapp,color)
                        else:
                            i=Result("La commande est mal formulée ou vous n'êtes pas connecté à internet","error",module="sys.update")
                            i.print(ids,adresseapp,color)
                    elif len(sys1)==2 and sys1[1]=="account":
                        i=Result(("Votre nom d'utilisateur : "+repname),"important")
                        i.print(ids,adresseapp,color)
                        i=Result(("Votre mot de passe : "+mdpt),"important")
                        i.print(ids,adresseapp,color)
                    elif len(sys1)==3 and sys1[1]=="account":
                        if type(sys1[2])==str:
                            if sys1[2]=="name" and system.shellter_main.connectt()==True and not key=="local":
                                answer=input("Taper votre nouveau nom d'utilisateur (pas plus de 50 caractères) : ")
                                if answer.startswith("local-") or answer in ["1","2","3","4","5"] or answer=="shutdown":
                                    i=Result("Le nom d'utilisateur est invalide",rt="error",module="sys.account.name")
                                    i.print(ids,adresseapp,color)
                                else:
                                    try:
                                        if not len(answer)>=50:
                                            commandsql="UPDATE utilisateur SET nom='"+str(answer)+"' WHERE nom='"+str(repname)+"';"
                                            cur.execute(commandsql)
                                            commandsql="UPDATE settings SET nom='"+str(answer)+"' WHERE nom='"+str(repname)+"';"
                                            cur.execute(commandsql)
                                            connsql.commit()
                                            os.rename(adresseapp+"/user/"+repname,adresseapp+"/user/"+answer)
                                            os.rename(adresseapp+"/logs/"+repname+".txt",adresseapp+"/logs/"+answer+".txt")
                                            adresse=adresseapp+"/user/"+answer
                                            adresseuser=adresseapp+"/user/"+answer
                                            repname=answer
                                        else:
                                            i=Result("Le nom d'utilisateur est invalide",rt="error",module="sys.account.name")
                                            i.print(ids,adresseapp,color)
                                    except psycopg2.errors.UniqueViolation:
                                        i=Result("Le nom d'utilisateur est déja pris",rt="error",module="sys.account.name")
                                        i.print(ids,adresseapp,color)
                            elif sys1[2]=="name" and key=="local":
                                answer=input("Taper votre nouveau nom d'utilisateur : ")
                                if answer in ["1","2","3","4","5"] or answer=="shutdown":
                                    i=Result("Le nom d'utilisateur est invalide",rt="error",module="sys.account.name")
                                    i.print(ids,adresseapp,color)
                                else:
                                    try:
                                        os.rename(adresseapp+"/user/"+repname,adresseapp+"/user/local-"+answer)
                                        os.rename(adresseapp+"/logs/"+repname+".txt",adresseapp+"/logs/local-"+answer+".txt")
                                        adresse=adresseapp+"/user/local-"+answer
                                        adresseuser=adresseapp+"/user/local-"+answer
                                        repname="local-"+answer
                                    except FileExistsError:
                                        i=Result("Le nom d'utilisateur est déja pris",rt="error",module="sys.account.name")
                                        i.print(ids,adresseapp,color)
                            elif sys1[2]=="password" and system.shellter_main.connectt()==True and not key=="local":
                                answer=input("Taper votre nouveau mot de passe (pas plus de 50 caractères) : ")
                                if not len(answer)>=50:
                                    commandsql="UPDATE utilisateur SET mdp='"+str(indecode.code(answer,key))+"' WHERE nom='"+str(repname)+"';"
                                    cur.execute(commandsql)
                                    connsql.commit()
                                    mdpt=answer
                                else:
                                    i=Result("Le mot de passe est invalide",rt="error",module="sys.account.password")
                                    i.print(ids,adresseapp,color)
                            elif sys1[2]=="password" and key=="local":
                                answer=input("Taper votre nouveau mot de passe : ")
                                try:
                                    mdpt=answer
                                    open(adresseapp+"/user/"+repname+"/mdp.txt","w").write(hashint.hash8192(answer))   
                                except:
                                    i=Result("Une erreur est survenue, cela est surement du à un caractère non encodable.",rt="error",module="sys.account.password")
                                    i.print(ids,adresseapp,color)
                            elif sys1[2]=="disconnect" and not key=="local":
                                answer=input("Voulez vous vraiment déconnecter votre compte ? (o/n) : ")
                                if answer=="o":
                                    shutil.rmtree(adresseuser)
                                    try:
                                        os.remove(adresseapp+"/logs/"+repname+".txt")
                                    except:
                                        pass
                                    a=1
                                    return
                            elif sys1[2]=="disconnect" and key=="local":
                                i=Result("Cette fonctionalité n'est pas disponible pour les comptes locaux.",rt="error",module="sys.account.disconnect")
                                i.print(ids,adresseapp,color)
                            elif sys1[2]=="delete" and system.shellter_main.connectt()==True and not key=="local":
                                answer=input("Voulez vous vraiment supprimer votre compte ? (o/n) : ")
                                if answer=="o":
                                    shutil.rmtree(adresseuser)
                                    commandsql="DELETE FROM utilisateur WHERE nom='"+repname+"';"
                                    cur.execute(commandsql)
                                    connsql.commit()
                                    commandsql="DELETE FROM settings WHERE nom='"+repname+"';"
                                    cur.execute(commandsql)
                                    connsql.commit()
                                    os.remove(adresseapp+"/logs/"+repname+".txt")
                                    a=1
                                    return
                            elif sys1[2]=="delete" and key=="local":
                                answer=input("Voulez vous vraiment supprimer votre compte ? (o/n) : ")
                                if answer=="o":
                                    shutil.rmtree(adresseuser)
                                    os.remove(adresseapp+"/logs/"+repname+".txt")
                                    a=1
                                    return
                            elif sys1[2]=="reset" and system.shellter_main.connectt()==True and not key=="local":
                                key=indecode.generate_key()
                                commandsql="UPDATE utilisateur SET mdp='"+str(indecode.code(mdpt,key))+"',key='"+key+"' WHERE nom='"+str(repname)+"';"
                                cur.execute(commandsql)
                                connsql.commit()
                                i=Result("Votre clé de cryptage à bien été changé","stdout")
                                i.print(ids,adresseapp,color)
                            elif sys1[2]=="reset" and key=="local":
                                i=Result("Cette fonctionalité n'est pas disponible pour les comptes locaux.",rt="error",module="sys.account.reset")
                                i.print(ids,adresseapp,color)
                            else:
                                i=Result("La commande est mal formulée ou vous n'êtes pas connecté à internet","error",module="sys.account")
                                i.print(ids,adresseapp,color)
                        else:
                            i=Result("La commande est mal formulée","error",module="sys.account")
                            i.print(ids,adresseapp,color)
                    elif sys1[1]=="scan":
                        i=Result("Le système va scanner le disque pour détecter d'autre instance de CmdOS",rt="stdout")
                        i.print(ids,adresseapp,color)
                        if input("Appuyer sur entrée pour continuer...")=="":
                            os.chdir(adresse)
                            system.shellter_main.clear()
                            i=Result("Scan du disque...",rt="stdout")
                            i.print(ids,adresseapp,color)
                            if str(sys.platform).startswith("win"):
                                text=[os.path.join(root, file) for root, _, files in os.walk("C:\\") for file in files]
                            else:
                                text=[os.path.join(root, file) for root, _, files in os.walk("/") for file in files]
                            i=Result("Recherche d'autre instance de CmdOS...",rt="stdout")
                            i.print(ids,adresseapp,color)
                            occur=[]
                            number=[]
                            for i in range(len(text)):
                                print(str(i+1)+"/"+str(len(text)))
                                if text[i].find("CmdOS.py")!=-1:
                                    number.append(str(i+1))
                                    occur.append(text[i])
                            if len(occur)>1:
                                i=Result("Nous avons trouvé "+str(len(occur)-1)+" autres instances de CmdOS",rt="stdout")
                                i.print(ids,adresseapp,color)
                                i=Result("Voici les autres instances de CmdOS que nous avons trouvé : ",rt="stdout")
                                i.print(ids,adresseapp,color)
                                for i in occur:
                                    print(i)
                            else:
                                i=Result("Nous n'avons pas trouvé d'autre instance de CmdOS sur le disque",rt="stdout")
                                i.print(ids,adresseapp,color)
                    elif sys1[1]=="purge":
                        fichier=os.listdir(adresseapp+"/temp")
                        for i in fichier:
                            os.remove(adresseapp+"/temp/"+i)
                        try:
                            os.remove(adresseuser+"/tree.txt")
                        except:
                            pass
                        try:
                            os.remove(adresseuser+"/content.txt")
                        except:
                            pass
                    elif sys1[1]=="info":
                        Result.version(color)
                        i=Result("Nom de l'appareil : "+platform.uname().node,rt="stdout")
                        i.print(ids,adresseapp,color)
                        i=Result("Système hôte : "+platform.platform(),rt="stdout")
                        i.print(ids,adresseapp,color)
                        i=Result("Processeur : "+platform.processor(),rt="stdout")
                        i.print(ids,adresseapp,color)
                        i=Result("RAM : "+str(psutil.virtual_memory().total/1024/1024/1024)+" go",rt="stdout")
                        i.print(ids,adresseapp,color)
                        i=Result("CmdOS © 2022 by lolo859 is licensed under CC BY-NC-SA 4.0",rt="stdout")
                        i.print(ids,adresseapp,color)
                    else:
                        i=Result("La commande est mal formulée","error",module="sys")
                        i.print(ids,adresseapp,color)
                else:
                    i=Result("La commande est mal formulée","error",module="sys")
                    i.print(ids,adresseapp,color)
            else:
                i=Result(text="Le mode invité désactive cette commande",rt="error",module="system")
                i.print(ids,adresseapp,color)
#################################
#Store list
#################################
        elif rep=="store list":
            if invit==0:
                fichiers = os.listdir(adresseapp+"/module")
                longueur=len(fichiers)
                i=Result("Voici les module installés :",rt="stdout")
                i.print(ids,adresseapp,color)
                for element in range(longueur):
                    i=Result(" "+fichiers[element]+" v"+open(adresseapp+"/module/"+fichiers[element]+"/version.txt","r").readlines()[0],rt="stdout")
                    i.print(ids,adresseapp,color)
            else:
                i=Result(text="Le mode invité désactive cette commande",rt="error",module="system")
                i.print(ids,adresseapp,color)
#################################
#Clear
#################################
        elif rep=="clear":
            system.shellter_main.clear()
            Result.version(color)
            print("""Taper "help" pour plus d'information""")
#################################
#log out : déconnexion
#################################
        elif rep=="unlog":
            a=1
            return
#################################
#Crédits et license
#################################
        elif rep=="credits":
            i=Result("Merci à tous les contributeurs, spécialement aymem2112, 1ventorus et beaucoup d'autres ainsi qu'à tous les béta-testeurs.",rt="stdout")
            i.print(ids,adresseapp,color)
            i=Result("Thanks to all the contributors, especially aymem2112, 1ventorus and many others as well as all the beta testers.",rt="stdout")
            i.print(ids,adresseapp,color)
        elif rep=="license":
            i=Result("CmdOS © 2022 by lolo859 is licensed under CC BY-NC-SA 4.0",rt="stdout")
            i.print(ids,adresseapp,color)
#################################
#Godmode
#################################
        elif rep=="godmode" and invit==0:
            if admin==1 and system.shellter_main.connectt()==True:
                print(colored("Le godmode est un ensemble de fonctions et de paramètres conçus pour les dévéloppeurs, n'y toucher seulement si vous savez ce que vous faites",color[2],attrs=["bold"]))
                godmode1=input(colored("Quelle fonction voulez vous activer/utilisez ? : ",color[3],attrs=["bold"]))
                if godmode1=="sys.variables":
                    print("Cette fonction permet d'afficher la valeur des variables systèmes")
                    input("Taper entrer pour exécuter")
                    print("mdpt='"+mdpt+"'")
                    print("adresse='"+adresse+"'")
                    print("adresseapp='"+str(adresseapp)+"'")
                    print("adresseuser='"+str(adresseuser)+"'")
                    print("version="+version+"")
                    print("godmode1='"+godmode1+"'")
                    print("invit='"+str(invit)+"'")
                    print("log="+str(log)+"")
                    print("check_update="+str(check_update))
                    print("autoclear="+str(autoclear))
                    print("color="+str(color))
                    print("notfoundbehaviour='"+str(notfoundbehaviour)+"'")
                if godmode1=="sys.cmd.store.install.vanish_loading":
                    print("Cette fonction permet de masquer le chargement lors de l'installation d'un module")
                    input("Taper entrer pour exécuter")
                    vanish_loading="Entrer votre choix (valeur actuelle : "+str(charginstall)+") : "
                    godmode2=input(vanish_loading)
                    if int(godmode2)==1 or int(godmode2)==0 :
                        if not key=="local":
                            charginstall=int(godmode2)
                            commandsql="UPDATE settings SET loading_install="+str(charginstall)+" WHERE nom='"+repname+"';"
                            cur.execute(commandsql)
                            connsql.commit()
                        else:
                            charginstall=int(godmode2)
                            open(adresseapp+"/user/"+repname+"/charginstall.txt","w").write(str(godmode2))
                    else:
                        print("La valeur entrée n'est pas correcte")
                if godmode1=="sys.protocol.list":
                    print("Cette fonction permet de voir quel protocole système fait quelle action")
                    input("Taper entrer pour exécuter")
                    print("login() - protocole qui demande le mot de passe et lance le protocole cmd()")
                    print("cmd() - protocole qui gère les interactions avec l'utilisateur")
                    print("clear() - protocole qui efface l'invite de commande")
                    print("connect() - vérifie si on est connecté à internet")
                if godmode1=="sys.protocol.execute":
                    print("Cette fonction éxécute le protocole demandé (elle positionne automatiquement les arguments)")
                    input("Taper entrer pour exécuter")
                    godmode2=input("Quel protocole voulez vous éxécuter ? : ")
                    if godmode2=="cmd":
                        cmd(admin,charginstall,displaysplit,logserver,repname,mdpt,adresseuser,key,log,color)
                    if godmode2=="login":
                        login()
                    if godmode2=="clear":
                        system.shellter_main.clear()
                    if godmode2=="connect":
                        system.shellter_main.connectt()
                if godmode1=="sys.cmd.display_split":
                    print("Cette fonction permet d'afficher le split de la variable rep lors du traitement de la commande")
                    input("Taper entrer pour exécuter")
                    display_split="Entrer votre choix (valeur actuelle : "+str(displaysplit)+") : "
                    godmode3=input(display_split)
                    if int(godmode3)==1 or int(godmode3)==0 :
                        if not key=="local":
                            displaysplit=int(godmode3)
                            commandsql="UPDATE settings SET display_split="+str(charginstall)+" WHERE nom='"+repname+"';"
                            cur.execute(commandsql)
                            connsql.commit()
                        else:
                            displaysplit=int(godmode3)
                            open(adresseapp+"/user/"+repname+"/displaysplit.txt","w").write(str(godmode3))
                    else:
                        print("La valeur entrée n'est pas correcte")
                if godmode1=="sys.cmd.report":
                    print("Cette fonction permet d'activer/désactiver l'enregistrement des commandes sur le serveur de support")
                    input("Taper entrer pour exécuter")
                    report="Entrer votre choix (valeur actuelle : "+str(logserver)+") : "
                    godmode4=input(report)
                    if int(godmode4)==1 or int(godmode4)==0 :
                        if not key=="local":
                            logserver=int(godmode4)
                            commandsql="UPDATE settings SET log_server="+str(logserver)+" WHERE nom='"+repname+"';"
                            cur.execute(commandsql)
                            connsql.commit()
                        else:
                            print("Cette fonctionnalité n'est pas disponible pour les comptes locaux.")
                    else:
                        print("La valeur entrée n'est pas correcte")
                if godmode1=="sys.class.list":
                    print("Cette fonction fait la liste des classes systèmes")
                    input("Taper entrer pour exécuter")
                    print("Result() - permet l'affichage des résultats / erreurs des différentes commandes")
                if godmode1=="sys.shellter.reboot":
                    print("Cette fonction reboot le noyau de CmdOS")
                    input("Taper entrer pour exécuter")
                    godmode2=input("Etes vous sur de vouloir reboot Shellter (o/n) ? : ")
                    if godmode2=="o":
                        print("Reboot dans 3...")
                        time.sleep(1)
                        print("2...")
                        time.sleep(1)
                        print("1...")
                        time.sleep(1)
                        print("Reboot...")
                        charginstall,displaysplit,logserver,version,invit,a,help,com,connect,cur,connsql,adresse,adresseapp,Result,check_update,autoclear,online=system.shellter_main.main()
                if godmode1=="sys.auto_check_update":
                    print("Cette fonction active/désactive la vérification automatique des mises à jour. Cette fonction peut ralentir le système.")
                    input("Taper entrer pour exécuter")
                    godmode2=input("Entrer une valeur (0/1) (valeur actuelle : "+str(check_update)+") : ")
                    if godmode2=="1":
                        check_update=1
                        open(adresseapp+"/system/checkupdate.txt","w").write("1")
                    elif godmode2=="0":
                        check_update=0
                        open(adresseapp+"/system/checkupdate.txt","w").write("0")
                    else:
                        print("La valeur entrée n'est pas correcte")
                if godmode1=="sys.auto_clear":
                    print("Cette fonction active/désactive l'effacement de la console à chaque commande.")
                    input("Taper entrer pour exécuter")
                    godmode2=input("Entrer une valeur (0/1) (valeur actuelle : "+str(autoclear)+") : ")
                    if godmode2=="1":
                        autoclear=1
                        open(adresseapp+"/system/autoclear.txt","w").write("1")
                    elif godmode2=="0":
                        autoclear=0
                        open(adresseapp+"/system/autoclear.txt","w").write("0")
                    else:
                        print("La valeur entrée n'est pas correcte")
                if godmode1=="sys.cmd.color.reset":
                    print("Cette fonction permet de réinitialiser les couleurs des outputs.")
                    answer=input("Taper entrer pour exécuter")
                    if answer=="":
                        open(adresseapp+"/user/"+repname+"/color.txt","w").write("white\nred\nyellow\nblue\ngreen")
                        color=open(adresseapp+"/user/"+repname+"/color.txt","r").readlines()
                        for z in range(len(color)):
                            color[z]=color[z].rstrip("\n")
                if godmode1=="sys.cmd.color.set":
                    print("Cette fonction permet de modifier les couleurs des différents outputs du système.")
                    answer=input("Taper entrer pour exécuter")   
                    if answer=="":
                        un=input("Selectionner une couleur pour les sorties standards (white/blue/red/yellow/green/magenta) : ")
                        if un in ["white","blue","red","yellow","green","magenta"]:
                            color[0]=un
                        deux=input("Selectionner une couleur pour les erreurs (white/blue/red/yellow/green/magenta) : ")
                        if deux in ["white","blue","red","yellow","green","magenta"]:
                            color[1]=deux
                        trois=input("Selectionner une couleur pour les avertissements (white/blue/red/yellow/green/magenta) : ")
                        if trois in ["white","blue","red","yellow","green","magenta"]:
                            color[2]=trois
                        quatre=input("Selectionner une couleur pour éléments importants (white/blue/red/yellow/green/magenta) : ")
                        if quatre in ["white","blue","red","yellow","green","magenta"]:
                            color[3]=quatre
                        cinq=input("Selectionner une couleur pour l'affichage de la version (white/blue/red/yellow/green/magenta) : ")
                        if cinq in ["white","blue","red","yellow","green","magenta"]:
                            color[4]=cinq
                        txt=open(adresseapp+"/user/"+repname+"/color.txt","w")
                        txt.write(un+"\n"+deux+"\n"+trois+"\n"+quatre+"\n"+cinq)
                        txt.close()
                if godmode1=="sys.cmd.command_notfound_behaviour":
                    print("Cette fonction vous permet de choisir le comportement du système en cas de commande erronée.")
                    input("Taper entrer pour exécuter")   
                    answer=input("Choississez une option (error/cmd) : ")
                    if answer=="cmd":
                        notfoundbehaviour="cmd"
                        open(adresseapp+"/system/notfoundbehaviour.txt","w").write("cmd")
                    elif answer=="error":
                        notfoundbehaviour="error"
                        open(adresseapp+"/system/notfoundbehaviour.txt","w").write("error")
            else:
                i=Result(module="godmode",rt="error",text="Vous devez être connecté en tant qu'administrateur et à internet pour utiliser le godmode")
                i.print(ids,adresseapp,color)
###############################
#Module                       #
###############################
        elif not len(rep.split())==0 and rep.split()[0] in os.listdir(adresseapp+"/module") and invit==0:
            moduler=rep.split()[0]
            state=analyse_module(moduler,adresseapp,rep,displaysplit,repname)
            if state=="ok":
                pass
            elif state=="advert":
                if system.shellter_main.connectt():
                    i=Result(module="sysdefender",rt="advert",text="Ce module n'est pas dans le store mais aucune erreur n'est arrivé lors de son exécution, il est déconseillé d'exécuter des modules non officiels")
                    i.print(ids,adresseapp,color)
                else:
                    i=Result(module="sysdefender",rt="advert",text="En l'absence de connexion internet, nous ne pouvons déterminer si ce module n'est pas dangereux pour votre système.\nAucune erreur n'est arrivé durant son exécution.\nIl est déconseillé d'exécuter des modules non vérifiés.")
                    i.print(ids,adresseapp,color)
            elif state=="error":
                if system.shellter_main.connectt():
                    i=Result(module="sysdefender",rt="error",text="Une erreur est survenu lors de l'exécution de ce module.\nIl est recommandé de le supprimer avec 'store uninstall <nom du module>' car il est pottentiellement dangereux si il parvient à se faire passer pour un module officiel.")
                    i.print(ids,adresseapp,color)
                else:
                    i=Result(module="sysdefender",rt="error",text="En l'absence de connexion internet, nous n'avons pu déterminer si ce module est dangereux pour votre système.\nCependant une erreur est arrivé lors de son exécution.\nIl est recommandé de le supprimer avec 'store uninstall <nom du module>'.")
                    i.print(ids,adresseapp,color)
            if state=="ok":
                if not os.path.exists(adresseapp+"/module/"+moduler+"/authorisation.txt"):
                    try:
                        cur.execute("SELECT * FROM module WHERE name='"+moduler+"';")
                        infomodule=cur.fetchall()
                        infomodule=list(infomodule[0])
                        if infomodule[5]=="NULL":
                            autorisation=0
                        else:
                            autorisation=1
                            listnec=infomodule[5].split()
                    except:
                        autorisation=0
                    litauto="arg="+str(rep.split()[1::])
                else:
                    try:
                        infomodule=open(adresseapp+"/module/"+moduler+"/authorisation.txt","r").readlines()
                        if infomodule[0]=="NULL":
                            autorisation=0
                        else:
                            autorisation=1
                            listnec=infomodule[0].split()
                    except:
                        autorisation=0
                    litauto="arg="+str(rep.split()[1::])
                if autorisation==1:
                    if "displaysplit" in listnec:
                        litauto=litauto+",displaysplit="+str(displaysplit)
                    if "rep" in listnec:
                        litauto=litauto+""",rep=\""""+rep+"""\""""
                    if "adresse" in listnec:
                        litauto=litauto+""",adresse=r\""""+adresseapp+"/user/"+repname+"""\""""
                command="from module."+moduler+"."+moduler+" import execute\nexecute("+litauto+")"
                subprocess.run(["python", "-c",command])
#################################
#Commande n'existe pas
#################################
        else:
            if not rep=="":
                if notfoundbehaviour=="error":
                    error="cette commande n'existe pas ou le module en question n'est pas installé : essayer help"
                    i=Result(text=error,rt="error",module="system")
                    i.print(ids,adresseapp,color)
                else:
                    os.system(rep)
        if printver==1:
            print("system : une nouvelle mise à jour est disponible, faites 'sys update upgrade' pour faire la mise à jour")
#################################
#Login
#################################
def login():
    global adresse,invit,online,cur,connsql
    adresse=os.path.realpath(__file__)
    adresse=os.path.dirname(adresse)
    valida="no"
    system.shellter_main.clear()
    Result.version()
    if online==0:
        print(colored("CmdOS n'a pas pu établir la connexion avec la base de donnée. Taper 'reconnect' pour réessayer.","blue",attrs=["bold"]))
    if invit==0:
        while True:
            if len(os.listdir(adresse+"/user"))==0:
                compte=input("Vouler vous vous connecter (1), créer un compte (2), activer le mode invité (3), créer un compte local (4) ou annuler (5) ? : ")
                system.shellter_main.clear()
                Result.version()
                if compte=="1":
                    if system.shellter_main.connectt() and online==1:
                        valida="no"
                        while valida!="ok":
                            repname=input("Taper votre nom d'utilisateur : ")
                            repmdp=input("Taper votre mot de passe : ")
                            cur.execute("SELECT * FROM utilisateur WHERE nom='"+repname+"';")
                            repsqluser=cur.fetchall()
                            cur.execute("SELECT * FROM settings WHERE nom='"+repname+"';")
                            repsqlset=cur.fetchall()
                            if repsqluser==[]:
                                system.shellter_main.clear()
                                Result.version()
                                print(colored("Le compte n'existe pas","red",attrs=["bold"]))
                            else:
                                repsqluser=list(repsqluser[0])
                                repsqlset=list(repsqlset[0])
                                if repmdp==indecode.decode(repsqluser[1],repsqluser[3]):
                                    os.makedirs(adresseapp+"/user/"+repname+"/image")
                                    os.makedirs(adresseapp+"/user/"+repname+"/music")
                                    os.makedirs(adresseapp+"/user/"+repname+"/download")
                                    logtxt=open(adresseapp+"/logs/"+repname+".txt","w")
                                    logtxt.close()
                                    logtxt=open(adresseapp+"/user/"+repname+"/log.txt","w")
                                    logtxt.write("1")
                                    logtxt.close()
                                    open(adresseapp+"/user/"+repname+"/color.txt","w").write("white\nred\nyellow\nblue\ngreen")
                                    color=open(adresseapp+"/user/"+repname+"/color.txt","r").readlines()
                                    for z in range(len(color)):
                                        color[z]=color[z].rstrip("\n")
                                    adresse=adresse+"/user/"+repname
                                    adresseuser=adresse
                                    valida="ok"
                                else:
                                    system.shellter_main.clear()
                                    Result.version()
                                    print(colored("Le mot de passe n'est pas correct","red",attrs=["bold"]))
                        mdpt=indecode.decode(repsqluser[1],repsqluser[3])
                        admin=repsqluser[2]
                        displaysplit=repsqlset[1]
                        logserver=repsqlset[3]
                        charginstall=repsqlset[2]
                        key=repsqluser[3]
                        log=1
                        system.shellter_main.clear()
                        Result.version()
                        print("""Taper "help" pour plus d'information""")
                        cmd(admin,charginstall,displaysplit,logserver,repname,mdpt,adresseuser,key,log,color)
                        return
                    else:
                        system.shellter_main.clear()
                        Result.version()
                        print(colored("Vous devez être connecté à internet pour vous connecter","red",attrs=["bold"]))
                elif compte=="2":
                    if system.shellter_main.connectt() and online==1:
                        valida="no"
                        while valida!="ok":
                            repname=input("Entrer un nom d'utilisateur (pas plus de 50 caractères) : ")
                            repmdp=input("Entrer un mot de passe (pas plus de 50 caractères) : ")
                            if not len(repname)>=50 and not len(repmdp)>=50:
                                if repmdp=="shutdown":
                                    system.shellter_main.clear()
                                    Result.version()
                                    print(colored("Le mot de passe ne peut pas être 'shutdown'","red",attrs=["bold"]))
                                elif repname in ["1","2","3","4"]:
                                    system.shellter_main.clear()
                                    Result.version()
                                    print(colored("Le nom d'utilisateur ne peut pas être 1, 2, 3, 4 ou 5","red",attrs=["bold"]))
                                elif repname.startswith("local-"):
                                    system.shellter_main.clear()
                                    Result.version()
                                    print(colored("Le nom d'utilisateur ne peut pas commencé par 'local-'","red",attrs=["bold"]))
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
                                        os.makedirs(adresseapp+"/user/"+repname+"/download")
                                        logtxt=open(adresseapp+"/logs/"+repname+".txt","w")
                                        logtxt.close()
                                        logtxt=open(adresseapp+"/user/"+repname+"/log.txt","w")
                                        logtxt.write("1")
                                        logtxt.close()
                                        open(adresseapp+"/user/"+repname+"/color.txt","w").write("white\nred\nyellow\nblue\ngreen")
                                        color=open(adresseapp+"/user/"+repname+"/color.txt","r").readlines()
                                        for z in range(len(color)):
                                            color[z]=color[z].rstrip("\n")
                                        adresse=adresse+"/user/"+repname
                                        adresseuser=adresse
                                        valida="ok"
                                    except psycopg2.errors.UniqueViolation:
                                        system.shellter_main.clear()
                                        Result.version()
                                        print(colored("Le nom d'utilisateur est déja pris","red",attrs=["bold"]))
                            else:
                                system.shellter_main.clear()
                                Result.version()
                                print(colored("Une valeur entrée n'est pas valide","red",attrs=["bold"]))
                        mdpt=repmdp
                        admin=0
                        displaysplit=0
                        logserver=1
                        charginstall=1
                        log=1
                        system.shellter_main.clear()
                        Result.version()
                        print("""Taper "help" pour plus d'information""")
                        cmd(admin,charginstall,displaysplit,logserver,repname,mdpt,adresseuser,key,log,color)
                        return
                    else:
                        system.shellter_main.clear()
                        Result.version()
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
                    color=["white","red","yellow","blue","green"]
                    key=indecode.generate_key()
                    system.shellter_main.clear()
                    Result.version()
                    print("""Taper "help" pour plus d'information""")
                    cmd(admin,charginstall,displaysplit,logserver,repname,mdpt,adresseuser,key,log,color,invit)
                    return
                elif compte=="4":
                    valida="no"
                    while valida!="ok":
                        repname=input("Entrer un nom d'utilisateur : ")
                        repname="local-"+repname
                        repmdp=input("Entrer un mot de passe : ")
                        if not len(repname)>=50 and not len(repmdp)>=50:
                            if repmdp=="shutdown":
                                system.shellter_main.clear()
                                Result.version()
                                print(colored("Le mot de passe ne peut pas être 'shutdown'","red",attrs=["bold"]))
                            elif repname in ["1","2","3","4","5"]:
                                system.shellter_main.clear()
                                Result.version()
                                print(colored("Le nom d'utilisateur ne peut pas être 1, 2, 3, 4 ou 5","red",attrs=["bold"]))
                            elif os.path.exists(adresseapp+"/user/"+repname+"/image"):
                                system.shellter_main.clear()
                                Result.version()
                                print(colored("Le nom d'utilisateur est déja utilisé","red",attrs=["bold"])) 
                            else:
                                key="local"
                                os.makedirs(adresseapp+"/user/"+repname+"/image")
                                os.makedirs(adresseapp+"/user/"+repname+"/music")
                                os.makedirs(adresseapp+"/user/"+repname+"/download")
                                open(adresseapp+"/user/"+repname+"/admin.txt","w").write("0")
                                open(adresseapp+"/user/"+repname+"/displaysplit.txt","w").write("0")
                                open(adresseapp+"/user/"+repname+"/charginstall.txt","w").write("1")
                                open(adresseapp+"/user/"+repname+"/mdp.txt","w").write(hashint.hash8192(repmdp))
                                logtxt=open(adresseapp+"/logs/"+repname+".txt","w")
                                logtxt.close()
                                logtxt=open(adresseapp+"/user/"+repname+"/log.txt","w")
                                logtxt.write("1")
                                logtxt.close()
                                open(adresseapp+"/user/"+repname+"/color.txt","w").write("white\nred\nyellow\nblue\ngreen")
                                color=open(adresseapp+"/user/"+repname+"/color.txt","r").readlines()
                                for z in range(len(color)):
                                    color[z]=color[z].rstrip("\n")
                                adresse=adresse+"/user/"+repname
                                adresseuser=adresse
                                valida="ok"
                        else:
                            system.shellter_main.clear()
                            Result.version()
                            print(colored("Une valeur entrée n'est pas valide","red",attrs=["bold"]))
                    mdpt=repmdp
                    admin=0
                    displaysplit=0
                    logserver=0
                    charginstall=1
                    log=1
                    system.shellter_main.clear()
                    Result.version()
                    print("""Taper "help" pour plus d'information""")
                    cmd(admin,charginstall,displaysplit,logserver,repname,mdpt,adresseuser,key,log,color)
                    return
                elif compte=="5":
                    system.shellter_main.clear()
                    exit()
                elif compte=="reconnect":
                    try:
                        host="ftp-cmdos.alwaysdata.net"
                        user="cmdos"
                        password="CmdOS2008)"
                        connect=FTP(host,user,password)
                        connect.sendcmd('CWD www')
                        connect.sendcmd("CWD command")
                        connsql = psycopg2.connect(user = "cmdos",password = "CmdOS2008)",host = "postgresql-cmdos.alwaysdata.net",port = "5432",database = "cmdos_user")
                        cur = connsql.cursor()
                        print(colored("La connexion a pu être établi.","blue",attrs=["bold"]))
                        online=1
                    except:
                        print(colored("La connexion n'a pas pu être établi.","yellow",attrs=["bold"]))
                        online=0
                else:
                    system.shellter_main.clear()
                    Result.version()
                    print(colored("La valeur entrée n'est pas valide","red",attrs=["bold"]))
            else:
                while True:
                    print("Selectionner une option ou taper le nom d'un compte existant sur la machine : \n 1 - Ajouter un compte existant\n 2 - Créer un compte\n 3 - Démarrer le mode invité\n 4 - Créer un compte local\n 5 - Eteindre")
                    fichiers=os.listdir(adresse+"/user")
                    longueur=len(fichiers)
                    for element in range(longueur):
                        print(" "+fichiers[element]+" - se connecter avec ce compte")
                    rep=input("Votre choix : ")
                    system.shellter_main.clear()
                    Result.version()
                    if rep=="1":
                        valida="no"
                        if system.shellter_main.connectt() and online==1:
                            while valida!="ok":
                                repname=input("Taper votre nom d'utilisateur : ")
                                repmdp=input("Taper votre mot de passe : ")
                                cur.execute("SELECT * FROM utilisateur WHERE nom='"+repname+"';")
                                repsqluser=cur.fetchall()
                                cur.execute("SELECT * FROM settings WHERE nom='"+repname+"';")
                                repsqlset=cur.fetchall()
                                if repsqluser==[]:
                                    system.shellter_main.clear()
                                    Result.version()
                                    print(colored("Le compte n'existe pas","red",attrs=["bold"]))
                                else:
                                    repsqluser=list(repsqluser[0])
                                    repsqlset=list(repsqlset[0])
                                    if repmdp==indecode.decode(repsqluser[1],repsqluser[3]):
                                        try:
                                            os.makedirs(adresseapp+"/user/"+repname+"/image")
                                            os.makedirs(adresseapp+"/user/"+repname+"/music")
                                            os.makedirs(adresseapp+"/user/"+repname+"/download")
                                            logtxt=open(adresseapp+"/logs/"+repname+".txt","w")
                                            logtxt.close()
                                            logtxt=open(adresseapp+"/user/"+repname+"/log.txt","w")
                                            logtxt.write("1")
                                            logtxt.close()
                                            adresse=adresse+"/user/"+repname
                                            adresseuser=adresse
                                            mdpt=repmdp
                                            log=1
                                            open(adresseapp+"/user/"+repname+"/color.txt","w").write("white\nred\nyellow\nblue\ngreen")
                                            color=open(adresseapp+"/user/"+repname+"/color.txt","r").readlines()
                                            for z in range(len(color)):
                                                color[z]=color[z].rstrip("\n")
                                            valida="ok"
                                        except FileExistsError:
                                            system.shellter_main.clear()
                                            Result.version()
                                            print(colored("Le compte est déja ajouté","red",attrs=["bold"]))
                                    else:
                                        system.shellter_main.clear()
                                        Result.version()
                                        print(colored("Le mot de passe n'est pas correct","red",attrs=["bold"]))
                        else:
                            system.shellter_main.clear()
                            Result.version()
                            print(colored("Vous devez être connecté à internet pour vous connecter","red",attrs=["bold"]))
                    elif rep=="2":
                        valida="no"
                        if system.shellter_main.connectt() and online==1:
                            while valida!="ok":
                                repname=input("Entrer un nom d'utilisateur (pas plus de 50 caractères) : ")
                                repmdp=input("Entrer un mot de passe (pas plus de 50 caractères) : ")
                                if not len(repname)>=50 and not len(repmdp)>=50:
                                    if repmdp=="shutdown":
                                        system.shellter_main.clear()
                                        Result.version()
                                        print(colored("Le mot de passe ne peut pas être 'shutdown'","red",attrs=["bold"]))
                                    elif repname in ["1","2","3","4","5"]:
                                        system.shellter_main.clear()
                                        Result.version()
                                        print(colored("Le nom d'utilisateur ne peut pas être 1, 2, 3, 4 ou 5","red",attrs=["bold"]))
                                    elif repname.startswith("local-"):
                                        system.shellter_main.clear()
                                        Result.version()
                                        print(colored("Le nom d'utilisateur ne peut pas commencé par 'local-'","red",attrs=["bold"]))
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
                                            os.makedirs(adresseapp+"/user/"+repname+"/download")
                                            logtxt=open(adresseapp+"/logs/"+repname+".txt","w")
                                            logtxt.close()
                                            logtxt=open(adresseapp+"/user/"+repname+"/log.txt","w")
                                            logtxt.write("1")
                                            logtxt.close()
                                            log=1
                                            adresse=adresse+"/user/"+repname
                                            adresseuser=adresse
                                            mdpt=repmdp
                                            cur.execute("SELECT * FROM utilisateur WHERE nom='"+repname+"';")
                                            repsqluser=cur.fetchall()
                                            cur.execute("SELECT * FROM settings WHERE nom='"+repname+"';")
                                            repsqlset=cur.fetchall()
                                            repsqluser=list(repsqluser[0])
                                            repsqlset=list(repsqlset[0])
                                            open(adresseapp+"/user/"+repname+"/color.txt","w").write("white\nred\nyellow\nblue\ngreen")
                                            color=open(adresseapp+"/user/"+repname+"/color.txt","r").readlines()
                                            for z in range(len(color)):
                                                color[z]=color[z].rstrip("\n")
                                            valida="ok"
                                        except psycopg2.errors.UniqueViolation:
                                            system.shellter_main.clear()
                                            Result.version()
                                            print(colored("Le nom d'utilisateur est déja pris","red",attrs=["bold"]))
                                else:
                                    system.shellter_main.clear()
                                    Result.version()
                                    print(colored("Une valeur entrée n'est pas valide","red",attrs=["bold"]))
                        else:
                            system.shellter_main.clear()
                            Result.version()
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
                        color=["white","red","yellow","blue","greeb"]
                        key=indecode.generate_key()
                        system.shellter_main.clear()
                        Result.version()
                        print("""Taper "help" pour plus d'information""")
                        cmd(admin,charginstall,displaysplit,logserver,repname,mdpt,adresseuser,key,log,color,invit)
                        return
                    elif rep=="4":
                        valida="no"
                        while valida!="ok":
                            repname=input("Entrer un nom d'utilisateur : ")
                            repname="local-"+repname
                            repmdp=input("Entrer un mot de passe : ")
                            if not len(repname)>=50 and not len(repmdp)>=50:
                                if repmdp=="shutdown":
                                    system.shellter_main.clear()
                                    Result.version()
                                    print(colored("Le mot de passe ne peut pas être 'shutdown'","red",attrs=["bold"]))
                                elif repname in ["1","2","3","4","5"]:
                                    system.shellter_main.clear()
                                    Result.version()
                                    print(colored("Le nom d'utilisateur ne peut pas être 1, 2, 3, 4 ou 5","red",attrs=["bold"]))
                                elif os.path.exists(adresseapp+"/user/"+repname+"/image"):
                                    system.shellter_main.clear()
                                    Result.version()
                                    print(colored("Le nom d'utilisateur est déja utilisé","red",attrs=["bold"])) 
                                else:
                                    key="local"
                                    os.makedirs(adresseapp+"/user/"+repname+"/image")
                                    os.makedirs(adresseapp+"/user/"+repname+"/music")
                                    os.makedirs(adresseapp+"/user/"+repname+"/download")
                                    open(adresseapp+"/user/"+repname+"/admin.txt","w").write("0")
                                    open(adresseapp+"/user/"+repname+"/displaysplit.txt","w").write("0")
                                    open(adresseapp+"/user/"+repname+"/charginstall.txt","w").write("1")
                                    open(adresseapp+"/user/"+repname+"/mdp.txt","w").write(hashint.hash8192(repmdp))
                                    logtxt=open(adresseapp+"/logs/"+repname+".txt","w")
                                    logtxt.close()
                                    logtxt=open(adresseapp+"/user/"+repname+"/log.txt","w")
                                    logtxt.write("1")
                                    logtxt.close()
                                    open(adresseapp+"/user/"+repname+"/color.txt","w").write("white\nred\nyellow\nblue\ngreen")
                                    color=open(adresseapp+"/user/"+repname+"/color.txt","r").readlines()
                                    for z in range(len(color)):
                                        color[z]=color[z].rstrip("\n")
                                    adresse=adresse+"/user/"+repname
                                    adresseuser=adresse
                                    valida="ok"
                            else:
                                system.shellter_main.clear()
                                Result.version()
                                print(colored("Une valeur entrée n'est pas valide","red",attrs=["bold"]))
                        mdpt=repmdp
                        admin=0
                        displaysplit=0
                        logserver=0
                        charginstall=1
                        log=1
                        system.shellter_main.clear()
                        Result.version()
                        print("""Taper "help" pour plus d'information""")
                        cmd(admin,charginstall,displaysplit,logserver,repname,mdpt,adresseuser,key,log,color)
                        return
                    elif rep=="5":
                        system.shellter_main.clear()
                        exit()
                    elif rep=="reconnect":
                        try:
                            host="ftp-cmdos.alwaysdata.net"
                            user="cmdos"
                            password="CmdOS2008)"
                            connect=FTP(host,user,password)
                            connect.sendcmd('CWD www')
                            connect.sendcmd("CWD command")
                            connsql = psycopg2.connect(user = "cmdos",password = "CmdOS2008)",host = "postgresql-cmdos.alwaysdata.net",port = "5432",database = "cmdos_user")
                            cur = connsql.cursor()
                            print(colored("La connexion a pu être établi.","blue",attrs=["bold"]))
                            online=1
                        except:
                            print(colored("La connexion n'a pas pu être établi.","yellow",attrs=["bold"]))
                            online=0
                    elif rep in fichiers:
                        valida="no"
                        while valida!="ok":
                            repname=rep
                            print(colored("Taper shutdown pour éteindre"))
                            repmdp=input("Taper votre mot de passe : ")
                            if not repmdp=="shutdown":
                                if not repname.startswith("local-") and system.shellter_main.connectt() and online==1:
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
                                        logtxt=open(adresseapp+"/user/"+repname+"/log.txt")
                                        data=logtxt.readlines()
                                        data=data[0]
                                        log=int(data)
                                        logtxt.close()
                                        valida="ok"
                                        color=open(adresseapp+"/user/"+repname+"/color.txt","r").readlines()
                                        for z in range(len(color)):
                                            color[z]=color[z].rstrip("\n")
                                        break
                                    else:
                                        system.shellter_main.clear()
                                        Result.version()
                                        print(colored("Le mot de passe n'est pas correct","red",attrs=["bold"]))
                                elif repname.startswith("local-"):
                                    repsqluser=[repname,repmdp,int(open(adresseapp+"/user/"+repname+"/admin.txt","r").readlines()[0]),"local"]
                                    repsqlset=[repname,open(adresseapp+"/user/"+repname+"/displaysplit.txt","r").readlines()[0],open(adresseapp+"/user/"+repname+"/charginstall.txt","r").readlines()[0],0]
                                    if hashint.hash8192(repmdp)==open(adresseapp+"/user/"+repname+"/mdp.txt","r").readlines()[0]:
                                        mdpt=repmdp
                                        adresse=adresse+"/user/"+repname
                                        adresseuser=adresse
                                        logtxt=open(adresseapp+"/user/"+repname+"/log.txt")
                                        data=logtxt.readlines()
                                        data=data[0]
                                        log=int(data)
                                        logtxt.close()
                                        valida="ok"
                                        color=open(adresseapp+"/user/"+repname+"/color.txt","r").readlines()
                                        for z in range(len(color)):
                                            color[z]=color[z].rstrip("\n")
                                        break
                                    else:
                                        system.shellter_main.clear()
                                        Result.version()
                                        print(colored("Le mot de passe n'est pas correct","red",attrs=["bold"]))
                                else:
                                    system.shellter_main.clear()
                                    Result.version()
                                    print(colored("Vous devez être connecté à internet pour vous connecter ou il n'existe de compte local de ce nom","red",attrs=["bold"]))
                                    break
                            else:
                                return
                    else:
                        system.shellter_main.clear()
                        Result.version()
                        print(colored("La valeur entrée n'est pas valide","red",attrs=["bold"]))
                    if valida=="ok":
                        admin=repsqluser[2]
                        displaysplit=repsqlset[1]
                        logserver=repsqlset[3]
                        charginstall=repsqlset[2]
                        key=repsqluser[3]
                        system.shellter_main.clear()
                        Result.version()
                        print("""Taper "help" pour plus d'information""")
                        a=0
                        cmd(admin,charginstall,displaysplit,logserver,repname,mdpt,adresseuser,key,log,color)
                        return
    elif invit==2:
        mdpt=0
        admin=0
        displaysplit=0
        logserver=0
        charginstall=0
        invit=1
        repname="Guest"
        log=0
        color=["white","red","yellow","blue","green"]
        adresseuser=adresse
        key=indecode.generate_key()
        system.shellter_main.clear()
        Result.version()
        print("Mode invité activé au démarrage")
        print("""Taper "help" pour plus d'information""")
        cmd(admin,charginstall,displaysplit,logserver,repname,mdpt,adresseuser,key,log,color,invit)
while True :
    login()
    if a==1:
        a=0
        adresse=os.path.realpath(__file__)
        adresse=os.path.dirname(adresse)
        login()
    else:
        break
try:
    connect.quit()
    cur.close()
    connsql.close()
except:
    pass
system.shellter_main.clear()