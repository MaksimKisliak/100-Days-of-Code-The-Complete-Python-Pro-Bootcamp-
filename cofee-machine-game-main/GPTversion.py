# This code implements the remaining methods of the CoffeeMachine class: fill, take, and remaining. 
# The fill method prompts the user to enter the amounts of water, milk, coffee beans, and disposable cups to add to the machine. 
# The take method gives the user all of the money in the machine. The remaining method prints the current state of the machine. 
# Finally, the main_loop function implements the main loop of the program. 
# It creates a CoffeeMachine object, and then repeatedly prompts the user for an action until they choose to exit.

class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee = 120
        self.cups = 9
        self.money = 550

    def remaining(self):
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffee} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")

    def make_coffee(self, coffee_type):
        if coffee_type == "espresso":
            if self.water < 250:
                print("Sorry, not enough water!")
                return
            if self.coffee < 16:
                print("Sorry, not enough coffee beans!")
                return
            if self.cups < 1:
                print("Sorry, not enough cups!")
                return
            print("I have enough resources, making you a coffee!")
            self.water -= 250
            self.coffee -= 16
            self.cups -= 1
            self.money += 4
        elif coffee_type == "latte":
            if self.water < 350:
                print("Sorry, not enough water!")
                return
            if self.milk < 75:
                print("Sorry, not enough milk!")
                return
            if self.coffee < 20:
                print("Sorry, not enough coffee beans!")
                return
            if self.cups < 1:
                print("Sorry, not enough cups!")
                return
            print("I have enough resources, making you a coffee!")
            self.water -= 350
            self.milk -= 75
            self.coffee -= 20
            self.cups -= 1
            self.money += 7
        elif coffee_type == "cappuccino":
            if self.water < 200:
                print("Sorry, not enough water!")
                return
            if self.milk < 100:
                print("Sorry, not enough milk!")
                return
            if self.coffee < 12:
                print("Sorry, not enough coffee beans!")
                return
            if self.cups < 1:
                print("Sorry, not enough cups!")
                return
            print("I have enough resources, making you a coffee!")
            self.water -= 200
            self.milk -= 100
            self.coffee -= 12
            self.cups -= 1
            self.money += 6

    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        coffee_type = input()
        if coffee_type == "back":
            return
        self.make_coffee(["espresso", "latte", "cappuccino"][int(coffee_type) - 1])

    def fill(self):
        print("Write how many ml of water do you want to add:")
        self.water += int(input())
        print("Write how many ml of milk do you want to add:")
        self.milk += int(input())
        print("Write how many grams of coffee beans do you want to add:")
        self.coffee += int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        self.cups += int(input())

def main_loop():
    coffee_machine = CoffeeMachine()
    while True:
        print("Write action (buy, fill, take, remaining, exit):")
        action = input()
        if action == "exit":
            break
        elif action == "buy":
            coffee_machine.buy()
        elif action == "fill":
            coffee_machine.fill()
        elif action == "take":
            print(f"I gave you ${coffee_machine.money}")
            coffee_machine.money = 0
        elif action == "remaining":
            coffee_machine.remaining()

main_loop()


