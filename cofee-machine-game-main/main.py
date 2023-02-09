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
    "water": 400,
    "milk": 200,
    "coffee": 100,
}


# TODO Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5


def report(action):
    """Print the report of current resources status."""
    if action == 'report':
        print(f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${resources["money"]}')


# TODO Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected. E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the program should say “Sorry that's not enough money. Money refunded.”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the machine as the profit and this will be reflected the next time “report” is triggered. E.g. Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal places.


def check_transaction(action, total_monetary_value):
    """Return True if money has been inserted are sufficient, otherwise return False."""
    if total_monetary_value < MENU[action]["cost"]:
        print('Sorry, that\'s not enough money. Money refunded')
        return False
    elif total_monetary_value == MENU[action]["cost"]:
        resources["money"] += MENU[action]["cost"]
        return True
    elif total_monetary_value > MENU[action]["cost"]:
        resources["money"] += MENU[action]["cost"]
        change = round((total_monetary_value - MENU[action]["cost"]), 2)
        print(f'Here is ${change} in change')
        return True


# TODO Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52


def process_coins():
    """Calculate total amount of coins have been inserted and return same value."""
    print('Please insert coins')
    total_monetary_value = float(0.25 * int(input('How many quarters?: ')))
    total_monetary_value += float(0.10 * int(input("How many dimes?: ")))
    total_monetary_value += float(0.05 * int(input("How many nickles?: ")))
    total_monetary_value += float(0.01 * int(input("How many pennies?: ")))
    return total_monetary_value


# TODO Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.


def check_resources(action):
    """Check the availability of required ingredients for specific coffee, if not available return False."""
    depleted_resource = []
    for each_ingredient in MENU[action]["ingredients"]:
        if MENU[action]["ingredients"][each_ingredient] > resources[each_ingredient]:
            depleted_resource.append(each_ingredient)
    if depleted_resource:
        print(f'Sorry, there is not enough {", ".join(depleted_resource)}')
        return False
    return True


# TODO Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the user selected, then the ingredients to make the drink should be deducted from the coffee machine resources.
# E.g. report before purchasing latte: Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If latte was their choice of drink.


def make_cofee(action):
    """Deduct specific amount of required ingredients for particular sort of coffee from machine resources and """
    for each_ingredient in MENU[action]["ingredients"]:
        if each_ingredient in resources:
            resources[each_ingredient] = resources[each_ingredient] - MENU[action]["ingredients"][each_ingredient]
    print(f'Here is your {action}. ☕️Enjoy!')


# TODO Main part. Prompt user by asking What would you like? (espresso/latte/cappuccino):
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
#    dispensed. The prompt should show again to serve the next customer


TURN_OFF = False
resources["money"] = 0
while not TURN_OFF:
    action = input('What would you like? (espresso/latte/cappuccino): ')
    if action == 'off':
        TURN_OFF = True
    elif action == 'report':
        report(action)
    elif check_resources(action):
        if check_transaction(action, process_coins()):
            make_cofee(action)
