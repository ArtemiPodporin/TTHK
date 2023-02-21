from MyModule import register, authorize, change, forgotpassword, logout

while True:
    print("Valige:")
    print("1. Registreerima")
    print("2. Logi sisse")
    print("3. Muudata login voi salasõna")
    print("4. Unustasid salasone")
    print("5. Logi välja")
    choice = input("Sisesta number (1-5): ")

    if choice == '1':
        register()
    elif choice == '2':
        authorize()
    elif choice == '3':
        change()
    elif choice == '4':
        forgotpassword()
    elif choice == '5':
        logout()
        break
    else:
        print("Viga! Palun andke number 1st kuni 5ni.")
