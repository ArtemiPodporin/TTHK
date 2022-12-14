
from math import *
from random import *

#1
num = int(input("Enter a number: "))
if num >= 0:
    if num % 2 == 0:
        print("Чётное")
else:
    print("Нечётное")

#2
num1 = int(input("Первый номер: "))
num2 = int(input("Второй номер: "))
num3 = int(input("Третий номер: "))
if num1 > 0 and num2 > 0 and num3 > 0:
    if num1 + num2 + num3 == 180:
        # Check if the triangle is equilateral, isosceles, or scalene
        if num1 == num2 and num2 == num3:
            print("Цифры обозначают углы равностороннего треугольника.")
        elif num1 == num2 or num1 == num3 or num2 == num3:
            print("Цифры обозначают углы равнобедренного треугольника.")
        else:
            print("Цифры обозначают углы разностороннего треугольника.")
    else:
        print("Не углы!")
else:
    print("Ошибка!")

#3
kusimus = input("Хочешь узнать день недели? ")
if kusimus.lower() == "jah":
  number = input("Введите число от 1 до 7: ")
  if number.isdigit() and 1 <= int(number) <= 7:
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    print(f"день недели: {days[int(number)-1]}")
  else:
    print("Ошибка!")
else:
  print("ок пока")

#4
день = int(input("ДЕНЬ рождения: "))
месяц = input("МЕСЯЦ рожения: ")
if месяц == 'декабрь':
	знак = 'стрелец' if (день < 22) else 'козерог'
elif месяц == 'январь':
	знак = 'козерог' if (день < 20) else 'водолей'
elif месяц == 'февраль':
	знак = 'водолей' if (день < 19) else 'рыбы'
elif месяц == 'март':
	знак = 'рыбы' if (день < 21) else 'овен'
elif месяц == 'апрель':
	знак = 'овен' if (день < 20) else 'телец'
elif месяц == 'май':
	знак = 'телец' if (день < 21) else 'близнецы'
elif месяц == 'июнь':
	знак = 'близнецы' if (день < 21) else 'рак'
elif месяц == 'июль':
	знак = 'рак' if (день < 23) else 'лев'
elif месяц == 'август':
	знак = 'лев' if (день < 23) else 'дева'
elif месяц == 'сентябоь':
	знак = 'дева' if (день < 23) else 'весы'
elif месяц == 'октябрь':
	знак = 'весы' if (день < 23) else 'скорпион'
elif месяц == 'ноябрь':
	знак = 'скорпион' if (день < 22) else 'стрелец'
print("твой знак :",знак)
