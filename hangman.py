# Task 1: Hangman Game - CodeAlpha Python Internship
# Student ID: CA/DF1/174377

import random

def hangman():
    words = ["python", "developer", "hangman", "internship", "coding"]
    word = random.choice(words)
    guessed = ["_"] * len(word)
    attempts = 6
    guessed_letters = []

    print("=== Hangman Game ===")
    print("Guess the word! You have 6 attempts.")

    while attempts > 0 and "_" in guessed:
        print("\nWord:", " ".join(guessed))
        print(f"Attempts left: {attempts}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")

        guess = input("Guess a letter: ").lower()

        if len(guess)!= 1 or not guess.isalpha():
            print("❌ Sirf ek letter daalo!")
            continue

        if guess in guessed_letters:
            print("❌ Ye letter pehle hi try kar chuke ho!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Sahi pakde hain!")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
        else:
            print("❌ Galat! Ek attempt kam ho gaya.")
            attempts -= 1

    if "_" not in guessed:
        print(f"\n🎉 Jeet gaye! Word tha: {word}")
    else:
        print(f"\n💀 Haar gaye! Word tha: {word}")

hangman()
