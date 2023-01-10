#15
katsed = 0
while True:
    answer = input("Osta elevant ära! ")
    katsed += 1
    if answer.lower() == "elevant":
        print(f"Teil elevandi ostmiseks kulus {katsed}.")
        break

