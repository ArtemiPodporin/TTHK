from random import *
from math import *
#Пятый вариант

#Задание 1
n = int(input("Mitu plaju kodu? (1-9): "))

for i in range(n):
    print("  ~~~~~  ", end=' ')
    if i == n-1:
        print("")

for i in range(n):
    print(" /_____\\ ", end=' ')
    if i == n-1:
        print("")

for i in range(n):
    print(" | []  | ", end=' ')
    if i == n-1:
        print("")

for i in range(n):
    print("  -----  ", end=' ')
    if i == n-1:
        print("")

#Задание 2
оценки_класс1 = []
оценки_класс2 = []
# Оценки классов
for i in range(4):
    оценка = float(input(f"Дай оценку ученику {i+1} в классе 1: "))
    оценки_класс1.append(оценка)
for i in range(4):
    оценка = float(input(f"Дай оценку ученику {i+1} в классе 2: "))
    оценки_класс2.append(оценка)
# Вычисление средних оценок
средняя_класс1 = sum(оценки_класс1) / len(оценки_класс1)
средняя_класс2 = sum(оценки_класс2) / len(оценки_класс2)
# Среднии оценки
print(f"Средная оценка в первом классе: {средняя_класс1}")
print(f"Средная оценка в втором классе: {средняя_класс2}")
