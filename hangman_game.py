import random 
import os
import sys
import time

def words_from_file():
    try:    
        f = open("countries-and-capitals.txt", 'r', encoding='utf-8') 
        content = f.read()
        f.close()
    except:
        print("There is an error!")

    words = content.replace('\n', '|').split('|') 
    words = [word.strip() for word in words if word.strip()] 

    return words

def display_hangman(lives, max_lives):
    stages = [
        """
            --------
            |      |
            |      O   
            |     /|\\  
            |     / \\
            |
         xxxxxxxxxxx
        xxxxxxxxxxxxxxxx
        """,
        """
            --------
            |      |
            |      O   
            |     /|\\  
            |     / 
            |
         xxxxxxxxxxx
        xxxxxxxxxxxxxxxx
        """,
        """
            --------
            |      |
            |      O   
            |     /|\\  
            |     
            |
         xxxxxxxxxxx
        xxxxxxxxxxxxxxxx
        """,
        """
            --------
            |      |
            |      O   
            |     /|
            |     
            |
         xxxxxxxxxxx
        xxxxxxxxxxxxxxxx
        """,
        """
            --------
            |      |
            |      O   
            |      | 
            |   
            |
         xxxxxxxxxxx
        xxxxxxxxxxxxxxxx
        """,
        """
            --------
            |      |
            |      O   
            |     
            |    
            |
         xxxxxxxxxxx
        xxxxxxxxxxxxxxxx
        """,
        """
            --------
            |      |
            |       
            |     
            |    
            |
         xxxxxxxxxxx
        xxxxxxxxxxxxxxxx
        """,
        """
            --------
            |      
            |        
            |      
            |     
            |
         xxxxxxxxxxx
        xxxxxxxxxxxxxxxx
        """
    ]
    index = max(0, len(stages) - 1 - (max_lives - lives))
    print(stages[index])

def animated_print(text):
    for item in text:
        sys.stdout.write(item)
        sys.stdout.flush()
        time.sleep(0.5)

def quit():
    os.system("cls")
    animated_print("GAME OVER!")

def exit_game():
    os.system("cls")
    print("Thank you for playing! See you later!")

def choose_difficulty():
    difficulties = { "1" : ("easy", 7), "2" : ("medium", 6), "3" : ("hard", 5)}

    while True:
        print("\nChoose difficulthy level!")
        for key, (name, _) in difficulties.items():
            print(f"{key}: {name}")
        
        choice = input("Enter a number: ")
        if choice in difficulties:
            return choice, difficulties[choice][1]
        else:
            print("Invalid choice! Try again! ")

def filter_words_from_difficulty(words, difficulty):
    if difficulty == "1":
        return [word for word in words if len(word) <= 6]
    elif difficulty == "2":
        return [word for word in words if 7 <= len(word) <= 9]
    elif difficulty == "3":
        return [word for word in words if 10 <= len(word)]
    return words

def play():
    all_words = words_from_file()
    difficulty, max_lives = choose_difficulty()
    filtered_words = filter_words_from_difficulty(all_words, difficulty)

    random_word = random.choice(filtered_words)
    hidden_word = ["_" if char.isalpha() else char for char in random_word]
    lives = max_lives
    guessed_letters = set()

    print("\nThe game has begun!")
    print("".join(hidden_word))

    while lives > 0 and "_" in hidden_word:
        guess = input("\nEnter a letter: ").strip()

        if guess in guessed_letters:
            print("You have tried this letter before!")
            continue

        if guess.lower() != "help":
            guessed_letters.add(guess)

        os.system('cls')
        print("guessed letters: ", guessed_letters)

        if guess.lower() == "help":
            help = [i for i, char in enumerate(hidden_word) if char == "_"]
            if help:
                index = random.choice(help)
                hidden_word[index] = random_word[index]
                
        if not guess.isalpha() or len(guess) != 1 and guess.lower != "help":
            print("You can only enter one letter!")

        if guess.lower() == "quit":
            quit()
            break
        
        guess = guess.upper()

        if any(char.upper() == guess for char in random_word):
            for index, char in enumerate(random_word):
                if char.upper() == guess:
                    hidden_word[index] = char
            print("You hit it!")
        else:
            lives -= 1
            print(f"Wrong letter! Remaining lives: {lives}")
            print("Do you need a help? Write 'help'")
        
        display_hangman(lives, max_lives)
        print(" ".join(hidden_word))
        
    if "_" not in hidden_word:
        print("\nCongratulations! You guessed the word!", random_word)
        menu()
    else:
        print("\nUnfortunately you lost! That was the word: ", random_word)
        menu()
    
def menu():
    time.sleep(5)
    os.system("cls")
    print("MENÜ: \nPLAY - press p\nEXIT - press e")
    selected = input("Choose: ")
    if selected.lower() == "p":
        play()
    elif selected.lower() == "e":
        exit_game()
        
while True:
    menu()
    break