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
            break


#22
katsed=0
answer=""
while answer!="komm":
    answer=input("Tahan kommi!")
    katsed+=1
print("Katsed: {katsed}")
print()


#15
katsed = 0
while True:
    answer = input("Osta elevant ära, kirjuta 'elevant' et ostma... ")
    katsed += 1
    if answer.lower() == "elevant":
        print(f"Teil elevandi ostmiseks kulus {katsed} katse.")
        exit()


#0
while True:
    print("Tere Tulemast!")
    try:
        print("Latte, 2.50 euro")
        print("Espresso, 2 euro")
        print("Cappuccino, 3 euro")
        print("Kakao, 2.20 euro")
        s=float(input("Sisestage summa:"))
        if s<2 or s>3: break
        m=input("Valige makseviis, sularaha või kaardiga: ")

        if m.lower()=="sularaha":
            hind=float(input("Anna raha: "))
        if s==hind:
            print("Oodake")
        elif s==s-hind:
            t=s-hind
            print("Teile tagasiraha {t}, oodake sinu kohvi!")
        if m.lower()=="kaardiga":
            n=int(input("Sisestage kaardi number: "))
            print (n,"selle kaardiga on tehtud makse.")
    except:
        print("!!")
#while True:
       # print("Latte")
       # print("Espresso")
       # print("Cappuccino")
       # print("Kakao")
       # try:
        #    j=int("Valige jook:")

#0.2
positive = 0
negative = 0
while True:
    a=int(input("Sisestage number: "))
    if a>0: positive +=a
    elif a<0: negative +=a
    else:break
print("Positiivne:", positive, "Negatiivne:", negative)