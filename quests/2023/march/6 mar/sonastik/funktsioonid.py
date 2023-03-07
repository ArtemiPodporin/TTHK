#
#
# Написал на английском из-за рефлексов и лёгкости, потом переведу
#
#
#
#
#
#


# Import necessary libraries
import random


# Define file paths
ESTONIAN_DICT_PATH = "est.txt"
RUSSIAN_DICT_PATH = "rus.txt"

# Define translation functions
def translate(word, from_language, to_language):
    if from_language == "est" and to_language == "rus":
        dict_path = ESTONIAN_DICT_PATH
    elif from_language == "rus" and to_language == "est":
        dict_path = RUSSIAN_DICT_PATH
    else:
        return "Unsupported languages"
    
    with open(dict_path, "r", encoding="utf-8") as dict_file:
        for line in dict_file:
            terms = line.strip().split("=")
            if len(terms) == 2:
                if from_language == "est":
                    if word == terms[0]:
                        return terms[1]
                elif from_language == "rus":
                    if word == terms[1]:
                        return terms[0]
    return "Word not found in dictionary"

# Define function to add new words to dictionary
def add_word(from_word, to_word, from_language, to_language):
    if from_language == "est" and to_language == "rus":
        dict_path = ESTONIAN_DICT_PATH
    elif from_language == "rus" and to_language == "est":
        dict_path = RUSSIAN_DICT_PATH
    else:
        return "Unsupported languages"
    
    with open(dict_path, "a", encoding="utf-8") as dict_file:
        dict_file.write(f"\n{from_word}={to_word}")
    
    return "Word added to dictionary"

# Define function to edit existing words in dictionary
def edit_word(word, new_translation, from_language, to_language):
    if from_language == "est" and to_language == "rus":
        dict_path = ESTONIAN_DICT_PATH
    elif from_language == "rus" and to_language == "est":
        dict_path = RUSSIAN_DICT_PATH
    else:
        return "Unsupported languages"
    
    with open(dict_path, "r", encoding="utf-8") as dict_file:
        lines = dict_file.readlines()
    
    found_word = False
    with open(dict_path, "w", encoding="utf-8") as dict_file:
        for line in lines:
            terms = line.strip().split("=")
            if len(terms) == 2:
                if from_language == "est":
                    if word == terms[0]:
                        dict_file.write(f"{word}={new_translation}\n")
                        found_word = True
                    else:
                        dict_file.write(line)
                elif from_language == "rus":
                    if word == terms[1]:
                        dict_file.write(f"{new_translation}={word}\n")
                        found_word = True
                    else:
                        dict_file.write(line)
            else:
                dict_file.write(line)
    
    if found_word:
        return "Word edited in dictionary"
    else:
        return "Word not found in dictionary"

# Define function to test knowledge of words
def test_knowledge(num_questions, from_language, to_language):
    if from_language == "est" and to_language == "rus":
        dict_path = ESTONIAN_DICT_PATH
    elif from_language == "rus" and to_language == "est":
        dict_path = RUSSIAN_DICT_PATH
    else:
        return "Unsupported languages"
    
    with open(dict_path, "r", encoding="utf-8") as dict_file:
        lines = dict_file.readlines()
    
    questions = random.sample(lines, min(num_questions, len(lines)))
    num_correct = 0
    for question in questions:
        terms = question.strip().split("=")
        if len(terms) == 2:
            if from_language == "est":
                prompt = f"Mis on venekeelne tõlge '{terms[0]}'? "
                correct_answer = terms[1]
            elif from_language == "rus":
                prompt = f"Mis on eestikeelne tõlge '{terms[1]}'? "
                correct_answer = terms[0]
            
            user_answer = input(prompt)
            if user_answer == correct_answer:
                num_correct += 1
                print("Correct!")
            else:
                print(f"Vale. Õige vastus on '{correct_answer}'")
    
    percent_correct = num_correct / len(questions) * 100
    return f"{num_correct}/{len(questions)} ({percent_correct:.2f}%) answers were correct"