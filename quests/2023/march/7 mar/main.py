import random

# lugege failist küsimusi ja vastuseid
with open('questions_and_answers.txt') as f:
    kus_vas = dict(line.strip().split(':') for line in f)

# määrake küsimuste arv ja küsitlemiseks kandideerijad
NUM_QUESTIONS = 5
NUM_APPLICANTS = 5

# initsialiseerida heakskiidetud ja vastu võtmata taotlejate nimekirjad
aksepteeritud = []
ei_kehti = []

# määrake taotlejale küsimuste esitamise funktsioon
def esitada_küsimusi(applicant):
    # esitage NUM_QUESTIONS juhuslikku küsimust vastusete sõnastikust
    kusimused = random.sample(list(kus_vas.keys()), NUM_QUESTIONS)
    # algatada taotleja hinde
    hinne = 0
    # esitage iga küsimus ja võrrelge vastust õigega
    for kusimus in kusimused:
        answer = input(f"{applicant}, {kusimus}? ")
        if answer == kus_vas[kusimus]:
            hinne += 1
    return hinne

# küsitluse taotlejad
for i in range(NUM_APPLICANTS):
    taotleja = input("What's your name? ")
    hinne = esitada_küsimusi(taotleja)
    if hinne >= 3:
        aksepteeritud.append((taotleja, hinne))
    else:
        ei_kehti.append(taotleja)

# sorteeri vastuvõetud taotlejad skoori järgi
aksepteeritud.sort(key=lambda x: x[1], reverse=True)

# kirjutage failidesse aktsepteeritud ja mitteaktsepteeritud taotlejad
with open('answers.txt', 'w') as f:
    for taotleja, hinne in aksepteeritud:
        f.write(f"{taotleja}: {hinne}\n")
with open('not_valid.txt', 'w') as f:
    for taotleja in sorted(ei_kehti):
        f.write(f"{taotleja}\n")

# kuvatakse heakskiidetud ja mitteaktsepteeritavate taotlejate nimekirjad
print("Vastuvõetud taotlejad:")
for taotleja, hinne in aksepteeritud:
    print(f"{taotleja}: {hinne}")
print("Ei aktsepteeritud taotlejaid:")
for taotleja in ei_kehti:
    print(taotleja)


