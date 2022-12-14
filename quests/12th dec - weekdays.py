from math import *
from random import *

print("Nädalapäevad")
try:
    päev=int(input("Mis päev täna on?"))
    if päev==1:
        n="esmaspäev"
        n="6 tundi"
    elif päev==2:
        n="teisipäev"
        n="8 tundi"
    elif päev==3:
        n="kolmapäev"
        n="6 tundi"
    elif päev==4:
        n="neljapäev"
        n="5 tundi"
    elif päev==5:
        n="reede"
        n="7 tundi"
    elif päev==6:
        n="laupäev"
        n="0 tundi"
    elif päev==7:
        n="pühapäev"
        n="0 tundi"
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
