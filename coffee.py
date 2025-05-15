# MENU--

menu = {
   "latte":{
       "ingredients":{
           "water": 200,
           "milk": 150,
           "coffee": 18
       },
       "cost": 99
   },
   "espresso":{
       "ingredients":{
           "water": 50,
           "coffee": 35
       },
       "cost": 199
   },
   "cappuccino":{
       "ingredients":{
           "water": 250,
           "milk": 100,
           "coffee": 24
       },
       "cost": 299
   },
   "bubble tea":{
       "ingredients":{
           "water": 50,
           "milk": 200,
           "coffee": 25
       },
       "cost": 139
   }
}
# INGREDIENTS PRESENT IN MACHINE FOR COFFEE MAKING--

resources = {
    "water": 500,
    "coffee": 100,
    "milk": 350, 
    }

# INGREDIENTS NEEDED FOR COFFE MAKING IS SUFFICIENT--

def  is_resource_sufficent(ingredients):
    ''' Return true when order can be made, or false when ingredients not sufficent '''
    
    for item in ingredients:
        if ingredients[item] > resources.get(item, 0):
            print(f"Sorry there is not enough {item}.")
            return False
    return True  

# MONEY GIVEN BY CUSTOMER--
      
def process_payment():
    ''' Return total money entered by customer '''
    
    print("Enter the money\n")
    
    total = int(input("How much cash:"))
    return total

# RETURN CHANGE AND CHECK IF MONEY IS SUFFICIENT--

def is_sufficent_money(money_received, drink_cost):
    
    if money_received >= drink_cost:
        
        global profit 
        profit += drink_cost
        
        change = round(money_received - drink_cost, 2)
        print(f"Your change: ₹{change}")
        return True
    
    else:
        print("Sorry that's not enough money. Money refunded\n.")
        return False
    
def make_coffee(drink_name, ingredients):
    
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name}🧋\n.")

 # LET'S START THE MAKING COFFEE--
    
is_on = True
profit = 0

print("...IT'S YOUR COFFEE WENDING MACHINE🧋...\n")

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino/bubble tea):") # ASK USER FOR INPUT--
    
    # STOP WORKING--
    if choice == "off":
        is_on = False
      
    # REPORT THE NGREDIENTS AMOUNT PRESENT IN MACHINE--
       
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Cash: ₹{profit}")
    
    # ORDER COFFEE--
        
    elif choice in menu:
        
        drink = menu[choice]
        
        if is_resource_sufficent(drink["ingredients"]):
           while True:
                payment = process_payment()
                if is_sufficent_money(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])
                    break
                else:
                    print("Please enter the big amount.\n")
                    
    # REFILLING THE STOCK--
                    
    elif choice == "refill":
        resources['water'] += 500
        resources['milk'] += 300 
        resources['coffee'] += 75
        print("Stock is refilled\n")
    
    # WRONG INPUT TRACKING--
        
    else:
        print("Invalid choice. Please select a valid drink.\n")     
           