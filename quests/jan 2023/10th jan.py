from math import *
from random import *

#0
n = int(input("дай позитивное число: "))
while True:
    print(n)
    n -= 1
    if n < 0:
        break


#16
while True:
    print("Mõtlesin numbrile 1-10 vahel. Püüa ära arvata, mis see on!")
    arvutinumber = random.randint(1, 10)
    while True:
        proov = input("Arvake ära number, mis ma mõtlesin! (Või tippige 'end', et lõpetada): ")
        if proov.lower() == "end":
            exit()
        try:
            proov = int(proov)
        except ValueError:
            print("Mida? Anda number palun.")
            continue
        if proov < arvutinumber:
            print("liiga madalale!")
        elif proov > arvutinumber:
            print("Liiga kõrgel!")
        else:
            print("Õige! my number oli", arvutinumber)
            exit()



#15
katsed = 0
while True:
    answer = input("Osta elevant ära, kirjuta 'elevant' et ostma... ")
    katsed += 1
    if answer.lower() == "elevant":
        print(f"Teil elevandi ostmiseks kulus {katsed} katse.")
        break

