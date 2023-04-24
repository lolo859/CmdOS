import webbrowser
from termcolor import colored
import cmd_fonction as cmdf
def execute(displaysplit,rep):
    browser=rep[8::]
    if type(browser)==str:
        if cmdf.connect()==True:
            webbrowser.open(browser)
        else:
            print(colored("Vous devez connecté à internet pour utiliser ce module","red"))
    else:
        print(colored("L'URl n'est pas bonne","red",))