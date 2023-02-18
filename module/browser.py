import webbrowser
from termcolor import colored
def execute(displaysplit,rep):
    browser=rep[8::]
    if type(browser)==str:
        webbrowser.open(browser)
    else:
        print(colored("L'URl n'est pas bonne","red",))