from MyModule import register, login, logout

list_of_logins = []
list_of_passwords = []

while True:
    действие = input("Нажми: '1' чтобы зарегистрироватся, '2' чтобы войти, или '3' чтобы выйти: ")
    if действие == '1':
        register(list_of_logins, list_of_passwords)
    elif действие == '2':
        login(list_of_logins, list_of_passwords)
    elif действие == '3':
        logout()
    else:
        print("чё?")
