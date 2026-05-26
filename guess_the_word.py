import random

words = ["apple", "tiger", "chair", "robot", "green"]

word = random.choice(words)

guessed_letters = []
lives = 6

print("--------- Welcome to Hangman Game! ---------")

while lives > 0:

    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct Guess!")
    else:
        lives -= 1
        print("Wrong Guess!")
        print("Lives remaining:", lives)


if lives == 0:
    print("\nGame Over!")
    print("The word was:", word)
