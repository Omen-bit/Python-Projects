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

fruits=["apple","banana","pineapple","blueberry"]
fruit=random.choice(fruits)
print(fruit)

word=len(fruit)

placeholder=""
for i in range(word):
    placeholder += "_"
print(placeholder)

game_over=False
lives=6
counter=[]
while not game_over:
    guess=input("Guess a letter: ").lower()
    display = ""
    for letter in fruit:
        if letter==guess:
            display+=letter
            counter.append(guess)
        elif letter in counter:
            display+=letter
        else:
            display+="_"
    print(display)

    if guess not in fruit:
        lives-=1

    print(stages[lives])
    if lives == 0:
        print("Game Over")
        game_over=True

    if "_" not in display:
        game_over=True
        print("You Win")