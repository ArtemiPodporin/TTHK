import rus.txt
import est.txt

def tolgi_sona(sona, mis_keelest, mis_keele):
    if mis_keelest == "est" and mis_keele == "rus":
        allika_loend = est
        siht_loend = rus
    elif mis_keelest == "rus" and mis_keele == "est":
        allika_loend = rus
        siht_loend = est
    else:
        return "Toetamata tolge"

    if sona in allika_loend:
        index = allika_loend.index(sona)
        return siht_loend[index]
    else:
        return None

def lisa_sona(sona, keel):
    if keel == "est":
        siht_loend = est
        faili_nime = "est.txt"
    elif keel == "rus":
        siht_loend = rus
        faili_nime = "rus.txt"
    else:
        return "Toetamata tolge"

    if sona not in siht_loend:
        siht_loend.append(sona)
        with open(faili_nime, "a", encoding="utf-8") as f:
            f.write(sona + "\n")
        return "sona added"
    else:
        return "sona juba eksisteerib"

def correct_sona(vana_sona, uus_sona, keel):
    if keel == "est":
        siht_loend = est
        faili_nime = "est.txt"
    elif keel == "rus":
        siht_loend = rus
        faili_nime = "rus.txt"
    else:
        return "Toetamata tolge"

    if vana_sona in siht_loend:
        index = siht_loend.index(vana_sona)
        siht_loend[index] = uus_sona
        with open(faili_nime, "w", encoding="utf-8") as f:
            for sona in siht_loend:
                f.write(sona + "\n")
        return "sona parandatud"
    else:
        return "sona ei leitud"
