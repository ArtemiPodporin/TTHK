from math import * #*-k�ik funktsioonid on vaja kasutada. kasutame: sin()

#1.osa print(), input(),int(),float()
print("Tere tulemast!") #print() teksti v�i andmete v�ljastuseks
nimi=input("Mis on sinu nimi? ")#Sisendi lugemine: akraanil "..."ja ootab , kuni kasutaja vajutab Enter klahvi
# input() -> str
print(f"{nimi}, sul on v�ga ilus nimi!")
print(nimi,", sul on v�ga ilus nimi!")#kui on erinevat andmete t��bid
print(nimi+", sul on v�ga ilus nimi!")#kui on sarnane andmete t��p
vanus=int(input("Kui vana sa oled? "))# input()->int
print(f"{nimi} jargmisel aastal saad {vanus+1}")#muutuja vanus ei muuda
print("Aga selle aastal on ", vanus)
vanus+=1 #muudame muutuja v��rtus
print(f"J�rgmine aasta on k�es, siis {nimi} on {vanus} aastat vana")
pikkus=float(input("Mis on sinu pikkus? ")) #input()->float: 1.75
print(f"{nimi} on {vanus} aastat vana ja suurep�rase pikkusega {pikkus}")


#import math kasutame: math.sin()
#2.osa Math kasutamine 
print("Ristk�liku ja ringi pindalad")
a=float(input("Anna laius: "))
b=float(input("Anna k�rgus: "))
S=a*b #+,-,/,*,**,sqrt(),//,%
d=sqrt(a**2+b**2)
r=float(input("Anna raadius: "))
Skr=pi*r**2
print(f"Ristk�liku pindala on {S}. Ringi pindala on {round(Skr,2)}.")


#-----------------------------
 
print()
print("Ruudu karakteristikud")
a=float(input("Sisesta ruudu k�lje pikkus => "))
S=a**2
print("Ruudu pindala", round(S,1))
P=4*a
print("Ruudu �mberm��t", round(P,1))
di=a*sqrt(2)
print("Ruudu diagonaal", round(di,2))
print()

#-----------------------------

print("Ristk�liku karakteristikud")
b=float(input("Sisesta ristk�liku 1. k�lje pikkus => "))
c=float(input("Sisesta ristk�liku 2. k�lje pikkus => "))
S=b*c
print("Ristk�liku pindala", round(S,1))
P=2*(b+c)
print("Ristk�liku �mberm��t", round(P,1))
di=sqrt(b*2+c*2)
print("Ristk�liku diagonaal", round(di,1))
print()
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => "))
d=2*r
print("Ringi l�bim��t", round(d,1))
S=pi*r**2
print("Ringi pindala", round(S,2))
C=2*pi*r
print("Ringjoone pikkus", round(C,2))
