import string
from random import choice

def random_salasona(k: int):
    sala=""
    for i in range(k):
        t=choice(string.ascii_letters) #Aa...Zz
        num=choice([1,2,3,4,5,6,7,8,9,0])
        t_num=[t,str(num)]
        sala+=choice(t_num)         
    return sala

def register(list_of_logins, list_of_passwords):
    login = input("Выбери себе логин: ")
    while login in list_of_logins:                                                                             
        login = input("Такой логин уже есть! Выбери новый: ")
    password_type = input("Набери '1' чтобы сгенерировать, или '2' чтобы написать самому: ")
    if password_type == '1':
        password = random_salasona(8)
        print("Ваш рандом пароль:", password)
    else:
        password = input("Выбери себе пароль: ")
    list_of_logins.append(login)
    list_of_passwords.append(password)
    print("Вы зарегистрировались!")

def login(list_of_logins, list_of_passwords):
    login = input("Вход: Введи свой логин: ")
    password = input("Вход: Ввежи свой пароль: ")
    if login in list_of_logins and password == list_of_passwords[list_of_logins.index(login)]:
        print("Вы успешно вошли!")
    else:
        print("Что-то неправильно!!")

def logout():
    print("Вы вышли.")
