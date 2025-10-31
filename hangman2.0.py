import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
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
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''',]

words=["apple", "house", "tiger", "phone", "brain", "smile", "river", "table", "pizza", "rainbow", "bicycle", "monster", "journey", "village", "laptop", "diamond", "curtain", "picture", "airport",  "astronaut", "crocodile", "knowledge", "nightmare", "blueprint", "whispering", "avalanche", "microwave", "rectangle", "volcano" ]

Random_word=random.choice(words)
print(Random_word)

for letters in range(len(Random_word)):
    print("_", end="")

game_over = False
container = []
lives=6

while not game_over:
    display = ""
    guess = input("\nGuess a letter: ")

    if guess not in container:
        container.append(guess)

    if guess not in Random_word:
        lives-=1

    print(stages[lives])

    for i in range(len(Random_word)):
        if guess==Random_word[i]:
            print(guess,end="")
            display+=guess
        elif Random_word[i] in container:
            print(Random_word[i],end="")
        else:
            print("_",end="")
            display+="_"

    if "_" not in display:
            game_over = True

    if lives==0:
        game_over=True








