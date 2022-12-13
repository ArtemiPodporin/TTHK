from math import *
from random import *
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

