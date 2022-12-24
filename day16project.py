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
money=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


   

def is_sufficeint(order):
    for item in resources:
        if resources[item]< order[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True

     
payment=0
def process_coin():
    global payment
    dimes=int(input("how many dimes?"))* 0.1
    payment+=dimes
    nickles=int(input("how many nickles?"))*0.05
    payment+=nickles
    pennies=int(input("how many pennies?"))*0.01
    payment+=pennies
    quarter=int(input("how many quater?"))* 0.25
    payment+=quarter
    payment=int(pennies+dimes+nickles+quarter)
    return payment

def transaction_successful(amount_inserted,cost_inserted):
    if amount_inserted<cost_inserted:
        print("Sorry that money is not enough.money refunded")
    elif amount_inserted>=cost_inserted:
        change=(amount_inserted-cost_inserted)
        print(f"Here is  ${change} change")
        global money
        money+=cost_inserted
        return True



def make_coffe(order,order_ingredients):
    for items in order_ingredients:
        resources[items]-=order_ingredients[items]
    print(f"Here your {order} Enjoy! ")   
            # return machine_resource[items]


action_on=True
while action_on:
    choice=input("What would you like?(espresso/latte/cappucino,): ")
    if choice=="off":
        action_on=False
    elif  choice=="report":
            print((f"water {(resources['water'])}ml"))
            print((f"milk {(resources['milk'])}kg"))
            print((f"coffee {(resources['coffee'])}ml"))
            print(f"money {money}$") 
    else:
        drink=MENU[choice]
        if  is_sufficeint(drink["ingredients"]):
            print("Please insert coins")
            payment=process_coin()
            if transaction_successful(payment,drink["cost"]):
                make_coffe(choice,drink["ingredients"])
                # print(f"Here your {choice} Enjoy! ") 