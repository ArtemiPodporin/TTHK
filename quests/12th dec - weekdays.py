from math import *
from random import *

print("N�dalap�evad")
try:
    p=int(input("Mis p�ev t�na on?"))
    if p==1:
        n="esmasp�ev"
    elif p==2:
        n="teisip�ev"
    elif p==3:
        n="kolmap�ev"
    elif p==4:
        n="neljap�ev"
    elif p==5:
        n="reede"
    elif p==6:
        n="laup�ev"
    elif p==7:
        n="p�hap�ev"
    else:
        n="vale number"
    print(n)  
except:
    print("Viga")







try:
    hinne=int(input("Mis hinne t�na said koolis"))
except:
    print("!!!!!!")
if hinne==5:
    print("V�ga hea!")
elif hinne==4:
    print("Hea!")
elif hinne==3:
    print("Rahuldav")
elif hinne==2 or hinne==1: #and, or, not, !=ei v�rdu, <, >, >=,<=
    print("Mitte rahuldav!")
else:
    print("Viga!")
