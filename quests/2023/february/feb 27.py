def Kustutamine(i:list,p:list):
    nimi=input("sisesta nimi: ")
    if nimi in i:
        n=i.count(nimi)
        for j in range(n):
            ind=i.index(nimi)
            i.pop(ind)
            p.pop(ind)

    return i,p
