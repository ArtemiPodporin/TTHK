from math import *
from random import *

#1
print("Puu läbimõõdu arvutamine")
C=float(input("Puu ümbermõõt: "))
d=2*(C/(2*pi))
print(f"Vastus:\nPuu läbimõõduga {C} ümbermõõt võrdub {d}")

#2
print("Ristkülikukujulise maatüki diagonaal")
N=float(input("Sisesta ristküliku 1. külje pikkus => "))
M=float(input("Sisesta ristküliku 2. külje pikkus => "))
d=sqrt(N**2+M**2)
print(f"Maatüki diagonaal on {d} m**2")

#3
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
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
print(f"Külg a={a}\nKülg b={b}\nKülg c={c}")
print(f"Kolmnurga ümbermõõt = {a+b+c}")
print()

#--------------------------------