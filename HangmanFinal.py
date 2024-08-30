import random

# Hangman stages
stages = ['''

      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
  ___|___
  ''', '''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
  ___|___
  ''', '''
      _______
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
  ___|___
  ''', '''
      _______
     |/      |
     |      (_)
     |       |
     |       
     |      
     |
  ___|___
  ''', '''
      _______
     |/      |
     |      (_)
     |      
     |     
     |      
     |
  ___|___
  ''', ''' 
      _______
     |/      |
     |      
     |      
     |      
     |      
     |
  ___|___
  ''', '''
      _______
     |/      |
     |      
     |      
     |      
     |      
     |
  ___|___
  ''' ]

names = ["sohani", "utsav", "satyam", "aman"]
lives = 6

# Randomly choose a word
chosen_word = random.choice(names)
word_length = len(chosen_word)
print("The word has", word_length, "letters.")

# Create a placeholder with blanks
placeholder = "_" * word_length
print(placeholder)

# Track the correct guesses
correct_letters = []

game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()

    # Validate the guess (should be a single letter)
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a valid single letter.")
        continue

    if guess in correct_letters:
        print("You already guessed that letter.")
        continue

    # Update the display with correct guesses
    display = ""
    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    # Check if guess is wrong
    if guess not in chosen_word:
        lives -= 1
        print("Wrong guess! Lives left:", lives)
        if lives == 0:
            game_over = True
            print("You lose! The word was:", chosen_word)

    # Check if the word is fully guessed
    if "_" not in display:
        game_over = True
        print("You Win! The word was:", chosen_word)

    print(stages[lives])
