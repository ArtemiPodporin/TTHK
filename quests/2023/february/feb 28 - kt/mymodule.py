from math import *
import random

def lapsed():
    nimed = []
    keskmise_hinnad = []

    # Get number of children from user
    mittu_lapse = int(input("Enter number of children: "))

    # Looge iga lapse jaoks juhuslikud nimed ja keskmised hinded
    for i in range(mittu_lapse):
        nimi = input(f"Sisesta lapse nimi {i+1}: ")
        hind = round(random.uniform(1, 5), 2)
        nimed.append(nimi)
        keskmise_hinnad.append(hind)

    while True:
        # Kuva menüü
        print("\nVali oma valik!:")
        print("1. Kuva laste nimed A-st Z-ni")
        print("2. Näidake suurepärast õpilast")
        print("3. Leidke laste keskmiste hinnete keskmine tulemus")
        print("4. Leidke lapse keskmine hinne, märkides tema nime")
        print("5. Loendage õpilaste arv ja hinded kokku")
        print("6. Välju")

        valik = int(input("Sisesta valik: "))

        if valik == 1:
            # Kuvage A-st Z-ni järjestatud laste nimed
            sortireeritud_nimed = sorted(nimed)
            for i in range(mittu_lapse):
                print(f"{sortireeritud_nimed[i]} - {keskmise_hinnad[nimed.index(sortireeritud_nimed[i])]}")

        elif valik == 2:
            # Näidake suurepärast õpilast, kui on kohal
            отличник = False
            for i in range(mittu_lapse):
                if keskmise_hinnad[i] == 5:
                    print(f"{nimed[i]} on suurepärane õpilane, hindeks 5")
                    отличник = True
                    break
            if not отличник:
                print("Suurepärast õpilast ei leitud")

        elif valik == 3:
            # Leidke laste keskmiste hinnete keskmine tulemus
            keskminne_hind = sum(keskmise_hinnad) / mittu_lapse
            print(f"Laste keskmiste hinnete keskmine punktisumma on {round(keskminne_hind, 2)}")

        elif valik == 4:
            # Leidke lapse keskmine märk nime järgi
            nimi = input("Sisestage lapse nimi: ")
            if nimi in nimed:
                indeks = nimed.index(nimi)
                print(f"{nimi} keskminne hind on {keskmise_hinnad[indeks]}")
            else:
                print(f"Ühtegi last nimega {nimi} ei leitud")

        elif valik == 5:
            # Loendage õpilaste arv ja hinded kokku
            kokku_hinde = sum(keskmise_hinnad)
            print(f"Seal on {mittu_lapse} õpilast, kellel on kokku {kokku_hinde} hinne")

        elif valik == 6:
            # Välju programmist
            print("Head aega...")
            break

        else:
            # Vale valik
            print("Valik on vale, proovige uuesti")
