
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

