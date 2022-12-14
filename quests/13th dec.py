from math import *
from random import *

#1
try:
    vanus=int(input("Kui vana sa oled?"))
except:
    print("!!!!!!")
if vanus==18:
    luba=int(input("Kas lubate vanematele hindeid vaadata?"))
elif vanus==14 or vanus==15 or vanus==16 or vanus==17: #and , or, not !=ei võrdu, <, >, >=, <=
    print("Automaatne juurdepääs vanematele")
else: 
    print("Viga!")

#2
try:
    hinne=int(input("Mis hinne täna said koolis"))
except:
    print("!!!!!!")
if hinne==5:
    print("Väga hea!")
elif hinne==4:
    print("Hea!")
elif hinne==3:
    print("Rahuldav!")
elif hinne==2 or hinne==1: #and , or, not !=ei võrdu, <, >, >=, <=
    print("Lastekodu!")
else: 
    print("Viga!")

#3
r=randint(-100,100)
a=randint(-100,100) 
print(f"r={r}\na={a}")
if r>0 and a>0:
    Skv=a**2
    Skv=pi*r**2
    if Skv>Skr:
        print(f"Ruudlu pindala {Skv} m^2 on suurem ringi pindala {Skr} m^2")
    elif Skr>Skv:
        Print(f"Ruudlu pindala {Skv} m^2 on suurem ruudu pindala {Skr} m^2")
    else:
        print("Pindalad on võrdsed. {Skr} m^2")
else:
    print(f"{a} ja {r} peavad > kui 0 olla")

#4
try:
     päev=int(input("Mis päev ja mitu tundi täna on ?"))
except:
     print("!!!!!!!")
if   päev==1:
    n="Esmaspäev"
    n="6 tundi"
elif päev==2:
    n="Teisipäev"
    n="8 tundi"
elif päev==3:
    n="Kolmapäev"
    n="6 tundi"
elif päev==4:
    n="Neljapäev"
    n="5 tundi"
elif päev==5:
    n="Reede"
    n="7 tundi"
elif päev==6:
    n="Laupäev"
    n="0 tundi"
elif päev==7:
    n="Pühapäev"
    n="0 tundi"
else: 
    n="vale number"
print(n)

print("sisselogimine tahvelisse")
try:
    vanus=int(input("kui vana sa oled?"))
    if vanus>=18:
        print("kas te annate vanematele loa oma tahvelit vaadata?")
        o=(input("jah või ei. "))
        if o.lower()=="jah": 
            print({o})
            print("see on ligipaas teie vanematele.")
            print("tahvel on kinni.")
        elif o.upper()=="EI":
            print("sissepaas puudub.")
            print("tahvel on kinni.")
    if vanus<18:
        print("juurdepaas vanematele on automaatselt antud.")
except:
    print("tahvel on kinni")
