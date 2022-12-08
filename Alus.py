from math import * #*-koik funktsioonid on vaja kasutada. kasutame sin()
#import math math.sin()
#2.osa math kasutamine
print("ristkuliku ja ringi pindalad")
a=float(input("anna laius: "))
b=float(input("anna korgus: "))
S=a*b
d=sqrt(a**2+b**2)
r=float("anna raadius: ")
Skr=pi*r**2
print(f"ristkuliku pindala on {S}. Ringi pindala on {round(Skr,2)}.")





#1.osa
print("Tere Tulemast") #print() teksti voi andmete valjastuseks
nimi=input("mis on su nimi? ")#sisendi lugemine
#input to str
print(f"{nimi}, sul on väga ilus nimi!")
print(nimi,", sul on väga ilus nimi!")
print(nimi+", sul on väga ilus nimi!")
vanus=int(input("kui vana sa oled? ")) #input() to int
print(f"{nimi} jargmisel aastal saad {vanus+1}")
print("aga selle aastal on", vanus)
vanus+=1
print(f"järgmine aasta on käes, siis {nimi} on {vanus} aastat vana")
pikkus=float(input("mis on sinu pikkus? ")) #input to float: 1.75
print(f"{nimi} on {vanus} aastat vana ja suurepärase pikkusega {pikkus}")
