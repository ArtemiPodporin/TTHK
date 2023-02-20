import string
from random import choice

# initialize empty lists for logins and passwords
logins = []
passwords = []

# function for generating a random password
def salasona(k: int):
  sala=""
  for i in range(k):
   t=choice(string.ascii_letters) #Aa...Zz
   num=choice([1,2,3,4,5,6,7,8,9,0])
   t_num=[t,str(num)]
   sala+=choice(t_num)
  return sala

# function for user registration
def register():
    login = input("Enter your name: ")
    if login in logins:
        print("This name is already taken.")
        return
    password_choice = input("Would you like to generate a password? (Y/N): ")
    if password_choice.lower() == 'y':
        password = salasona(8)
        print(f"Your password is: {password}")
    else:
        while True:
            password = input("Enter your password: ")
            if any(char.isdigit() for char in password) and any(char.islower() for char in password) and any(char.isupper() for char in password) and any(char in string.punctuation for char in password):
                break
            else:
                print("Your password must contain at least one number, one lowercase character, one uppercase character, and one special symbol.")
    logins.append(login)
    passwords.append(password)
    print("Registration complete.")

# function for user authorization
def authorize():
    login = input("Enter your name: ")
    if login not in logins:
        print("This name is not registered.")
        return
    password = input("Enter your password: ")
    if password != passwords[logins.index(login)]:
        print("Incorrect password.")
        return
    print("Authorization successful.")

# function for changing name or password
def change():
    login = input("Enter your name: ")
    if login not in logins:
        print("This name is not registered.")
        return
    password = input("Enter your password: ")
    if password != passwords[logins.index(login)]:
        print("Incorrect password.")
        return
    choice = input("Would you like to change your name or password? (login/password): ")
    if choice.lower() == 'login':
        new_login = input("Enter your new name: ")
        if new_login in logins:
            print("This name is already taken.")
            return
        logins[logins.index(login)] = new_login
        print("Name change successful.")
    elif choice.lower() == 'password':
        while True:
            new_password = input("Enter your new password: ")
            if any(char.isdigit() for char in new_password) and any(char.islower() for char in new_password) and any(char.isupper() for char in new_password) and any(char in string.punctuation for char in new_password):
                break
            else:
                print("Your password must contain at least one number, one lowercase character, one uppercase character, and one special symbol.")
        passwords[logins.index(login)] = new_password
        print("Password change successful.")
    else:
        print("Invalid choice.")

# function for restoring forgotten password
def forgotpassword():
    login = input("Наберите свой логин: ")
    if login not in logins:
        print("Вы не зарегистрированы.")
        return
    new_password = salasona(8)
    passwords[logins.index(login)] = new_password
    print(f"Your new password is: {new_password}")

# function for logging out
def logout():
    print("Вы вышли.")
    
