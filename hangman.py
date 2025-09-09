print(r'''
░█░█░█▀▀░█░░░█▀▀░█▀█░█▄█░█▀▀░░░▀█▀░█▀█░░░█░█░█▀█░█▀█░█▀▀░█▄█░█▀█░█▀█░░░
░█▄█░█▀▀░█░░░█░░░█░█░█░█░█▀▀░░░░█░░█░█░░░█▀█░█▀█░█░█░█░█░█░█░█▀█░█░█░░░
░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░░░░▀░░▀▀▀░░░▀░▀░▀░▀░▀░▀░▀▀▀░▀░▀░▀░▀░▀░▀░▀░
''')

from wonderwords import RandomWord
rw = RandomWord()

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


# Generate a random word
chosen_word = rw.word()
lives = 6
length = len(chosen_word)

# blanks
placeholder = ""
for i in range(length):
    placeholder += "_"
print(f"*******************************It's a {length}-letter word. Can you guess it?*******************************")
print(placeholder)

# userinput, loop, store correct letters
game_over = False
correct_letters = []
guessed_letters = []

while not game_over:
    
    guess = input("Enter a guess: ").lower()

    # check for double letters
    if guess in guessed_letters:
        print(f"You already tried {guess}. Try another")
        continue


    display = ""
    for letter in chosen_word:
        if guess == letter or letter in correct_letters:
            display += letter            
            
        else:
            display += "_"
    if guess in chosen_word and guess not in correct_letters:
        correct_letters.append(guess)
# lives
    if guess not in chosen_word:
        print("Wrong. Try again.")
        lives -= 1
        if lives == 0:
            game_over = True
            
            print(r'''
        ██████   █████  ███    ███ ███████      ██████  ██    ██ ███████ ██████  
        ██       ██   ██ ████  ████ ██          ██    ██ ██    ██ ██      ██   ██ 
        ██   ███ ███████ ██ ████ ██ █████       ██    ██ ██    ██ █████   ██████  
        ██    ██ ██   ██ ██  ██  ██ ██          ██    ██  ██  ██  ██      ██   ██ 
         ██████  ██   ██ ██      ██ ███████      ██████    ████   ███████ ██   ██ 
                                                                                 
                                                                                ''')
            print(f"The word was {chosen_word}")
    print(stages[lives])
    print(display)
    print(f"Lives remaining: {lives}")

    if "_" not in display:
        game_over = True
        print("you win.")


    
       