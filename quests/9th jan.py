#1
for i in range(2, 12, 3)
    print(i, end=" ")
print()
for i in range(12, 2, -2)
    print(i, end=" ")
print()

#2.1
print("Arvuta peast! ...4*100-55")
o_vastus=4*100-55
vastus=int(input("Lahenda ülesanne..."))
k=1
while vastus!=o_vastus:
    print("Viga! Sisesta Õige vastus...", )
    vastus=int(input("Sisesta vastus..."))
    k+=1
print("Õige vastus! Katsed oli ...",k )

#2.2
x=0
while x<30:
    if x%2==1:
        print(x, end=" ")
    x+=1

