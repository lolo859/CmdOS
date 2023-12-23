import system.shellter_core
def display():
    print("[SHELLTER.DISPLAY] : Start booting Shellter's display core...")
    print("[SHELLTER.DISPLAY] : Importing termcolor, os and sys...")
    import os,sys
    from termcolor import colored
    print("[SHELLTER.DISPLAY] : Create clear() function...")
    print("[SHELLTER.DISPLAY] : Create Result class...")
    class Result():
        def __init__(self,text,rt,module=None,object=None):
            self.resultType=rt
            self.module=module
            self.text=text
            self.object=object
        def print(self,id,adresse,color):
            ResultType=["error","stdout","notfound","advert","important","version"]
            if self.resultType in ResultType:
                if self.resultType=="error":
                    system.shellter_core.check_cpu(id,adresse)
                    print(colored((self.module+" : "+self.text),color[1],attrs=["bold"]))
                if self.resultType=="stdout":
                    system.shellter_core.check_cpu(id,adresse)
                    print(colored(self.text,color[0]))
                if self.resultType=="notfound":
                    system.shellter_core.check_cpu(id,adresse)
                    texte=self.module+" : L'élément '"+self.object+"' n'existe pas, n'a pas pu être trouvé ou n'est pas du type attendu"
                    print(colored(texte,color[2],attrs=["bold"]))
                if self.resultType=="advert":
                    system.shellter_core.check_cpu(id,adresse)
                    print(colored(self.text,color[2],attrs=["bold"]))
                if self.resultType=="important":
                    system.shellter_core.check_cpu(id,adresse)
                    print(colored(self.text,color[3],attrs=["bold"]))
        def version(color=["white","red","yellow","blue","green"]):
            version="3.0"
            print(colored(("CmdOS v"+version),color[4],attrs=["bold"]))
    print("[SHELLTER.DISPLAY] : Shellter's display core fully booted")
    return Result
def clear():
    import sys,os
    if str(sys.platform).startswith("win"):
        os.system("cls")
    else:
        os.system("clear")
def connection():
    print("[SHELLTER.CONNECTION] : Start booting Shellter's connectivity core...")
    print("[SHELLTER.CONNECTION] : Importing psycopg2, requests and ftplib...")
    import requests
    import psycopg2
    from ftplib import FTP
    print("[SHELLTER.CONNECTION] : Etablishing connection with the ftp and postgresql server...")
    try:
        host="ftp-cmdos.alwaysdata.net"
        user="cmdos"
        password="CmdOS2008)"
        connect=FTP(host,user,password)
        connect.sendcmd('CWD www')
        connect.sendcmd("CWD command")
        connsql = psycopg2.connect(user = "cmdos",password = "CmdOS2008)",host = "postgresql-cmdos.alwaysdata.net",port = "5432",database = "cmdos_user")
        cur = connsql.cursor()
        online=1
    except:
        print("[SHELLTER.CONNECTION] : Error when trying to connect : check your internet connection, firewall or try to change connection")
        online=0
        connect=None
        cur=None
        connsql=None
    print("[SHELLTER.CONNECTION] : Connection etablish")
    print("[SHELLTER.CONNECTION] : Create connect() function...")
    print("[SHELLTER.CONNECTION] : Shellter's connection core fully booted")
    return connect,cur,connsql,online
def connectt():
    try:
        import requests
        requests.get("https://www.google.com",allow_redirects=True)
        return True
    except:
        return False
