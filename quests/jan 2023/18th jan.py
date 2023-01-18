from random import *
from math import *
#Пятый вариант


# Задание 1
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


print()
print()

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


# Задание 3
import random

# Number of students
num_students = randint(5, 15)

# List to store student grades
grades = []

# Generate random grades for each student
for i in range(num_students):
    grade = random.randint(0, 100)
    grades.append(grade)

# Initialize minimum and maximum grade as the first grade
min_grade = grades[0]
max_grade = grades[0]

# Iterate through the list of grades
for grade in grades:
    # Compare current grade with minimum grade
    if grade < min_grade:
        min_grade = grade
    # Compare current grade with maximum grade
    if grade > max_grade:
        max_grade = grade

# Print the minimum and maximum grades
print(f"Minimum grade: {min_grade}")
print(f"Maximum grade: {max_grade}")
