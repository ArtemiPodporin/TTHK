from random import *
from math import *
from OmaMoodul import *

esimenenumber=[1,2,3,4,5,6]
isikukood=""
arvud=["100","1001","211","222"]
ikoodid=[]

while True:
    isikukood=input("sisestage sinu isikukood: \n")
    if isikukood=="-": break
    if checklen(isikukood)==False:
        print("Liiga pikk või lühike isikukood")
        arvud.append(isikukood)
    else:
        s=sugu(isikukood)
        if s=="viga":
            print("------------------------------")
            print("Esimene täht ei ole õige")
        else:
            if sunnipaev(isikukood)=="viga":
                print("------------------------------")
                print("2-7 tähed on valesti sisestatud")
            else:
                print("------------------------------")
                lause(isikukood)
                print("------------------------------")
                print((kontrollnr(isikukood)))
                if kontrollnr(isikukood)==int(isikukood[-1]):
                    print("OK")
                    ikoodid.append(isikukood)
                else:
                    print("!!!")
print()
ikoodid=naised_mehed(ikoodid)
print(ikoodid)
arvud_sorted(arvud)
print(arvud)