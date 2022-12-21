from math import *
from random import *

#3
# 
length = float(input("длину комнаты в метрах: "))
width = float(input("ширина комнаты в метрах: "))
area = length * width

make_repairs = input("чиним? (да или нет) ")

if make_repairs.lower() == "да":
  ЦенаЗаКвадМетер = float(input("Цена за квадратный метер: "))
  # выясняем цену
  ВсяЦена = ЦенаЗаКвадМетер * area
  print(f"Цена починки: {ВсяЦена:.2f}.")
else:
  print("Не чиним!")


#2
while True:
    nimi1=input("1. Mis on sinu nimi? ")
    if nimi1.isalpha(): break
while True:
    nimi2=input("2. Mis on sinu nimi? ")
    if nimi2.isalpha(): break

#1
while True:
    nimi=input("Mis on sinu nimi? ")
    if nimi.isalpha(): break

if nimi.upper()=="JUKU":
    while True:
        try:
            vanus=int(input("Kui vana sa oled? "))
        except:
            print("kasuta arvude tuup!")
    
    if vanus < 6:
        print("Jukul on tasuta pilet!")
    #Kui Juku on vanem kui 6 aga noorem 14, siis laste pilet!
    elif vanus >= 6 and vanus <= 14:
        print("Lastepilet Jukule!")
    #kui on vanem kui 15 või noorem kui 65, siis täispilet
    elif vanus >= 15 and vanus <= 65:
        print("Täispilet.")
    #Kui on vanem kui 65, siis on soodus
    elif vanus > 65:
        print("Soodus!")
  #Kui on vanem kui 100 või noorem kui 0, siis viga
    else:
        print("Viga! Kas ta on inimene?")