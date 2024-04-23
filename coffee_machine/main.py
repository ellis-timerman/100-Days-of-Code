MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
        "cost": 3,
    }
}

RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def print_report(water, milk, coffee, money):
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")


def take_order():
    machine_status = True
    order = "Waiting for order!"
    take_order = input("What would you like? (espresso/latte/cappuccino):")
    if take_order == "espresso":
        order = "espresso"
    elif take_order == "latte":
        order = "latte"
    elif take_order == "cappuccino":
        order = "cappuccino"
    elif take_order == "report":
        print_report(RESOURCES["water"], RESOURCES["milk"], RESOURCES["coffee"], RESOURCES["money"])
    elif take_order == "off":
        machine_status = False
    else:
        print("Invalid order!")

    return machine_status, order


def check_resources(order, water, milk, coffee):
    low_resources = []
    need_supplies = False
    if water < MENU[order]["ingredients"]["water"]:
        low_resources.append("water")
    if milk < MENU[order]["ingredients"]["milk"]:
        low_resources.append("milk")
    if coffee < MENU[order]["ingredients"]["coffee"]:
        low_resources.append("coffee")
    if len(low_resources) > 0:
        need_supplies = True
    return need_supplies, low_resources


def process_coins():
    print("Please insert coins.")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickels = float(input("How many nickels?: "))
    pennies = float(input("How many pennies?: "))

    amt_paid = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
    return amt_paid


def validate_transaction(amt_paid, cost):
    if amt_paid >= cost:
        valid_payment = True
    else:
        valid_payment = False
    return valid_payment


def make_coffee(order):
    RESOURCES["water"] = RESOURCES["water"] - MENU[order]["ingredients"]["water"]
    RESOURCES["coffee"] = RESOURCES["coffee"] - MENU[order]["ingredients"]["coffee"]
    if "milk" in MENU[order]["ingredients"]:
        RESOURCES["milk"] = RESOURCES["milk"] - MENU[order]["ingredients"]["milk"]


while True:
    machine_status, order = take_order()
    if not machine_status:
        break
    elif order not in ("espresso", "latte", "cappuccino"):
        print(order)
    else:
        need_supplies, low_resources = check_resources(
            order, RESOURCES["water"],
            RESOURCES["milk"],
            RESOURCES["coffee"])
        if need_supplies:
            for resource in low_resources:
                print(f"Sorry there is not enough {resource}.")
        else:
            payment = process_coins()
            valid_payment = validate_transaction(payment, MENU[order]["cost"])
            if not valid_payment:
                print("Sorry that's not enough money. Money refunded.")
            else:
                RESOURCES["money"] = RESOURCES["money"] + MENU[order]["cost"]
                if payment > MENU[order]["cost"]:
                    return_change = round(float(payment - MENU[order]["cost"]), 2)
                    print(f"Here is ${return_change} in change.")
                make_coffee(order)
                print(f"Here is your {order}. Enjoy!")
