﻿import string
from random import choice

# luua tühjad nimekirjad login ja paroolid
logins = []
passwords = []

# funktsioon juhusliku parooli genereerimiseks
def salasona(k: int):
  sala=""
  for i in range(k):
   t=choice(string.ascii_letters) #Aa...Zz
   num=choice([1,2,3,4,5,6,7,8,9,0])
   t_num=[t,str(num)]
   sala+=choice(t_num)
  return sala

# funktsioon kasutaja registreerimiseks
def register():
    login = input("Sisesta oma login: ")
    if login in logins:
        print("See login on juba votud.")
        return
    password_choice = input("Kas sa tahad juhuslik salasone? (Y/N): ")
    if password_choice.lower() == 'y':
        password = salasona(8)
        print(f"Sinu salasona: {password}")
    else:
        while True:
            password = input("Sisesta oma salasona: ")
            if any(char.isdigit() for char in password) and any(char.islower() for char in password) and any(char.isupper() for char in password) and any(char in string.punctuation for char in password):
                break
            else:
                print("Teie parool peab sisaldama vähemalt ühte numbrit, ühte väiketähte, ühte suurtähte ja ühte erilist sümbolit.")
    logins.append(login)
    passwords.append(password)
    print("Registreerimine õnnetus!")

# funktsioon kasutaja autoriseerimiseks
def authorize():
    login = input("Sisesta oma login: ")
    if login not in logins:
        print("See logini pole registreeritud.")
        return
    password = input("Sisesta oma salasona: ")
    if password != passwords[logins.index(login)]:
        print("Vale salasona.")
        return
    print("Login õnnetus!")

# funktsioon nime või parooli muutmiseks
def change():
    login = input("Sisesta oma login: ")
    if login not in logins:
        print("See nimi ei ole registreeritud.")
        return
    password = input("Mis on sinu salasona: ")
    if password != passwords[logins.index(login)]:
        print("Vale salasona.")
        return
    choice = input("Kas soovite muuta oma nime või parooli? (login/password): ")
    if choice.lower() == 'login':
        new_login = input("Sisesta uue login: ")
        if new_login in logins:
            print("See login on juba võtud.")
            return
        logins[logins.index(login)] = new_login
        print("Login muudatus õnnetus.")
    elif choice.lower() == 'password':
        while True:
            new_password = input("Sisesta uue salasone: ")
            if any(char.isdigit() for char in new_password) and any(char.islower() for char in new_password) and any(char.isupper() for char in new_password) and any(char in string.punctuation for char in new_password):
                break
            else:
                print("Teie parool peab sisaldama vähemalt ühte numbrit, ühte väiketähte, ühte suurtähte ja ühte erilist sümbolit.")
        passwords[logins.index(login)] = new_password
        print("Salasone muudatus õnnetus.")
    else:
        print("Viga.")

# funktsioon unustatud parooli taastamiseks
def forgotpassword():
    login = input("Наберите свой логин: ")
    if login not in logins:
        print("Вы не зарегистрированы.")
        return
    new_password = salasona(8)
    passwords[logins.index(login)] = new_password
    print(f"Sinu uus parool on: {new_password}")

# funktsioon välja logimiseks
def logout():
    print("Sa logisid välja.")
    