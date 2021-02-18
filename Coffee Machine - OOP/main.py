from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_maker = MoneyMachine()


is_off = False

while not is_off:
    options = menu.get_items()
    choice = input(f"What would you like {(options)}: ")
    if choice == "off":
        is_off = True
    elif choice == "report":
        coffee_maker.report()
        money_maker.report()
    else:
        drink = menu.find_drink(choice)
        is_enough = coffee_maker.is_resource_sufficient(drink)
        if is_enough:
            payment_okay = money_maker.make_payment(drink.cost)
            if payment_okay:
                coffee_maker.make_coffee(drink)
        else:
            print("Call Service to refill to machine...")
            is_off = True
