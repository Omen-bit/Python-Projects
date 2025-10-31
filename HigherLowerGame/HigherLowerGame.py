import random
import os
from followers import data
from logo import art1,art2

def compare(compare_A):
    name = compare_A["name"]
    description = compare_A["description"]
    country = compare_A["country"]
    return f"Compare A : {name},{description} from {country}"

def against(Against_B):
    name = Against_B["name"]
    description = Against_B["description"]
    country = Against_B["country"]
    return f"Against B : {name},{description} from {country}"


compare_A = random.choice(data)
score=True
current_score=0

while score:
    print(art1)
    resultA=compare(compare_A)
    follower_of_A=compare_A["followers"]
    print(resultA)

    print(art2)

    Against_b= random.choice(data)
    score=True
    while Against_b==compare_A:
        Against_b = random.choice(data)
    resultB=against(Against_b)
    followers_of_B=Against_b["followers"]
    print(resultB)

    guess=input("who has more followers , Type 'A' or 'B': ").lower()
    print("\n"*100)
    os.system('cls' if os.name == 'nt' else 'clear')
    if follower_of_A>followers_of_B and guess=="a":
        current_score+=1
        print(f"You're right! ,The current score: {current_score}")
        compare_A=Against_b
    elif followers_of_B>follower_of_A and guess=="b":
        current_score+=1
        print(f"You're right! , The current score: {current_score}")
        compare_A = Against_b
    elif follower_of_A>followers_of_B and guess=="b":
        print("You Loose")
        score=False
    else:
        print("You loose")
        score=False
