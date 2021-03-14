# print("Starting to make a coffee\nGrinding coffee beans\nBoiling water\nMixing boiled water with crushed coffee beans\nPouring coffee into the cup\nPouring some milk into the cup\nCoffee is ready!")


# print("Write how many cups of coffee you will need:")
# cups = int(input())
# print("For ", cups, " cups of coffee you will need:")
# print((200 * cups), " ml of water")
# print((50 * cups), " ml of milk")
# print((15 * cups), " g of coffee beans")


class CoffeeMachine:
    water = 400
    milk = 540
    beans = 120
    cups = 9
    money = 550


def remaining(coffeeMachine):
    print("The coffee machine has:")
    print(coffeeMachine.water, " of water")
    print(coffeeMachine.milk, " of milk")
    print(coffeeMachine.beans, " of coffee beans")
    print(coffeeMachine.cups, " of disposable cups")
    print(coffeeMachine.money, " of money")


def buy(coffeeMachine):
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    typeOfCoffee = input().replace(" ", "")
    if typeOfCoffee == "1":
        if (coffeeMachine.water  < 250):
            print("Sorry, not enough water!")
        else:
            coffeeMachine.water -= 250
            coffeeMachine.beans -= 16
            coffeeMachine.money += 4
            coffeeMachine.cups -= 1
            print("I have enough resources, making you a coffee!")
    elif typeOfCoffee == "2":
        if (coffeeMachine.water  < 350):
            print("Sorry, not enough water!")
        else :
            coffeeMachine.water -= 350
            coffeeMachine.milk -= 75
            coffeeMachine.beans -= 20
            coffeeMachine.money += 7
            coffeeMachine.cups -= 1
            print("I have enough resources, making you a coffee!")
    elif typeOfCoffee == "3":
        if (coffeeMachine.water < 200):
            print("Sorry, not enough water!")
        else :
            coffeeMachine.water -= 200
            coffeeMachine.milk -= 100
            coffeeMachine.beans -= 12
            coffeeMachine.money += 6
            coffeeMachine.cups -= 1
            print("I have enough resources, making you a coffee!")




def take(coffeeMachine):
    print("I gave you $", coffeeMachine.money)
    coffeeMachine.money = 0

def fill(coffeeMachine):
    print("Write how many ml of water do you want to add:")
    coffeeMachine.water += int(input())
    print("Write how many ml of milk do you want to add:")
    coffeeMachine.milk += int(input())
    print("Write how many grams of coffee beans do you want to add:")
    coffeeMachine.beans += int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    coffeeMachine.cups += int(input())

coffeeMachine = CoffeeMachine()



while True:
    print("Write action (buy, fill, take, remaining, exit):")
    command = input().replace(" ", "")
    print("")
    if command == "buy":
        buy(coffeeMachine)
    elif command == "fill":
        fill(coffeeMachine)
    elif command == "take":
        take(coffeeMachine)
    elif command == "remaining":
        remaining(coffeeMachine)
    else:
        break

