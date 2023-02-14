import string
from random import choice

def salasona(k: int):
    sala=""
    for i in range(k):
        t=choice(string.ascii_letters) #Aa...Zz
        num=choice([1,2,3,4,5,6,7,8,9,0])
        t_num=[t,str(num)]
        sala+=choice(t_num)
    return sala

def register(login_list, password_list):
    login = input("Выбери себе логин: ")
    while login in login_list:
        login = input("Такой логин уже есть! Выбери новый: ")
    password_type = input("Набери '1' чтобы сгенерировать, или '2' чтобы написать самому: ")
    if password_type == '1':
        password = salasona(8)
    else:
        password = input("Выбери себе пароль: ")
    login_list.append(login)
    password_list.append(password)
    print("Вы зарегистрировались!")

def login(login_list, password_list):
    login = input("Enter your login: ")
    password = input("Enter your password: ")
    if login in login_list and password == password_list[login_list.index(login)]:
        print("You have successfully logged in.")
    else:
        print("Incorrect login or password.")

def logout():
    print("Вы вышли.")
