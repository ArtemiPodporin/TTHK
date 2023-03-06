def Loe_failist(fail:str)->list:
    """
    """
    f=open(fail,'r',encoding="utf-8")
    jarjend=[]
    for rida in f:
        jarjend.append(rida.strip())
    f.close()
    return jarjend
def Kirjuta_failisse(fail:str,jarjend:list):
    f=open(fail,'w',encoding="utf-8")
    for line in jarjend:
        f.write(line+'\n')
    f.close()
