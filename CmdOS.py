#####################################################################
#Import
####################################################################
from genericpath import exists
#from msvcrt import open_osfhandle
from os import listdir
from os.path import isfile, join
import os.path
import os
from random import random
from xml.sax.xmlreader import AttributesImpl
from termcolor import colored
import getpass
import requests as req
import time
import cmd_fonction as cmdf
from datetime import datetime
from ftplib import FTP
import uuid
os.system("clear")
####################################################################
#Dico commande and app plus chargement
####################################################################
admin=0
cmdf.charg()
mdpt="6"
com={"help":"Voici la liste des commandes de Cmd OS :""\nhelp - Afficher la liste des commandes"
     "\ninfo - Afficher les infos sur un programme / Utliser sys pour voir la version du système"
     "\nstore - Affiche les différentes applications installables : \n   install - installer un module \n   uninstall - desinstaller un module""\n   list - affiche les différents modules installés"
     "\ncd - changer de dossier""\ndir - permet de voir les fichiers/dossiers"
     "\nopendir - ouvrir un dossier"
     "\nmdp - Voir si le mot de passe est actif ou non :\n   act - active le mot de passe\n   disact - desactive le mot de passe"
     "\nren - renomer un fichier"
     "\nupdate :""\n   upgrade - mettre à jour le système en téléchargant la dernière version""\n   check - vérifier si une nouvelle mise à jour est disponible"
     "\nadmin - active ou désactive le mode admin"
     "\nlog - affiche les logs (il faut être connecté en tant qu'administrateur pour utiliser cette commande)""\n   show - affiche les logs""\n   delete - supprime les logs"
     "\ndetail - affiche les propriétés d'un fichier ou dossier sous forme de os.stat_result"
     "\nshell (version raccourci : sh) - ouvre le cmd"}
app={"random":"0",
     "time":"0",
     "music":"0",
     "uuid":"0",
     "image":"0",
     "browser":"0",
     "print":"0",
     "maths":"0",
     "download":"0"}
def appinitext():
    if not os.path.exists("/home/pi/Documents/CmdOS/random.txt"):
        randomtext=open("random.txt","w")
        randomtext.write(app["random"])
        randomtext.close()
    else:
        import random
        randomtext=open("random.txt",'r')
        data=randomtext.readlines()
        app.update({"random":str(data[0])})
        randomtext.close()
    if not os.path.exists("/home/pi/Documents/CmdOS/time.txt"):
        timetext=open("time.txt","w")
        timetext.write(app["time"])
        timetext.close()
    else:
        import time
        timetext=open("time.txt",'r')
        data=timetext.readlines()
        app.update({"time":str(data[0])})
        timetext.close()
    if not os.path.exists("/home/pi/Documents/CmdOS/music.txt"):
        musictext=open("music.txt","w")
        musictext.write(app["music"])
        musictext.close()
    else:
        import simpleaudio as sa
        musictext=open("music.txt",'r')
        data=musictext.readlines()
        app.update({"music":str(data[0])})
        musictext.close()
    if not os.path.exists("uuid.txt"):
        uuidtext=open("uuid.txt","w")
        uuidtext.write(app["uuid"])
        uuidtext.close()
    else:
        import uuid
        import random
        uuidtext=open("uuid.txt",'r')
        data=uuidtext.readlines()
        app.update({"uuid":str(data[0])})
        uuidtext.close()
    if not os.path.exists("image.txt"):
        imagetext=open("image.txt","w")
        imagetext.write(app["image"])
        imagetext.close()
    else:
        from PIL import Image
        imagetext=open("image.txt",'r')
        data=imagetext.readlines()
        app.update({"image":str(data[0])})
        imagetext.close()
    if not os.path.exists("browser.txt"):
        browsertext=open("browser.txt","w")
        browsertext.write(app["browser"])
        browsertext.close()
    else:
        import webbrowser
        browsertext=open("browser.txt",'r')
        data=browsertext.readlines()
        app.update({"browser":str(data[0])})
        browsertext.close()
    if not os.path.exists("print.txt"):
        printtext=open("print.txt","w")
        printtext.write(app["print"])
        printtext.close()
    else:
        printtext=open("print.txt",'r')
        data=printtext.readlines()
        app.update({"print":str(data[0])})
        printtext.close()
    if not os.path.exists("maths.txt"):
        mathstext=open("maths.txt","w")
        mathstext.write(app["maths"])
        mathstext.close()
    else:
        mathstext=open("maths.txt",'r')
        data=mathstext.readlines()
        app.update({"maths":str(data[0])})
        mathstext.close()
    if not os.path.exists("download.txt"):
        downloadtext=open("download.txt","w")
        downloadtext.write(app["download"])
        downloadtext.close()
    else:
        downloadtext=open("download.txt",'r')
        data=downloadtext.readlines()
        app.update({"download":str(data[0])})
        downloadtext.close()
