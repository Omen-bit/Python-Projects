import random


logo = """
88          88                       88        88                       88         
88          88                       88        ""                       88         
88          88                       88                                 88         
88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                              ,88                                  
                                            888P"                                  
"""
print("Welcome to Blackjack")
print(logo)

def fix_ace(cards,score):
    while score>21 and 11 in cards:
        cards[cards.index(11)]=1
        score=sum(cards)
    return score

def calculate(Usercard,comcard,current_sum,com_sum):
    gameOn=True
    while gameOn:
        choice = input("Type 'y' to get another card and 'n' to pass: ")
        if choice == "y":
            New_card=random.choice(card)
            Usercard.append(New_card)
            current_sum+=New_card

            current_sum=fix_ace(Usercard,current_sum)

            if current_sum > 21:
                print(f"Your final hand : {Usercard} ,final score : {current_sum}")
                print(f"Computers final hand : {comcard}")
                return "You loose"
            else:
                print(f"your cards : {Usercard}, current Score : {current_sum}")
                print(f"Computers first card : {comcard}")

        elif choice=="n":
            while com_sum<17:
                new_card=random.choice(card)
                comcard.append(new_card)
                com_sum+=new_card

            com_sum=fix_ace(comcard,com_sum)

            if current_sum>com_sum or com_sum>21:
                print(f"Your final hand : {Usercard} ,final score : {current_sum}")
                print(f"Computers final hand : {comcard} ,final score : {com_sum}")
                return "you Win"
            elif current_sum==com_sum:
                print(f"Your final hand : {Usercard} ,final score : {current_sum}")
                print(f"Computers final hand : {comcard} ,final score : {com_sum}")
                return "Draw"
            else:
                print(f"Your final hand : {Usercard} ,final score : {current_sum}")
                print(f"Computers final hand : {comcard} ,final score : {com_sum}")
                return "you lose"


card=[11,2,3,4,5,6,7,8,9,10,10,10,10]
current_sum= 0
com_sum = 0
game_over=True
while game_over:

    comcard = [random.choice(card), ]
    Usercard = [random.choice(card), random.choice(card), ]

    current_sum=sum(Usercard)
    com_sum = sum(comcard)

    print(f"your cards : {Usercard}, current Score : {current_sum}")
    print(f"Computers first card : {comcard}")

    result=calculate(Usercard,comcard,current_sum,com_sum)
    print(result)
    interest=input("Do you want to keep playing this game type 'y' for yes and 'n' for no : ").lower()
    if interest=="y":
        print("\n" * 100)
        print(logo)
    else:
        game_over=False


