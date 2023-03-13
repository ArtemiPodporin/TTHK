import random

# lugege failist küsimusi ja vastuseid
kusimused = open("kusimusedjavastused.txt", "r")
kus_vas = {}
for line in kusimused:
    kusimus, vastus = line.strip().split(":")
    kus_vas[kusimus] = vastus
kusimused.close()

# määrake küsimuste arv ja küsitlemiseks kandideerijad
küsimuste_arv = 5
taotlejate_arv = 5

# initsialiseerida heakskiidetud ja vastu võtmata taotlejate nimekirjad
vastuvõetud = []
eisoobi = []

# määrake taotlejale küsimuste esitamise funktsioon
def esitada_küsimusi(taotleja):
    # esitage küsimuste_arv juhuslikku küsimust vastusete sõnastikust
    kusimused = random.sample(list(kus_vas.keys()), küsimuste_arv)
    # algatada taotleja hinde
    hinne = 0
    # esitage iga küsimus ja võrrelge vastust õigega
    for kusimus in kusimused:
        vastus = input(f"{taotleja}, {kusimus}? ")
        if vastus == kus_vas[kusimus]:
            hinne += 1
    return hinne

# küsitluse taotlejad
for i in range(taotlejate_arv):
    taotleja = input("Mis on sinu nimi? ")
    hinne = esitada_küsimusi(taotleja)
    if hinne >= 3:
        vastuvõetud.append((taotleja, hinne))
    else:
        eisoobi.append(taotleja)

# sorteeri vastuvõetud taotlejad skoori järgi
vastuvõetud.sort(key=lambda x: x[1], reverse=True)

# kirjutage failidesse aktsepteeritud ja mitteaktsepteeritud taotlejad
with open('vastuvõetud.txt', 'w') as f:
    for taotleja, hinne in vastuvõetud:
        f.write(f"{taotleja}: {hinne}\n")
with open('eisoobi.txt', 'w') as f:
    for taotleja in sorted(eisoobi):
        f.write(f"{taotleja}\n")

# kuvatakse heakskiidetud ja mitteaktsepteeritavate taotlejate nimekirjad
print("Vastuvõetud taotlejad:")
for taotleja, hinne in vastuvõetud:
    print(f"{taotleja}: {hinne}")
print("Ei aktsepteeritud taotlejaid:")
for taotleja in eisoobi:
    print(taotleja)