def main():
    print("[SHELLTER.MAIN] : Start booting Shellter's main core...")
    print("[SHELLTER.MAIN] : Importing os, termcolor, psutil, platform...")
    import os
    from termcolor import colored
    import platform
    import psutil
    print("[SHELLTER.MAIN] : Checking boot's option...")
    if "invit.txt" in os.listdir(os.getcwd()+"/system"):
        invit=2
    else:
        invit=0
    print("[SHELLTER.MAIN] : Checking main os...")
    print("[SHELLTER.MAIN] : Shellter is running on "+str(platform.platform()))
    print("[SHELLTER.MAIN] : Checking processor...")
    print("[SHELLTER.MAIN] : Shellter is running on "+str(platform.processor()))
    print("[SHELLTER.MAIN] : Checking RAM...")
    if psutil.virtual_memory().total/1024/1024>=200:
        print("[SHELLTER.MAIN] : Ram on this computer : "+str(psutil.virtual_memory().total/1024/1024)+" MB")
    else:
        print("[SHELLTER.MAIN] : Please add RAM, CmdOS need at least 200 MB")
    connect,cur,connsql,online=connection()
    Result=display()
    print("[SHELLTER.MAIN] : Setting variables...")
    a=0
    help="Voici la liste des commandes de CmdOS :"+"\nhelp - Afficher la liste des commandes :\n   help <commande>"+"\nstore - Affiche les différents modules installables : \n   install <module> - installer un module \n   uninstall <module> - desinstaller un module""\n   list - affiche les différents modules installés""\n   info <module> - affiche les informations du module"+"\ncd - changer de dossier :\n   cd <chemin absolu>\n   cd <dossier à ouvrir>\n   cd .. : ouvre le dossier parent"+"\ndir - permet de voir les fichiers/dossiers"+"\nsys account - Voir vos identifiants :\n   name - modifie votre nom d'utilisateur\n   password - modifie votre mot de passe\n   disconnect - déconnecte votre compte de l'appareil\n   delete - supprime totalement votre compte\n   reset - change votre clé de cryptage"+"\nren - renomer un fichier"+"\ndel - supprimer un fichier / dossier"+"\nsys update :""\n   upgrade - mettre à jour le système en téléchargant la dernière version""\n   check - vérifier si une nouvelle mise à jour est disponible"+"\nadmin on/off - active ou désactive le mode admin"+"\nlog - affiche l'état des logs (il faut être connecté en tant qu'administrateur pour utiliser cette commande)""\n   enable - active les logs""\n   disable - désactive les logs""\n   delete - supprime les logs"+"\ndetail - affiche les propriétés d'un fichier ou dossier sous forme de os.stat_result"+"\nshell (version raccourci : sh) - ferme CmdOS"+"\nunlog - déconnecte l'utilisateur"+"\nmkdir - crée un dossier"+"\nmove - déplacer un dossier ou un fichier"+"\ncat - afficher le contenu d'un fichier"+"\nmktxt - créer un fichier texte avec la syntaxe : mktxt <nom du fichier> <contenu>"+"\ncopy - copier un fichier ou un dossier"+"\nsys scan - recherche d'autres configurations de CmdOS sur l'appareil"+"\nsys purge - supprime les fichiers temporaires"+"\nsys info - affiche les spécifications de l'appareil et du système"+"\ncredits - affiche les crédits"+"\nlicense - affiche la license de CmdOS"
    com={
        "help":"help - Afficher la liste des commandes :\n   help <commande>",
        "store":"store - Affiche les différents modules installables : \n   install <module> - installer un module \n   uninstall <module> - desinstaller un module""\n   list - affiche les différents modules installés""\n   info <module> - affiche les différentes informations sur un module",
        "cd":"cd - changer de dossier :\n   cd <chemin absolu>\n   cd <dossier à ouvrir>\n   cd .. : ouvre le dossier parent",
        "dir":"dir - permet de voir les fichiers/dossiers",
        "sys account":"account - Voir vos identifiants :\n   name - modifie votre nom d'utilisateur\n   password - modifie votre mot de passe\n   disconnect - déconnecte votre compte de l'appareil\n   delete - supprime totalement votre compte\n   reset - change votre clé de cryptage",
        "ren":"ren - renomer un fichier",
        "del":"del - supprimer un fichier / dossier",
        "sys update":"update :""\n   upgrade - mettre à jour le système en téléchargant la dernière version""\n   check - vérifier si une nouvelle mise à jour est disponible",
        "admin":"admin on/off - active ou désactive le mode admin",
        "log":"log - affiche l'état des logs (il faut être connecté en tant qu'administrateur pour utiliser cette commande)""\n   enable - active les logs""\n   disable - désactive les logs""\n   delete - supprime les logs",
        "detail":"detail - affiche les propriétés d'un fichier ou dossier sous forme de os.stat_result",
        "shell":"shell (version raccourci : sh) - ferme CmdOS",
        "unlog":"unlog - déconnecte l'utilisateur",
        "mkdir":"mkdir - crée un dossier",
        "move":"move - déplacer un dossier ou un fichier",
        "cat":"cat - afficher le contenu d'un fichier",
        "mktxt":"mktxt - créer un fichier texte avec la syntaxe : mktxt <nom du fichier> <contenu>",
        "copy":"copy - copier un fichier ou un dossier",
        "sys purge":"sys purge - supprime les fichiers temporaires",
        "sys scan":"sys scan - recherche d'autres configurations de CmdOS sur l'appareil",
        "sys info":"sys info - affiche les spécifications de l'appareil et du système",
        "credits":"credits - affiche les crédits",
        "license":"license - affiche la license de CmdOS"
        }
    print("[SHELLTER.MAIN] : Variables are set")
    print("[SHELLTER.MAIN] : Get system's folder...")
    adresseapp=os.path.realpath(__file__)
    adresseapp=os.path.dirname(adresseapp)
    adresseapp=os.path.dirname(adresseapp)
    print("[SHELLTER.MAIN] : System's folder stocked in adresseapp='"+adresseapp+"'")
    print("[SHELLTER.MAIN] : Get work's folder...")
    adresse=os.path.realpath(__file__)
    adresse=os.path.dirname(adresse)
    adresse=os.path.dirname(adresse)
    print("[SHELLTER.MAIN] : Work's folder in adresse='"+adresse+"'")
    print("[SHELLTER.MAIN] : Checking system's integrity...")
    if not os.path.exists(adresse)==True:
        while not os.path.exists(adresse)==True:
            print("[SHELLTER.MAIN] : Adress error, please retry or contact your administrator / lolo859 on GitHub")
            quit()
    if not(os.path.exists(adresse+"/module") and os.path.exists(adresse+"/user") and os.path.exists(adresse+"/logs") and os.path.exists(adresse+"/temp") and os.path.exists(adresse+"/system")):
        print(colored("[SHELLTER.MAIN] : Some file(s) and/or folder(s) are missing, please reintsall CmdOS","red",attrs=["bold"]))
        quit()
    print("[SHELLTER.MAIN] : If you can see this message, no error occured")
    print("[SHELLTER.MAIN] : Setting user's variables...")
    charginstall=1
    displaysplit=0
    logserver=1
    version="3.0"
    if not os.path.exists(adresseapp+"/system/checkupdate.txt"):
        open(adresseapp+"/system/checkupdate.txt","w").write("0")
    check_update=open(adresseapp+"/system/checkupdate.txt","r").readlines()[0]
    if not os.path.exists(adresseapp+"/system/autoclear.txt"):
        open(adresseapp+"/system/autoclear.txt","w").write("0")
    autoclear=open(adresseapp+"/system/autoclear.txt","r").readlines()[0]
    if not os.path.exists(adresseapp+"/system/notfoundbehaviour.txt"):
        open(adresseapp+"/system/notfoundbehaviour.txt","w").write("error")
    notfoundbehaviour=open(adresseapp+"/system/notfoundbehaviour.txt","r").readlines()[0]
    print("[SHELLTER.MAIN] : Shellter's boot complete")
    return charginstall,displaysplit,logserver,version,invit,a,help,com,connect,cur,connsql,adresse,adresseapp,Result,check_update,autoclear,online,notfoundbehaviour