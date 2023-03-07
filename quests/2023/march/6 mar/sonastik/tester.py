from funktsioonid import translate, add_word, edit_word, test_knowledge

# main.py
while True:
        print("\nValikud:")
        print("1. Tõlgi eesti keelest vene keelde")
        print("2. Tõlgi vene keelest eesti keelde")
        print("3. Lisage sõnastikku uus sõna")
        print("4. Muutke sõnastikus olemasolevat sõna")
        print("5. Testige sõnade tundmist")
        print("6. Lõpeta")
        
        valik = input("Sisestage oma valik: ")
        if valik == "1":
            sona = input("Sisestage tõlgitav sõna: ").strip()
            result = translate(sona, "est", "rus")
            print(result)
        elif valik == "2":
            sona = input("Sisestage tõlgitav sõna: ").strip()
            result = translate(sona, "rus", "est")
            print(result)
        elif valik == "3":
            from_word = input("Sisestage sõna originaalkeeles: ").strip()
            to_word = input("Sisestage tõlge: ").strip()
            result = add_word(from_word, to_word, "est", "rus")
            print(result)
        elif valik == "4":
            sona = input("Sisestage muutmiseks sõna: ").strip()
            new_translation = input("Sisestage uus tõlge: ").strip()
            result = edit_word(sona, new_translation, "est", "rus")
            print(result)
        elif valik == "5":
            num_questions = int(input("Sisestage küsimuste arv: "))
            result = test_knowledge(num_questions, "est", "rus")
            print(result)
        elif valik == "6":
            print("Programmist väljumine...")
            break
        else:
            print("Vale valik. Palun proovi uuesti.")
