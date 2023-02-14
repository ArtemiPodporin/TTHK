from MyModule import register, login, logout

login_list = []
password_list = []

while True:
    action = input("Enter '1' to register, '2' to log in, or '3' to log out: ")
    if action == '1':
        register(login_list, password_list)
    elif action == '2':
        login(login_list, password_list)
    elif action == '3':
        logout()
    else:
        print("Invalid action.")
