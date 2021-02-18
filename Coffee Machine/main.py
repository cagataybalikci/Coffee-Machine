MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


machine_money = 0
is_off = False

QUARTER = 0.25
DIME = 0.1
NICKLE = 0.05
PENNY = 0.01

def get_coin():
    print("Please insert coins.")
    numb_of_quarters = int(input("How Many Quarters? "))
    numb_of_dimes = int(input("How Many Dimes? "))
    numb_of_nickles = int(input("How Many Nickles? "))
    numb_of_pennies = int(input("How Many Pennies? "))
    input_total = (numb_of_quarters * QUARTER) + (numb_of_dimes * DIME) + (numb_of_nickles * NICKLE) + (numb_of_pennies * PENNY)
    return input_total

def money_operations(user_coin,drink,machine_money):
    cost = MENU[drink]["cost"]
    if user_coin >= cost:
        refund = user_coin - cost
        formatted_refund = "{:.2f}".format(refund)
        machine_money += cost
        print(f"Here is ${formatted_refund} in change.")
        print(f"Here is your {drink} Enjoy!")
        return  machine_money
    else:
        print("Sorry that is not enough money. Money refunded.")

while not is_off:
    drink = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if drink in MENU:
        user_coins = get_coin()
        machine_money = money_operations(user_coins,drink,machine_money)
    elif drink == "report":
        print(f'Water: {resources["water"]}')
        print(f'Milk: {resources["milk"]}')
        print(f'Coffee: {resources["coffee"]}')
        print(f'Money: {machine_money}')
    elif drink == "off":
        is_off = True
    else:
        print("Not in the list Pick again.")