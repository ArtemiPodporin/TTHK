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
try:
    A1=int(input("Sisesta 1. arv => "))
except:
    print("Vale andmetüüp!")
    A1=0
try:
    A2=int(input("Sisesta 2. arv => "))
except:
    print("Vale andmetüüp!")
    A2=0
A3=int(input("Sisesta 3. arv => "))
A4=int(input("Sisesta 4. arv => "))
A5=int(input("Sisesta 5. arv => "))
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

#7
print("Pitsa Võtsite 3 sõbraga suure pitsa hinnaga 12,90€ te jätate teenindaja 10%")
s=10*12.90/100
s=round(s)
d=(12.90+s)
print(f"Vastus: {d}")
p=d/3
p=round(p,1)
print (f"iga lollpea peab: {p}")
print()

#8
print("Kütusekulu arvutamine")
p=l/km*100
l=float(input("Kasutaja sisestab tangitud kütuse liitrid: "))
km=float(input("Kasutaja sisestab läbitud kilomeetrid: "))
print (f"Vastus: {p}l/km")
print()

#9
print("Rulluisutajad")
print("Rulluisutaja keskmine kiirus on 29,9km/h")
m=24/60
t=m*29.9
t=round(t,2)
print("Vastus: {t}km")
print()

#10
from math import *
print("Ajateisendus")
v=float(input("sisesta aja minutites: "))
t=int(v//60)
sec=int(v`)
print(f"minutes {t}: sekundid {sec}")


#--------------------------------
