import random

# lugege failist k�simusi ja vastuseid
with open('questions_and_answers.txt') as f:
    kus_vas = dict(line.strip().split(':') for line in f)

# m��rake k�simuste arv ja k�sitlemiseks kandideerijad
NUM_QUESTIONS = 5
NUM_APPLICANTS = 5

# initsialiseerida heakskiidetud ja vastu v�tmata taotlejate nimekirjad
aksepteeritud = []
ei_kehti = []

# m��rake taotlejale k�simuste esitamise funktsioon
def esitada_k�simusi(applicant):
    # esitage NUM_QUESTIONS juhuslikku k�simust vastusete s�nastikust
    kusimused = random.sample(list(kus_vas.keys()), NUM_QUESTIONS)
    # algatada taotleja hinde
    hinne = 0
    # esitage iga k�simus ja v�rrelge vastust �igega
    for kusimus in kusimused:
        answer = input(f"{applicant}, {kusimus}? ")
        if answer == kus_vas[kusimus]:
            hinne += 1
    return hinne

# k�sitluse taotlejad
for i in range(NUM_APPLICANTS):
    taotleja = input("What's your name? ")
    hinne = esitada_k�simusi(taotleja)
    if hinne >= 3:
        aksepteeritud.append((taotleja, hinne))
    else:
        ei_kehti.append(taotleja)

# sorteeri vastuv�etud taotlejad skoori j�rgi
aksepteeritud.sort(key=lambda x: x[1], reverse=True)

# kirjutage failidesse aktsepteeritud ja mitteaktsepteeritud taotlejad
with open('answers.txt', 'w') as f:
    for taotleja, hinne in aksepteeritud:
        f.write(f"{taotleja}: {hinne}\n")
with open('not_valid.txt', 'w') as f:
    for taotleja in sorted(ei_kehti):
        f.write(f"{taotleja}\n")

# kuvatakse heakskiidetud ja mitteaktsepteeritavate taotlejate nimekirjad
print("Vastuv�etud taotlejad:")
for taotleja, hinne in aksepteeritud:
    print(f"{taotleja}: {hinne}")
print("Ei aktsepteeritud taotlejaid:")
for taotleja in ei_kehti:
    print(taotleja)


