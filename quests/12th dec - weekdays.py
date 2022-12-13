from math import *
from random import *

print("Nädalapäevad")
try:
    p=int(input("Mis päev täna on?"))
    if p==1:
        n="esmaspäev"
    elif p==2:
        n="teisipäev"
    elif p==3:
        n="kolmapäev"
    elif p==4:
        n="neljapäev"
    elif p==5:
        n="reede"
    elif p==6:
        n="laupäev"
    elif p==7:
        n="pühapäev"
    else:
        n="vale number"
    print(n)  
except:
    print("Viga")







try:
    hinne=int(input("Mis hinne täna said koolis"))
except:
    print("!!!!!!")
if hinne==5:
    print("Väga hea!")
elif hinne==4:
    print("Hea!")
elif hinne==3:
    print("Rahuldav")
elif hinne==2 or hinne==1: #and, or, not, !=ei võrdu, <, >, >=,<=
    print("Mitte rahuldav!")
else:
    print("Viga!")
