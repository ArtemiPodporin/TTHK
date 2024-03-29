﻿import math
import random

#1
def arithmetic(a, b, действие):
    if действие == '+':
        return a + b
    elif действие == '-':
        return a - b
    elif действие == '*':
        return a * b
    elif действие == '/':
        return a / b
    else:
        return "Неизвестная операция"
результат = arithmetic(2, 3, '+')
print("Прибовляем, результат будет", {результат}) # Результат: 5
результат = arithmetic(2, 3, '-')
print("Вычисляем, результат будет", {результат}) # Результат: -1
результат = arithmetic(2, 3, '*')
print("Умножаем, результат будет", {результат}) # Результат: 6
результат = arithmetic(2, 3, '/')
print("Делим, результат будет", {результат}) # Результат: 0.6666666666666666
результат = arithmetic(2, 3, '**')
print("Непонятный результат будет", {результат}) # Результат: "Неизвестная операция"

#2
def годВысок(год):
    if год % 400 == 0:
        return True
    elif год % 100 == 0:
        return False
    elif год % 4 == 0:
        return True
    else:
        return False


#3
def square(сторона):
    периметер = 4 * сторона
    зона = сторона * сторона
    диагональ = math.sqrt(2 * сторона * сторона)
    return периметер, зона, диагональ
# вычисляет периметр, умножая длину стороны на 4, площадь, возводя длину стороны в квадрат,
# и диагональ, находя квадратный корень из 2 * сторона * сторона
# используя функцию math.sqrt из математического модуля. Наконец, он возвращает все три значения в виде кортежа.


#4
def season(месяц):
    if месяц in [12, 1, 2]:
        return "talv"
    elif месяц in [3, 4, 5]:
        return "kevad"
    elif месяц in [6, 7, 8]:
        return "suvi"
    else:
        return "sügis"

#5
def bank(a, years):
    for i in range(years):
        a = a * 1.1
    return a
# a — первоначальная сумма депозита, а years — количество лет, в течение которых депозит будет удерживаться.
# Функция использует цикл for для многократного повторения по годам,
# и в каждой итерации она умножает a на 1,1, чтобы имитировать увеличение суммы депозита на 10% каждый год. 
# После всех итераций возвращается окончательное значение a, 
# которое представляет собой общую сумму на счете пользователя через указанное количество лет.

#6
def is_prime(цифра):
    if цифра < 2:
        return False
    for i in range(2, int(цифра ** 0.5) + 1):
        if цифра % i == 0:
            return False
    return True

#7
def date(день, месяц, год):
    if год < 0:
        return False
    if месяц not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
        return False
    if месяц in [1, 3, 5, 7, 8, 10, 12]:
        if день not in range(1, 32):
            return False
    elif месяц in [4, 6, 9, 11]:
        if день not in range(1, 31):
            return False
    elif год % 4 == 0 and (год % 100 != 0 or год % 400 == 0):
        if день not in range(1, 30):
            return False
    else:
        if день not in range(1, 29):
            return False
    return True

#8
def XOR_cipher(inputstring, ключ):
    """
    Функция XOR_cipher, которая принимает 2 аргумента: строку для шифрования и ключ шифрования,
    и возвращает строку, зашифрованную путем применения функции XOR (^) к символам строки с ключом.
    """
    inputstring = str(inputstring)
    ключ = str(ключ)
    input_string_length = len(inputstring)
    длинаКлюча = len(ключ)
    индексключа = 0
    encryptedstring = ""
    for буква in inputstring:
        if индексключа >= длинаКлюча:
            индексключа = 0
        encryptedstring += chr(ord(буква) ^ ord(ключ[индексключа]))
        индексключа += 1
    return encryptedstring

def XOR_uncipher(inputstring, ключ):
    """
    Функция XOR_uncipher, которая с помощью зашифрованной строки и ключа восстанавливает исходную строку.
    """
    inputstring = str(inputstring)
    ключ = str(ключ)
    input_string_length = len(inputstring)
    длинаКлюча = len(ключ)
    индексключа = 0
    decryptedstring = ""
    for char in inputstring:
        if индексключа >= длинаКлюча:
            индексключа = 0
        decryptedstring += chr(ord(char) ^ ord(ключ[индексключа]))
        индексключа += 1
    return decryptedstring