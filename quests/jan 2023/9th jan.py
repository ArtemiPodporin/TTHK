#1
for i in range(1,31,2):
    print(i, end=» «)

#2.1
print("Arvuta peast! ...4*100-55")
o_vastus = 4*100-55
katsed = 0
while True:
    vastus = int(input("Lahenda ülesanne... "))
    katsed += 1
    if vastus == o_vastus:
        print(f"Õige vastus! Katsed oli... {katsed}")
        break
    else:
        print("Viga! Sisesta Õige vastus...")


#2.2
x=0
while True:
    if x%2==1:
        print(x, end=» «)
    if x== 30:
        break
    x+=1
