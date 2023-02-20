from MyModule import register, login, logout

logins = []
passwords = []

while True:
    действие = input("Нажми: '1' чтобы зарегистрироватся, '2' чтобы войти, или '3' чтобы выйти: ")
    if действие == '1':
        register(logins, passwords)
    elif действие == '2':
        login(logins, passwords)
    elif действие == '3':
        logout()
    else:
        print("чё?")
