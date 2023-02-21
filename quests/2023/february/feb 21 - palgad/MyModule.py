palk = [1200,2500,750,395,1200]
inimesed = ["A","B","C","D","E"]

def leiaPalk(inimene):
palgad = []
for i in range(len(inimesed)):
if inimesed[i] == inimene:
palgad.append(palk[i])
return palgad