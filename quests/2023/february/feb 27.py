def Sorteerimine(i:list,p:list):
    """Kirjeldus....kirjuta ise!!!
    :param list i: Inimeste järjend
    :param list p: Palgade järjend
    :rtype: list, list
    """
    v=int(input("palk 1-kahaneb,2-kasvab?"))
    if v==1:
        n=len(p)
        for j in range(0,n-1):
            for k in range(j+1,n):
                if p[j]<p[k]:
                    abi=p[j]
                    p[j]=p[k]
                    p[k]=abi
                    abi=i[j]
                    i[j]=i[k]
                    i[k]=abi
    elif v==2:
        n=len(p)
        for j in range(0,n-1):
            for k in range(j+1,n):
                if p[j]>p[k]:
                    abi=p[j]
                    p[j]=p[k]
                    p[k]=abi
                    abi=i[j]
                    i[j]=i[k]
                    i[k]=abi

    return i,p

def Vordsed_palgad(i:list,p:list):
    """Kirjeldus....kirjuta ise!!!
    :param list i: Inimeste järjend
    :param list p: Palgade järjend
    :rtype: list, list
    """
    dublikatid=[x for x in p if p.count(x)>1 ]
    dublikatid=list(set(dublikatid)) #[1200,2500,750,750,1200]->[1200,750]
    for palk in dublikatid: 
        n=p.count(palk) #1200, n=2; 750, n=2
        k=-1 #-----
        print(f"{palk} saavad kätte järgmised inimesed:")
        for j in range(n):            
            k=p.index(palk,k+1)#-----
            nimi=i[k]
            print(nimi)
