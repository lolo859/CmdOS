import secure_id
def initialise(adresse):
    id=secure_id.sid1()
    open(adresse+"/temp/"+id+".txt","w")
    return id
def check_cpu(id,adresse):
    import psutil
    with open(adresse+"/temp/"+id+".txt","a") as text:
        text.write("[SHELLTER.CORE] : Cpu usage : "+str(psutil.cpu_percent(0.1))+"\n")