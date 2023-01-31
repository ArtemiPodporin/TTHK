maakonnad = [    [1, "Tallinnas"],
    [2, "Narvas, Narva-Jõesuul"],
    [3, "Kohtla-Järvel"],
    [4, "Ida-Virumaal, Lääne-Virumaal, Jõgevamaal"],
    [5, "Tartu linnas"],
    [6, "Tartumaal, Põlvamaal, Võrumaal, Valgamaal"],
    [7, "Viljandimaal, Järvamaal, Harjumaal, Raplamaal"],
    [8, "Parnumaal"],
    [9, "Läänemaal, Hiiumaal, Saaremaal"]  ]

def ValideeriKood(ZipKood):
    EsimeneNumber = int(str(ZipKood)[0])
    for maakond in maakonnad:
        if maakond[0] == EsimeneNumber:
            return maakond[1]

ZipKood = input("Andke oma zipkoodi: ")

try:
    ZipKood = int(ZipKood)
    if len(str(ZipKood)) == 5:
        maakond = ValideeriKood(ZipKood)
        if maakond in ["Tallinn", "Narva, Narva-Jõesuu", "Kohtla-Järve"]:
            print("Sa elad",maakond,", palun püsi kodus!!")
        else:
            print("Sa elad",maakond,", palun kandke maske!!")
    else:
        print("Postiindeks peab koosnema 5 numbrist.")
except ValueError:
    print("Postiindeks peab olema number.")
