import random
import est.txt
import rus.txt

def test_words(lang):
    if lang == "est":
        source_list = est
        target_list = rus
    elif lang == "rus":
        source_list = rus
        target_list = est
    else:
        return "Unsupported language"

    correct = 0
    total = 0

    while True:
        word = random.choice(source_list)
        index = source_list.index(word)
        expected_translation = target_list[index]

        print(f"What is the translation of '{word}'?")
        answer = input("> ")

        if answer == expected_translation:
            print("Correct!")
            correct += 1
        else:
            print(f"Incorrect. The correct translation is '{expected_translation}'.")

        total += 1

        print(f"You have answered {correct} out of {total} correctly.")

        if input("Do you want to continue? (y/n) ").lower() != "y":
            break

    print(f"You answered {correct} out of {total} correctly ({correct / total * 100:.2f}%).")

