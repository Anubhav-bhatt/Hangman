import random

# Hangman stages
stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']

# Word list
word_list = ["anubhav", "vyshu", "aditya"]

# Game setup
lives = 6
chosen_word = random.choice(word_list)
print(f"(DEBUG: The word is {chosen_word})")  # remove in final version

# Create placeholders
display = "_" * len(chosen_word)
print(display)

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    # To rebuild the display with correct guesses
    new_display = ""
    for letter in chosen_word:
        if letter == guess:
            new_display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            new_display += letter
        else:
            new_display += "_"

    display = new_display
    print(display)

    # Wrong guess check
    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong guess. You lose a life. Lives left: {lives}")
        if lives == 0:
            game_over = True
            print("You lose 😢")
            print(f"The word was: {chosen_word}")

    # Win check
    if "_" not in display:
        game_over = True
        print("You win 🎉")

    # Print current hangman stage
    print(stages[lives])
