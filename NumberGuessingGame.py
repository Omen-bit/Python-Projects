import random
logo = """
 ,adPPYb,d8 88       88  ,adPPYba, ,adPPYba, ,adPPYba,  
a8"    `Y88 88       88 a8P_____88 I8[    "" I8[    ""  
8b       88 88       88 8PP"""""""  `"Y8ba,   `"Y8ba,   
"8a,   ,d88 "8a,   ,a88 "8b,   ,aa aa    ]8I aa    ]8I  
 `"YbbdP"Y8  `"YbbdP'Y8  `"Ybbd8"' `"YbbdP"' `"YbbdP"'  
 aa,    ,88                                             
  "Y8bbdP"   
"""

def calculate(choice,num):
    for i in range(choice,0,-1):
        print(f"You have {i} attempts remaining to guess a number")
        guess=int(input("Make a Guess: "))
        if guess != num:
            if guess>num:
                print("Too high")
            elif guess<num:
                print("Too low")
            print("Guess Again")
        elif guess==num:
            return (f"You got it the answer is {guess}")

    return "Out of guesses,You loose"

print(logo)
number=random.randint(1,100)
print("Welcome to number guessing game !!")
choice=input("choose a difficulty level, Type 'easy' or 'hard': ").lower()
if choice=="easy":
    result=calculate(10,number)
    print(result)
elif choice=="hard":
    result=calculate(5,number)
    print(result)