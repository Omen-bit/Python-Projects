from resources import MENU

LATTE=2.50
ESPRESSO=1.5
CAPPUCCINO=3.00

machine_requirements={
    "water":300,
    "coffee":100,
    "milk":200,
    "money":0,
}

def coin_calculation(value,machine_requirements,choice):
    quarters=float(input("How many Quarters? : ")) * 0.25
    dime=float(input("How many Dimes? : ")) * 0.10
    nickel=float(input("How many Nickels? : ")) * 0.05
    penny=float(input("How many Pennies? : ")) * 0.01

    sum=quarters+dime+nickel+penny
    sum-=value

    if sum>=0:
        machine_requirements["money"]+=value
        print(f"Here is your ${round(sum,2)} in change")
        print(f"Enjoy your {choice} ☕")

    else:
        print("Insufficient Amount , Money refunded")

def deducting_resources(machine_requirements,MENU,choice):
    if choice=="latte" or choice=="cappuccino":
        machine_requirements["water"]-=MENU["water"]
        machine_requirements["coffee"] -= MENU["coffee"]
        machine_requirements["milk"] -= MENU["milk"]
    else:
        machine_requirements["water"] -= MENU["water"]
        machine_requirements["coffee"] -= MENU["coffee"]

def coffee_possible(machine_requirements,MENU):
    for keys in MENU:
        if MENU[keys ]>machine_requirements.get(keys,0):
            return keys
        else:
            return "continue"


game_over=True
while game_over:
    choice=input("What would you like (espresso/latte/cappuccino): ")
    if choice=="report":
        for keys in machine_requirements:
            print(f"{keys} : {machine_requirements[keys]}")

    elif choice=="latte":
        result=coffee_possible(machine_requirements, MENU["latte"]["ingredients"])
        if result=="continue":
            print(f"Please Insert ${LATTE} in coins: ")
            coin_calculation(LATTE,machine_requirements,choice)
            deducting_resources(machine_requirements,MENU["latte"]["ingredients"],choice)
        else:
            print(f"Not able to make {choice} due to insufficient {result}")

    elif choice=="espresso":
        result = coffee_possible(machine_requirements, MENU["espresso"]["ingredients"])
        if result=="continue":
            print(f"Please Insert ${ESPRESSO} in coins: ")
            coin_calculation(ESPRESSO,machine_requirements,choice)
            deducting_resources(machine_requirements, MENU["espresso"]["ingredients"],choice)
        else:
            print(f"Not able to make {choice} due to insufficient {result}")


    elif choice=="cappuccino":
        result = coffee_possible(machine_requirements, MENU["cappuccino"]["ingredients"])
        if result=="continue":
            print(f"Please Insert ${CAPPUCCINO} in coins: ")
            coin_calculation(CAPPUCCINO,machine_requirements,choice)
            deducting_resources(machine_requirements, MENU["cappuccino"]["ingredients"],choice)
        else:
            print(f"Not able to make {choice} due to insufficient {result}")

    else:
        game_over=False






