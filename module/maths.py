from termcolor import colored
def execute(displaysplit,rep):
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