appinitext()
info={"sys":"Cmd OS v1.19 - Basé en Python",
      "system":"Cmd OS v1.19 - Basé en Python",
      "time":"Module Time""\nVersion : 1.0""\nAuteur : système",
      "random":"Module Random""\nVersion : 1.1""\nAuteur : système",
      "music":"Module Music""\nVersion : 1.1""\nAuteur : système""\nNote : basé avec le module simpleaudio",
      "uuid":"Module Uuid""\nVersion : 1.0""\nAuteur : système""\nNote : basé avec le module uuid4",
      "image":"Module Image""\nVersion : 1.0""\nAuteur : système""\nNote : basé avec le module PIL",
      "browser":"Module Browser""\nVersion : 1.0""\nAuteur : système""\nNote : basé avec le module browser",
      "print":"Module Print""\nVersion : 1.0""\nAuteur : système""\nNote : basé avec le module termcolor",
      "maths":"Module Maths""\nVersion : 1.1""\nAuteur : système",
      "download":"Module Download""\nVersion : 1.0""\nAuteur : système""\nNote : basé sur le module request"} 
adresse=os.path.realpath(__file__)
adresse=os.path.dirname(adresse)
if not os.path.exists(adresse)==True:
    while not os.path.exists(adresse)==True:
        adresse=input("Le système n'a pas démmarrer correctement, veulliez rentrer le chemin absolu du dossier ou se trouve le fichier CmdOS.py : ")
if not(os.path.exists(adresse+"/image") and os.path.exists(adresse+"/music") and os.path.exists(adresse+"/README.md") and os.path.exists(adresse+"/gif") and os.path.exists(adresse+"/__pycache__")):
    print(colored("Le système ne peut pas fonctionner dans son intégrité car certain dosssier/fichier ne sont pas présents.\nVeulliez vous assurez que les dossier suivant existe: image, music, __pycache__, gif et README.md.","red",attrs=["bold"]))
    quit()
if not os.path.exists(adresse+"/mdp.txt"):
    mdptext=open("mdp.txt","w")
    mdptext.write(mdpt)
    mdptext.close()
else:
    mdptext=open("mdp.txt",'r')
    data=mdptext.readlines()
    mdpt=data[0]
    mdptext.close()
