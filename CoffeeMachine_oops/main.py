from menu import MENU, resources

money = 0


# TODO : print report

def print_report(resources, money):
    print(
        f"""    water : {resources["water"]}
    milk : {resources["milk"]}
    coffee : {resources["coffee"]}
    money : {money}""")
    start(resources, money)


# TODO : check resources

def check_resources(choose, money):
    """to check if there are enough resources"""
    for item in MENU[f"{choose}"]["ingredients"]:
        if MENU[f"{choose}"]["ingredients"][item] > resources[item]:
            print(f"sorry! there is not enough {item}")
            return start(resources, money)
    return True


    # if resources["water"] > MENU[f"{choose}"]["ingredients"]["water"] and \
    #         resources["coffee"] > MENU[f"{choose}"]["ingredients"]["coffee"] and \
    #         resources["milk"] > MENU[f"{choose}"]["ingredients"]["milk"]:
    #     return True
    # else:
    #     print("insufficient ingredients")
    #     start(resources, money)


def process_coffee(choose, money, amount):
    cost = MENU[f"{choose}"]["cost"]
    if amount >= cost and check_resources(choose, money):
        if amount > cost:
            print(f"Here is ${round((amount - cost), 2)} dollars in change.")
        print(f"here is your {choose} ☕! enjoy")
        for item in MENU[f"{choose}"]["ingredients"]:
            resources[item] -= MENU[f"{choose}"]["ingredients"][item]
        # resources["water"] -= MENU[f"{choose}"]["ingredients"]["water"]
        # resources["coffee"] -= MENU[f"{choose}"]["ingredients"]["coffee"]
        # resources["milk"] -= MENU[f"{choose}"]["ingredients"]["milk"]
        money += cost
        start(resources, money)
    if amount < cost:
        print("Sorry that is not enough money, money refunded")
        start(resources, money)

# TODO : process coins


def process_coins(choose, money):
    print("please insert coins")
    quarters = int(input("How many Quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    amount = float(quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01)
    process_coffee(choose, money, amount)


def start(resources, money):
    choose = input("What would you like? (espresso/latte/cappuccino): ")
    if choose == "report":
        print_report(resources, money)
    elif choose == "off":
        return
    else:
        process_coins(choose, money)


start(resources, money)
