import MyModule

inimine = input("Sisesta nimi: ")
palgad = MyModule.leiaPalk(inimine)

if len(palgad) == 0:
    print("Ei leidsid palga", inimine)
else:
    print("Palk", inimine, "on:", palgad)