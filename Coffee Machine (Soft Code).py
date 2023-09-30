Resources = {"Coffee" : 100,
            "Water": 500,
            "Milk" : 300,
            "Sugar": 800,
            "Tea": 200}

Menu = {
    "Espresso":{
        "Ingredients":{
            "Coffee": 18,
            "Water":50
        },
        "Cost":1,
        "Price":1.5
    },

    "Cappuccino":{
        "Ingredients":{
            "Coffee": 24,
            "Water":250,
            "Milk": 100
        },
        "Cost":1.5,
        "Price":2
    },

    "Latte":{
        "Ingredients":{
            "Coffee": 24,
            "Water":200,
            "Milk": 150
        },
        "Cost":1.75,
        "Price":2.5
    },

    "Tea":{
        "Ingredients":{
            "Tea": 10,
            "Water":250,
            "Sugar": 150
        },
        "Cost":1.2,
        "Price":2.25
    }
}

Penny = 0.01
Nickel = 0.05
Dime = 0.10
Quarter = 0.25
Profit = 0

def isReport(User_Order):
    if User_Order == "Report": 
        for Ingredient in Resources:
            print(f"{Ingredient}: {Resources[Ingredient]}")
            
        print(f"The total profit of todays machine is: {Profit}$ ")
        return True 
    
    else:
        return True

def isMenu(User_Order):
    if User_Order in Menu:
        return True
    
    elif User_Order == "Off" or User_Order == "Report":
        pass

    else:
        print("Invalid input! Please try again")
            
def Check_Resources(User_Order):
    Cooking_items = Menu[User_Order]['Ingredients']

    for Components, quantity in Cooking_items.items():
        if Resources[Components] < quantity : 
            print(f"Sorry! There is not enough {Components} ro make {User_Order}")
            # return False       

def Update_Resources(User_Order):
    Cooking_items = Menu[User_Order]['Ingredients']

    for Components, quantity in Cooking_items.items():
        if Resources[Components] >= quantity : 
            Resources[Components] -= quantity
            

def CheckMoney_and_UpdateResources(Penny_cash, Nickel_cash, Dime_cash, Quarter_cash):    
    if isMenu(User_Order):
        Total_cashe = Penny_cash*0.01 + Nickel_cash*0.05 + Dime_cash*0.10 + Quarter_cash*0.25

        if Total_cashe >= Menu[User_Order]['Price']:
            print(f"Here is your change: {Total_cashe - Menu[User_Order]['Price']}$ ")
            print(f"Enjoy your {User_Order}")
            Update_Resources(User_Order)
                    
        elif Total_cashe == Menu[User_Order]['Price']:
            print(f"Enjoy your{User_Order}")
            Update_Resources(User_Order)
                  
        else:
            print(f"There not enough money for {User_Order}")


Menu_List = []
for each_item in Menu:
    Menu_List.append(each_item)

Menu_List = ', '.join(Menu_List)

# The Coffee machine Operation
while True:
    # user insert a write item in menu
    User_Order = input(f"What would you like ? {Menu_List}: ").title()
    
    # Check if manager wants to turn off the machine
    if User_Order == "Off":
        break

    # Check if manager wants take a report of resources   
    isReport(User_Order)

    # Check if user insert a write item in menu
    if isMenu(User_Order):
        
### ❌❌❌❌Problem Here 👇👇👇👇👇
        Check_Resources(User_Order) 
### ❌❌❌❌Problem Here 👆👆👆👆👆 

########## Problem: Customer must choose an item in coffee machine
##########          and at first, machine has to check the resources if it is enough make the order or not
##########          after that if the resource is enough to make the order, ask for cash from the user + Update the resources 
##########   👇👇   which is down below
##########          but ❌ i can't use this condition ❌ if the resource is not enough to make
##########          then ask user for another choose: (back again to the loop and ask user again)
##########          not to break the whole loop !!!!
##########          when the source is not enough and user enter the whole price for his order, the resource will update 
##########          and this will cause problem for report !!!!

        # Check how much money inserted in machine
        Penny_cash   = int(input("How much Penny inserted? "))
        Nickel_cash  = int(input("How much Nickel inserted? "))
        Dime_cash    = int(input("How much Dime inserted? "))
        Quarter_cash = int(input("How much Quarter inserted? "))

        Order_Price = Menu[User_Order]['Price']
        Order_Cost = Menu[User_Order]['Cost']
        Profit += Order_Price - Order_Cost
            
        # if user inserted enough money in machine and then the machine makes the order and update the resources
        CheckMoney_and_UpdateResources(Penny_cash, Nickel_cash, Dime_cash, Quarter_cash)
        # i made some changes in github    
        # hanoz nashode