repmdp=""
print(colored("""Cmd OS v1.19""","green",attrs=["bold"])) 
host="ftp-cmdos.alwaysdata.net"
user="cmdos"
password="CmdOS2008)"
connect=FTP(host,user,password)
connect.sendcmd('CWD www')
connect.sendcmd("CWD command")
def cmd():
    global adresse,mdpt,app,mdptext,repmdp,admin
    log=["Voici les logs :"]
    charginstall=1
    displaysplit=0
    logserver=1
    store="store"+"Bienvenue dans le store de Cmd OS, voici les modules disponibles :"+"\nrandom - générer un nombre aléatoire"+"\ntime - attendre un temps"+"\nmusic - permet de jouer un son"+"\nuuid - générer des identifiants aléatoire"+"\nimage - permet d'afficher une image"+"\nbrowser - permet d'afficher une page web"+"\nprint - permet d'afficher du texte en couleur dans la console"+"\ndownload - permet de télécharger une page web"+"\nPour installer un module, faites <<store install>> suivie du nom du module"+"\nPour desinstaller un module, faites <<store uninstall>> suivie du nom du module"+"\nPour voir la liste des modules installés faites <<store list>>"
    while True:
        version="1.19"
        if app["random"]=="1":
            import random
        if app["time"]=="1":
            import time
        if app["music"]=="1":
            import simpleaudio as sa
        if app["uuid"]=="1":
            import random
            import uuid
        if app["image"]=="1":
            from PIL import Image
        if app["browser"]=="1":
            import webbrowser
        if admin==0:
            demande=colored(getpass.getuser(),"green",attrs=["bold"])+" "+colored(adresse,"blue",attrs=["bold"])+" >>> "
        else:
            demande=colored(getpass.getuser(),"green",attrs=["bold"])+colored("(admin)","red",attrs=["bold"])+" "+colored(adresse,"blue",attrs=["bold"])+" >>> "
        rep=input(demande)
        if admin==1:
            heure=str(datetime.now())
            if logserver==1:
                id=str(uuid.uuid4())
                contenttxt=open("content.txt","w")
                contenttxt.write(getpass.getuser()+"(admin) "+heure+" "+rep)
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
                id=str(uuid.uuid4())
                contenttxt=open("content.txt","w")
                contenttxt.write(getpass.getuser()+" "+heure+" "+rep)
                contenttxt.close()
                contenttxt=open("content.txt","rb")
                connect.storbinary("STOR "+id,contenttxt)
                contenttxt.close()
                log.append(id+" "+colored(getpass.getuser(),"green",attrs=["bold"])+" "+colored(heure,"blue",attrs=["bold"])+" "+rep)
            else:
                log.append(colored(getpass.getuser(),"green",attrs=["bold"])+" "+colored(heure,"blue",attrs=["bold"])+" "+rep)
        if rep in com:
            print(com[rep])
        elif rep=="store":
            print(store)
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
        elif rep=="uuid":
            if app.get("uuid")=="1":
                uuid.uuid4()
                while True:
                    id=str(uuid.uuid4())
                    trimmed=id[:random.randint(0,len(id)-1)]
                    spaces=" " * random.randint(0,15)
                    print(f"{spaces}{trimmed}")
            else:
                print(colored("Ce module n'est pas installé ou n'existe pas","red",attrs=["bold"]))
        elif rep.startswith("download"):
            download=rep.split()
            if displaysplit==1:
                print(download)
            if app["download"]=="1":
                if len(download)==3:
                    urldown=download[1]
                    lentxt=len(download[2])-5
                    txtname=download[2]
                    if txtname[lentxt::]==".html":
                        try:
                            txtcontent=req.get(urldown,allow_redirects=True)
                            open(txtname,"wb").write(txtcontent.content)
                            txtfile=open(txtname,"r")
                            txtlist=txtfile.readlines()
                            txtfile.close()
                            print(colored(("La page web a bien été enregistré sous le nom "+txtname),"blue",attrs=["bold"]))
                        except req.exceptions.MissingSchema:
                            print(colored("La page web n'existe pas","yellow",attrs=["bold"]))
                    else:
                        print(colored("Le nom de fichier doit terminé par '.html'","red",attrs=["bold"]))
                else:
                    print(colored("La commande n'est pas bien formulée","red",attrs=["bold"]))
            else:
                print(colored("Ce module n'est pas installé ou n'existe pas","red",attrs=["bold"]))
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
        elif rep=="dir":
            fichiers = os.listdir(adresse)
            longueur=len(fichiers)
            print("Voici les fichiers/dossiers dans ce dossier :")
            for element in range(longueur):
                print(" ",fichiers[element])
        elif rep.startswith("store install "):
            install=rep[14::]
            if install in app: 
                app.update({install:"1"})
                if charginstall==1:
                    cmdf.charg(0.3,colored("Installation du module...","blue",attrs=["bold"]))
                install2=colored("Le module ","blue",attrs=["bold"])+colored(install,"blue",attrs=["bold","underline"])+colored(" a bien été installé","blue",attrs=["bold"])
                print(install2)
                if install=="random":
                    import random
                    appt=open("random.txt","w")
                    appt.write(app.get("random"))
                    appt.close()
                if install=="time":
                    import time
                    appt=open("time.txt","w")
                    appt.write(app.get("time"))
                    appt.close()
                if install=="music":
                    import simpleaudio as sa
                    appt=open("music.txt","w")
                    appt.write(app.get("music"))
                    appt.close()
                if install=="uuid":
                    import uuid
                    import random
                    appt=open("uuid.txt","w")
                    appt.write(app.get("uuid"))
                    appt.close()
                if install=="image":
                    from PIL import Image
                    appt=open("image.txt","w")
                    appt.write(app.get("image"))
                    appt.close()
                if install=="browser":
                    import webbrowser
                    appt=open("browser.txt","w")
                    appt.write(app.get("browser"))
                    appt.close()
                if install=="print":
                    appt=open("print.txt","w")
                    appt.write(app.get("print"))
                    appt.close()
                if install=="maths":
                    appt=open("maths.txt","w")
                    appt.write(app.get("maths"))
                    appt.close()
                if install=="download":
                    appt=open("download.txt","w")
                    appt.write(app.get("download"))
                    appt.close()
            else:
                print(colored("L'app que vous essayez d'installer n'existe pas","red",attrs=["bold"]))
        elif rep.startswith("random"):
            if app.get("random")=="1":
                    error=0
                    aleatoire=rep.split()
                    if displaysplit==1:
                        print(aleatoire)
                    try:
                        aleatoire[1]=int(aleatoire[1])
                        aleatoire[2]=int(aleatoire[2])
                    except:
                        print(colored("La commande n'accepte que des nombres","yellow",attrs=["bold"]))
                        error=1
                    if len(aleatoire)==3 and type(aleatoire[1])==int and type(aleatoire[2]==int):
                        random_1=aleatoire[1]
                        random_2=aleatoire[2]
                        print("Le nombre est",random.randint(random_1,random_2))
                    else:
                        if error==0:
                            print(colored("La commande est mal formulée","red",attrs=["bold"]))
                    error=0
            else:
                print(colored("Ce module n'est pas installé ou n'est pas bien formulé","red",attrs=["bold"]))
        elif rep.startswith("time"):
            if app.get("time")=="1":
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
            else:
                print(colored("Ce module n'est pas installé ou n'est pas bien formulé","red",attrs=["bold"]))
            error=0
        elif rep=="shutdown" or rep=="sh" or rep=="shell":
            break
        elif rep.startswith("info"):
            info_command=rep.split()
            if displaysplit==1:
                print(info_command)
            if len(info_command)==2:
                if info_command[1] in info:
                    print(info[info_command[1]])
                else:
                    print(colored("Le module n'existe pas","yellow",attrs=["bold"]))
            else:
                print(colored("La commande est mal formulé","red",attrs=["bold"]))
        elif rep.startswith("store uninstall "):
            uninstall=rep[16::]
            if uninstall in app:
                if app.get(uninstall)=="1":
                    app.update({uninstall:"0"})
                    uninstall1=colored("Le module ","blue",attrs=["bold"])+colored(uninstall,"blue",attrs=["bold","underline"])+colored(" a bien été desinstallé","blue",attrs=["bold"])
                    print(uninstall1)
                    if uninstall=="random":
                        appt=open("random.txt","w")
                        appt.write(app.get("random"))
                        appt.close()
                    if uninstall=="time":
                        appt=open("time.txt","w")
                        appt.write(app.get("time"))
                        appt.close()
                    if uninstall=="music":
                        appt=open("music.txt","w")
                        appt.write(app.get("music"))
                        appt.close()
                    if uninstall=="uuid":
                        appt=open("uuid.txt","w")
                        appt.write(app.get("uuid"))
                        appt.close()
                    if uninstall=="image":
                        appt=open("image.txt","w")
                        appt.write(str(app.get("image")))
                        appt.close()
                    if uninstall=="browser":
                        appt=open("browser.txt","w")
                        appt.write(str(app.get("browser")))
                        appt.close()
                    if uninstall=="print":
                        appt=open("print.txt","w")
                        appt.write(str(app.get("print")))
                        appt.close()
                    if uninstall=="maths":
                        appt=open("maths.txt","w")
                        appt.write(str(app.get("maths")))
                        appt.close()
                    if uninstall=="download":
                        appt=open("download.txt","w")
                        appt.write(str(app.get("download")))
                        appt.close()
                else:
                    print(colored("L'app que vous essayez de désinstaller n'est pas installée","yellow",attrs=["bold"]))
            else:
                print(colored("L'app que vous voulez desinstaller n'existe pas","yellow",attrs=["bold"]))
        elif rep.startswith("music"):
            if app.get("music")=="1":
                    error=0
                    music=rep.split()
                    if displaysplit==1:
                        print(music)
                    if music[1]=="store":
                        print("Voici votre musique :")
                        fichiers = os.listdir(adresse+"/music")
                        longueur=len(fichiers)
                        for element in range(longueur):
                            print(" ",fichiers[element])
                    if len(music)==3:
                        if music[1]=="play":
                            fichiers = os.listdir(adresse+"/music")
                            musicplay=rep[11::]
                            if musicplay in fichiers:
                                musicd=adresse+"/music"/+musicplay
                                wave_object = sa.WaveObject.from_wave_file(musicd)
                                print(colored("Le son suivant va être lu : ","blue",attrs=["bold"]))
                                play_object = wave_object.play()
                            else:
                                print(colored("Ce fichier n'existe pas","yellow",attrs=["bold"]))
                        else:
                            print(colored("La commande est mal formulée","red",attrs=["bold"]))
            else:
                print(colored("Ce module n'est pas installé ou n'est pas bien formulé","red",attrs=["bold"]))
        elif rep.startswith("image"):
            if app.get("image")=="1":
                    error=0
                    image=rep.split()
                    if displaysplit==1:
                        print(image)
                    if image[1]=="store":
                        print("Voici votre phototèque :")
                        fichiers = os.listdir(adresse+"/image")
                        longueur=len(fichiers)
                        for element in range(longueur):
                            print(" ",fichiers[element])
                    if len(image)==3:
                        if image[1]=="display":
                            fichiers = os.listdir(adresse+"/image")
                            imgaffich=rep[14::]
                            print(imgaffich)
                            if imgaffich in fichiers:
                                imgd=adresse+"/image/"+imgaffich
                                im = Image.open(imgd)
                                im.show()
                            else:
                                print(colored("Ce fichier n'existe pas","yellow",attrs=["bold"]))
                        else:
                            print(colored("La commande est mal formulé","red",attrs=["bold"]))
            else:
                print(colored("Ce module n'est pas installé ou n'est pas bien formulé","red",attrs=["bold"]))
        elif rep.startswith("mdp"):
            mdp=rep.split()
            if displaysplit==1:
                print(mdp)
            if len(mdp)==1:
                if not mdpt=="6":
                    mdpdise="Le mot de passe est :"+mdpt
                    print(colored(mdpdise,"blue",attrs=["bold"]))
                else:
                    print(colored("Le mot de passe est désactivé","blue",attrs=["bold"]))
            elif len(mdp)==2:
                if type(mdp[1])==str:
                    if mdp[1]=="act":
                        if mdpt=="6":
                            mdpt=input("Taper votre nouveau mot de passe : ")
                            mdptext=open("mdp.txt","w")
                            mdptext.write(mdpt)
                            mdptext.close()
                        else:
                            print(colored("Le mot de passe est déja activé","yellow",attrs=["bold"]))
                    elif mdp[1]=="disact":
                        if not mdpt=="6":
                            print(colored("Le mot de passe a bien été désactivé","blue",attrs=["bold"]))
                            mdpt="6"
                            mdptext=open("mdp.txt","w")
                            mdptext.write(mdpt)
                            mdptext.close()
                        else:
                            print(colored("Le mot de passe est déja desactivé","yellow",attrs=["bold"]))
                else:
                    print(colored("La commande n'est pas bien formulée","red",attrs=["bold"]))
            else:
                print(colored("La commande n'est pas bien formulée","red",attrs=["bold"]))
        elif rep.startswith("browser"):
            if app.get("browser")=="1":
                browser=rep[8::]
                if type(browser)==str:
                    webbrowser.open(browser)
                else:
                    print(colored("L'URl n'est pas bonne","red"))
            else:
                print(colored("Ce module n'est pas installé ou n'est pas bien formulé","red",attrs=["bold"]))
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
        elif rep.startswith("print"):
            error=0
            if app.get("print")=="1":
                if len(rep)>=9:
                    colorp={"b":"blue","g":"green","r":"red","w":"white","y":"yellow","m":"magenta","c":"cyan"}
                    if rep[6] in colorp:
                        colorprint=colorp.get(rep[6])
                    else:
                        print(colored("Cette couleur n'est pas prise en charge","red",attrs=["bold"]))
                        error=1
                    print1=rep[8::]
                    if error==0:
                        print(colored(print1,colorprint))
                else:
                    print(colored("La commande est mal formulée","red",attrs=["bold"]))
            else:
                print(colored("Ce module n'est pas installé ou n'est pas bien formulé","red",attrs=["bold"]))
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
        elif rep=="clear":
            os.system("clear")
        elif rep.startswith("maths"):
            if app.get("maths")=="1":
                maths1=rep.split()
                if displaysplit==1:
                    print(maths1)
                if len(maths1)==4:
                    op=["+","-","*","/","%","p"]
                    op1=maths1[2]
                    if op1 in op:
                        try:
                            terme1=float(maths1[1])
                            terme2=float(maths1[3])
                            if op1=="+":
                                result=terme1+terme2
                                print(terme1,op1,terme2,"=",result)
                            if op1=="-":
                                result=terme1-terme2
                                print(terme1,op1,terme2,"=",result)
                            if op1=="*":
                                result=terme1*terme2
                                print(terme1,op1,terme2,"=",result)
                            if op1=="/":
                                result=terme1/terme2
                                print(terme1,op1,terme2,"=",result)
                            if op1=="%":
                                result=terme1%terme2
                                print(terme1,op1,terme2,"=",result)
                            if op1=="p":
                                result=pow(terme1,terme2)
                                print(result)
                        except:
                            print(colored("L'un des termes/facteurs n'est pas valide","red",attrs=["bold"]))
                    else:
                        print(colored("Cet opérateur n'est pas prise en charge ou n'existe pas","red",attrs=["bold"]))
                else:
                    print(colored("La commande est mal formulée","red",attrs=["bold"]))
            else:
                print(colored("Ce module n'est pas installé ou n'est pas bien formulé","red",attrs=["bold"]))
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
                    else:
                        print(colored("La commande est mal formulée","red",attrs=["bold"]))
                else:
                    print(colored("La commande est mal formulée","red",attrs=["bold"]))
            else:
                print(colored("Vous devez être connecté en tant qu'administrateur pour utiliser cette commande","red",attrs=["bold"]))
        else:
            if not rep=="":
                print(rep,": cette commande n'existe pas : essayer help")
def login():
    if not mdpt=="6":
        print("Taper",colored("shutdown",attrs=["bold"]),"pour éteindre")
        repmdp=input("Taper votre mot de passe : ")
        if repmdp==mdpt:
            os.system("clear")
            print(colored("""Cmd OS v1.18""","green",attrs=["bold"])) 
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