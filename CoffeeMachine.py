menu = {
"espresso" :{"ingredients" : {"water" : 50 , "milk" : 0 , "coffee" : 18 }, "cost" : 1.5},
"lattee" : {"ingredients" :{"water" : 200 , "milk" : 150 , "coffee" : 24}, "cost" : 2.5 },
"cappuccino" : {"ingredients" : {"water" : 250 , "milk" : 100 , "coffee" : 24} , "cost" : 3 }
}
profit = 0
resources = {"water" : 600 , "milk" : 700 , "coffee" : 100 , "profit" : profit}


def check(price):
    global profit , exchange , type
    exchange = 0
    quaretr = int(input("Enter your quarter coin num:"))
    dimes = int(input("Enter your dimes coin num:"))
    nickles = int(input("Enter your nickles coin num:"))
    pennies = int(input("Enter your pennies coin num:"))
    amount =  0.25 * quaretr + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    
    if amount ==  price or amount > price:
        if resources["water"] >= menu[type]["ingredients"]["water"] and resources["milk"] >= menu[type]["ingredients"]["milk"] and resources["coffee"] >= menu[type]["ingredients"]["coffee"]:
            resources["water"] -= menu[type]["ingredients"]["water"]
            resources["milk"] -= menu[type]["ingredients"]["milk"]
            resources["coffee"] -= menu[type]["ingredients"]["coffee"]
            profit += price
            exchange = amount - price
            print(f"enjoy your {type} , you have {exchange} exchange ")
        else:
            print("sorry we run out of sources")

    elif amount < price:
        print("sorry , not enough money")
                

def drink():
    global type
    type = input("What would you like? (espresso/latte/cappuccino):").lower()
    if type == "report":
        print(f"water : {resources["water"]} ml\nmilk : {resources["milk"]} ml\ncoffee : {resources["coffee"]}g\nmoney : {profit} $")
    elif type == "espresso":
        price = 1.5
        check(price)
    elif type == "lattee":
        price = 2.5
        check(price)
    elif type == "cappuccino":
        price = 3
        check(price)
        
drink()

while input("type ON to start the machine") == "on":
    drink()
