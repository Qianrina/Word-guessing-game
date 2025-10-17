import random
import pygame

# Initialize pygame and the mixer for playing sounds
pygame.init()
pygame.mixer.init()

# List of words for the guessing game
word_bank = ['panda', 'cat', 'wolf', 'monkey', 'penguin','kangaroo']

# Select a random word from the word bank
word = random.choice(word_bank)
guessedWord = ['_'] * len(word)
attempts = 10

# Load sound effects
Win_sound = pygame.mixer.Sound('Win.mp3')
Lose_sound = pygame.mixer.Sound('Lose.mp3')
Caution_sound = pygame.mixer.Sound('Caution.mp3')

print("Welcome to the Word Guessing Game!")
print("Category: Animals")
print(" ".join(guessedWord))
print(f"You have {attempts} attempts in total.\n")

# Main game loop: runs while player has attempts left
while attempts > 0:
    guess = input("Please enter your guess (a single letter): ").strip().lower()

    if len(guess) != 1:
        print("Invalid input. Please enter a single letter.")
        continue

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessedWord[i] = guess
        print("Good guess!")
    else:
        print("Wrong guess.")
    
    # Reduce attempts by 1 after each input
    attempts -= 1

    print(" ".join(guessedWord))

    # Check if the player has guessed the full word
    if "_" not in guessedWord:
        print("Congratulations! You've guessed the word:", word)
        Win_sound.play()  # Play win sound
        break

    # Display remaining attempts and play caution sound if low
    if attempts > 0:
        if attempts <= 3:
            print(f"Warning: You have only {attempts} attempts left! Be careful!\n")
            Caution_sound.play()  # Play caution sound
        else:
            print(f"You have {attempts} attempts left.\n")

# Player failed to guess the word
if attempts == 0:
    print("Sorry, you've run out of attempts. The word was:", word)
    Lose_sound.play()  # Play lose sound

pygame.time.wait(2000)  