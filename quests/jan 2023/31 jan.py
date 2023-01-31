from math import *
from random import *

# Задание 1: Почтовый индекс
#
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


# Задание 2: Перемена мест
#
def VahetaElemendi(arr, n):
    for i in range(n):
        arr[i], arr[-(i+1)] = arr[-(i+1)], arr[i]
    return arr

lst = [1, 2, 3, 4, 5]
n = int(input("Сколько элементов изменить?: "))

if n > len(lst) // 2:
    n = len(lst) // 2

print("Обычный список:", lst)
print("Изменённый список:", VahetaElemendi(lst, n))

# Задание 3: Бесполезные числа
# Функция LeiaKasutuNumber принимает в качестве аргумента список чисел и возвращает
# список делений наибольшего числа в списке. Функция использует понимание списка для 
# перебора всех делителей наибольшего числа и деления наибольшего числа на каждый 
# делитель, если делитель равномерно делит наибольшее число
def LeiaKasutuNumber(numbers):
    max_num = max(numbers)
    деления = [max_num // i for i in range(1, max_num + 1) if max_num % i == 0]
    return деления



# Задание 4: Сортировка
#
def SorteeriNumbrid(numbrid, reverse=False):
  return sorted(numbrid, key=lambda x: abs(x), reverse=reverse)

numbrid = [4, -2, -1, 9, -5, 8, 7, 6, 5, -9]
print("По возрастанию:", SorteeriNumbrid(numbrid))
print("По убыванию:", SorteeriNumbrid(numbrid, reverse=True))
