from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu=Menu()
coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()

game_over=True
while game_over:
    choice=input(f"What would you like to have ({menu.get_items()}): ")

    if choice=="report":
        coffee_maker.report()
        money_machine.report()

    elif choice=="off":
        game_over=False

    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            money_machine.make_payment(drink.cost)
            coffee_maker.make_coffee(drink)




