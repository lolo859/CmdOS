import requests as req
from termcolor import colored
def execute(displaysplit,rep):
    download=rep.split()
    if displaysplit==1:
        print(download)
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
            except UnicodeDecodeError:
                pass
        else:
            print(colored("Le nom de fichier doit terminé par '.html'","red",attrs=["bold"]))
    else:
        print(colored("La commande n'est pas bien formulée","red",attrs=["bold"]))