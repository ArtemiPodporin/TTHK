from math import *
from random import *

#3
# First, we ask the user for the length and width of the room
length = float(input("Enter the length of the room (in meters): "))
width = float(input("Enter the width of the room (in meters): "))

# Next, we calculate the area of the floor
area = length * width

# Then, we ask the user if they want to make repairs
make_repairs = input("Do you want to make repairs? (yes/no) ")

# If the user wants to make repairs, we ask for the cost per square meter
if make_repairs.lower() == "yes":
  cost_per_sq_meter = float(input("Enter the cost per square meter: "))
  # We calculate the total cost of replacing the floor
  total_cost = cost_per_sq_meter * area
  print(f"The total cost of replacing the floor is {total_cost:.2f}.")
else:
  print("No repairs will be made.")


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