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
#Pay system for coffee machine is to put 4 types of coin which values in above
#Example: 4 Quartes = $0.25 * 4 = $1
Profit = 0


def isReport(User_Order):
    global Profit
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

def Check_Resource_and_MoneyPaid(User_Order): 
    Cooking_items = Menu[User_Order]['Ingredients']
    enough_list = []
    global Profit

    for Components, quantity in Cooking_items.items():
        if Resources[Components] < quantity : 
            print(f"Sorry! There is not enough {Components} ro make {User_Order}")
            enough_list.append(1)
        else:
            enough_list.append(2)
                    
    # 1 means: it's not enough to make the order
    # 2 means: the resource is enough to make the order
    if 1 not in enough_list:
        Penny_cash   = int(input("How much Penny inserted? "))
        Nickel_cash  = int(input("How much Nickel inserted? "))
        Dime_cash    = int(input("How much Dime inserted? "))
        Quarter_cash = int(input("How much Quarter inserted? "))

        CheckMoney_and_UpdateResources(Penny_cash,Nickel_cash,Dime_cash,Quarter_cash)

        Order_Price = Menu[User_Order]['Price']
        Order_Cost = Menu[User_Order]['Cost']
        Profit += Order_Price - Order_Cost

# create a list for asking user to show all items to choose
Menu_List = []
for each_item in Menu:
    Menu_List.append(each_item)

Menu_List = ', '.join(Menu_List)

# The Coffee machine Operation 
while True:
    # user insert a write item in menu in title formet
    User_Order = input(f"What would you like ? {Menu_List}: ").title()
    
    # Check if manager wants to turn off the machine
    if User_Order == "Off":
        break

    # Check if manager wants take a report of resources   
    isReport(User_Order)

    # Check if user insert a write item in menu
    if isMenu(User_Order):

        #Check whether the resource is enough to make and calculate the money or not
        Check_Resource_and_MoneyPaid(User_Order) 

