from math import *
from random import *

#1
print("Puu l�bim��du arvutamine")
C=float(input("Puu �mberm��t: "))
d=2*(C/(2*pi))
print(f"Vastus:\nPuu l�bim��duga {C} �mberm��t v�rdub {d}")

#2
print("Ristk�likukujulise maat�ki diagonaal")
N=float(input("Sisesta ristk�liku 1. k�lje pikkus => "))
M=float(input("Sisesta ristk�liku 2. k�lje pikkus => "))
d=sqrt(N**2+M**2)
print(f"Maat�ki diagonaal on {d} m**2")

#3
aeg = float(input("Mitu tundi kulus s�iduks? "))
teepikkus = float(input("Mitu kilomeetrit s�itsid? "))
kiirus = aeg/teepikkus
print()
print("Sinu kiirus oli " + str(kiirus) + " km/h")

#4
A1=int(input("sisesta 1. arv => "))
A2=int(input("sisesta 2. arv => "))
A3=int(input("sisesta 3. arv => "))
A4=int(input("sisesta 4. arv => "))
A5=int(input("sisesta 5. arv => "))
Keskmine=(A1+A2+A3+A4+A5)/5
print(f"Keskmine on {Keskmine}")

#5
print("    @..@")
print("   (----)")
print("  ( \__/ )")
print("  ^^ "'""'" ^^ ")

#6 
a=randint(1,100)
b=randint(1,100)
c=randint(1,100)
print(f"K�lg a={a}\nK�lg b={b}\nK�lg c={c}")
print(f"Kolmnurga �mberm��t = {a+b+c}")
print()

#--------------------------------