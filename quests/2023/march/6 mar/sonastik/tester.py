from funktsioonid import translate, add_word, edit_word, test_knowledge

# main.py
while True:
        print("\nOptions:")
        print("1. Translate from Estonian to Russian")
        print("2. Translate from Russian to Estonian")
        print("3. Add a new word to dictionary")
        print("4. Edit an existing word in dictionary")
        print("5. Test knowledge of words")
        print("6. Quit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            word = input("Enter word to translate: ").strip()
            result = translate(word, "est", "rus")
            print(result)
        elif choice == "2":
            word = input("Enter word to translate: ").strip()
            result = translate(word, "rus", "est")
            print(result)
        elif choice == "3":
            from_word = input("Enter word in original language: ").strip()
            to_word = input("Enter translation: ").strip()
            result = add_word(from_word, to_word, "est", "rus")
            print(result)
        elif choice == "4":
            word = input("Enter word to edit: ").strip()
            new_translation = input("Enter new translation: ").strip()
            result = edit_word(word, new_translation, "est", "rus")
            print(result)
        elif choice == "5":
            num_questions = int(input("Enter number of questions: "))
            result = test_knowledge(num_questions, "est", "rus")
            print(result)
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")
