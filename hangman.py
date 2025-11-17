import random
import time

def hangman_demo():
    words = ['apple', 'house', 'table', 'river', 'plant']
    word = random.choice(words)  # Randomly select a word
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6

    print("Welcome to Hangman!")
    print("_ " * len(word))
    print(f"You have {max_incorrect} chances to guess wrong.")

    while incorrect_guesses < max_incorrect:
        guess = input("\nGuess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
        else:
            incorrect_guesses += 1
            print(f"Wrong! {max_incorrect - incorrect_guesses} guesses left.")

        # Display current progress
        display_word = ''
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + ' '
            else:
                display_word += '_ '
        print(display_word.strip())
        time.sleep(1)

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word:", word)
            break
    else:
        print("Game over! The word was:", word)

hangman_demo()