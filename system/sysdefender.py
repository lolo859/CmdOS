import os
import psycopg2
import shutil
import subprocess
def connectt():
    try:
        import requests
        requests.get("https://www.google.com",allow_redirects=True)
        return True
    except:
        return False
def analyse_module(name,adresseapp,rep,displaysplit,repname):
    if connectt():
        command="SELECT name FROM module;"
        connsql = psycopg2.connect(user = "cmdos",password = "CmdOS2008)",host = "postgresql-cmdos.alwaysdata.net",port = "5432",database = "cmdos_user")
        cur = connsql.cursor()
        cur.execute(command)
        data=cur.fetchall()
        for i in range(len(data)):
            data[i]=str(data[i][0])
        if name in data:
            return "ok"
        else:
            os.chdir(adresseapp)
            parent=os.path.dirname(adresseapp)
            shutil.copytree(parent+"/CmdOS",os.path.join(adresseapp,"vm"))
            origin=[os.path.join(root, file) for root, _, files in os.walk(adresseapp+"/vm") for file in files]
            moduler=name
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
            after=os.listdir(adresseapp+"/vm")
            try:
                avant=open(adresseapp+"/CmdOS.py","r").readlines()
                apres=open(adresseapp+"/vm/CmdOS.py","r").readlines()
                if not avant==apres:
                    shutil.rmtree(adresseapp+"/vm")
                    return "error"
                avant=open(adresseapp+"/system/shellter_core.py","r").readlines()
                apres=open(adresseapp+"/vm/system/shellter_core.py","r").readlines()
                if not avant==apres:
                    shutil.rmtree(adresseapp+"/vm")
                    return "error"
                avant=open(adresseapp+"/system/shellter_main.py","r").readlines()
                apres=open(adresseapp+"/vm/system/shellter_main.py","r").readlines()
                if not avant==apres:
                    shutil.rmtree(adresseapp+"/vm")
                    return "error"
                avant=open(adresseapp+"/system/sysdefender.py","r").readlines()
                apres=open(adresseapp+"/vm/system/sysdefender.py","r").readlines()
                if not avant==apres:
                    shutil.rmtree(adresseapp+"/vm")
                    return "error"
                if not "system" in after:
                    shutil.rmtree(adresseapp+"/vm")
                    return "error"
                if not "user" in after:
                    shutil.rmtree(adresseapp+"/vm")
                    return "error"
                if not "module" in after:
                    shutil.rmtree(adresseapp+"/vm")
                    return "error"
                if not "logs" in after:
                    shutil.rmtree(adresseapp+"/vm")
                    return "error"
                shutil.rmtree(adresseapp+"/vm")
                return "advert"
            except:
                return "error"
    else:
        os.chdir(adresseapp)
        parent=os.path.dirname(adresseapp)
        shutil.copytree(parent+"/CmdOS",os.path.join(adresseapp,"vm"))
        origin=[os.path.join(root, file) for root, _, files in os.walk(adresseapp+"/vm") for file in files]
        moduler=name
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
        after=os.listdir(adresseapp+"/vm")
        try:
            avant=open(adresseapp+"/CmdOS.py","r").readlines()
            apres=open(adresseapp+"/vm/CmdOS.py","r").readlines()
            if not avant==apres:
                shutil.rmtree(adresseapp+"/vm")
                return "error"
            avant=open(adresseapp+"/system/shellter_core.py","r").readlines()
            apres=open(adresseapp+"/vm/system/shellter_core.py","r").readlines()
            if not avant==apres:
                shutil.rmtree(adresseapp+"/vm")
                return "error"
            avant=open(adresseapp+"/system/shellter_main.py","r").readlines()
            apres=open(adresseapp+"/vm/system/shellter_main.py","r").readlines()
            if not avant==apres:
                shutil.rmtree(adresseapp+"/vm")
                return "error"
            avant=open(adresseapp+"/system/sysdefender.py","r").readlines()
            apres=open(adresseapp+"/vm/system/sysdefender.py","r").readlines()
            if not avant==apres:
                shutil.rmtree(adresseapp+"/vm")
                return "error"
            if not "system" in after:
                shutil.rmtree(adresseapp+"/vm")
                return "error"
            if not "user" in after:
                shutil.rmtree(adresseapp+"/vm")
                return "error"
            if not "module" in after:
                shutil.rmtree(adresseapp+"/vm")
                return "error"
            if not "logs" in after:
                shutil.rmtree(adresseapp+"/vm")
                return "error"
            shutil.rmtree(adresseapp+"/vm")
            return "advert"
        except:
            return "error"