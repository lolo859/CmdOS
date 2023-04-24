import requests as req
from termcolor import colored
def execute(adresse,displaysplit,rep):
    download=rep.split()
    if displaysplit==1:
        print(download)
    if len(download)==3:
        urldown=download[1]
        lentxt=len(download[2])-5
        txtname=download[2]
        try:
            txtcontent=req.get(urldown,allow_redirects=True)
            open(adresse+"/download/"+txtname,"wb").write(txtcontent.content)
            print(colored(("La page web a bien été enregistré sous le nom "+txtname),"blue",attrs=["bold"]))
        except req.exceptions.MissingSchema:
            print(colored("La page web n'existe pas","yellow",attrs=["bold"]))
        except UnicodeDecodeError:
            pass
        except:
            print(colored("Vous devez connecté à internet pour utiliser ce module","red"))
    else:
        print(colored("La commande n'est pas bien formulée","red",attrs=["bold"]))