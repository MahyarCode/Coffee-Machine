sources = {"Coffee" : 100,
            "Water": 300,
            "Milk" : 200}

espresso = {"Coffee": 18,
                "Water":50}

latte = {"Coffee": 24,
                "Water":200,
                "Milk": 150}

cappuccino = {"Coffee": 24,
                "Water":250,
                "Milk": 100}

penny = 0.01
nickel = 0.05
dime = 0.10
quarter = 0.25

espresso_Price = 1.5
cappuccino_Price = 2.0
latte_Price = 2.5

while True:
    user = input("What would you like? (espresso/latte/cappuccino): ")

    choose = ["espresso" , "latte" , "cappuccino"]

    if user not in choose and user != "report" and user != "off":
        print("invalid input")

    if user == "off":
        break

    if user == "report":
        print(f"Coffee amount is: {sources['Coffee']}g\n"
              f"Water amount is: {sources['Water']}ml\n"
              f"Milk amount is: {sources['Milk']}ml\n")
    
    
    

    



    ## user input and calculation of resources
    if user in choose:
        if user == "espresso":
            if espresso["Coffee"] <= sources["Coffee"] and espresso["Water"] <= sources["Water"]:
                penny_num = int(input("how much Penny inserted ? "))
                nickel_num = int(input("how much Nickel inserted ? "))
                dime_num = int(input("how much Dime inserted ? "))
                quarter_num = int(input("how much Quarter inserted ? "))
                total_cashe = penny*penny_num + nickel*nickel_num + dime* dime_num + quarter*quarter_num

            
                if total_cashe < espresso_Price:
                    print("there's not enough money for espresso")

                if total_cashe > espresso_Price:        
                    sources["Coffee"] = sources["Coffee"] - espresso["Coffee"]
                    sources["Water"] = sources["Water"] - espresso["Water"]
                    print(f"here's your change: {total_cashe - espresso_Price}$\n"
                        f"Enjoy your Espresso <3")
                                
                if total_cashe == espresso_Price:            
                    sources["Coffee"] = sources["Coffee"] - espresso["Coffee"]
                    sources["Water"] = sources["Water"] - espresso["Water"]
                    print("Enjoy your Espresso <3")

            elif espresso["Coffee"] > sources["Coffee"]:
                print("sorry we run out of Coffee")
            elif espresso["Water"] > sources["Water"]:
                print("sorry we run out of water")
                            
                        
        if user == "cappuccino":
            if cappuccino["Coffee"] <= sources["Coffee"] and cappuccino["Water"] <= sources["Water"] and cappuccino["Milk"] <= sources["Milk"]:
                penny_num = int(input("how much Penny inserted ? "))
                nickel_num = int(input("how much Nickel inserted ? "))
                dime_num = int(input("how much Dime inserted ? "))
                quarter_num = int(input("how much Quarter inserted ? "))
                total_cashe = penny*penny_num + nickel*nickel_num + dime* dime_num + quarter*quarter_num


                if total_cashe < cappuccino_Price:
                    print("there's not enough money for cappuccino")

                if total_cashe > cappuccino_Price:                
                    sources["Coffee"] = sources["Coffee"] - cappuccino["Coffee"]
                    sources["Water"] = sources["Water"] - cappuccino["Water"]
                    sources["Milk"] = sources["Milk"] - cappuccino["Milk"]
                    print(f"here's your change: {round(total_cashe - cappuccino_Price,2)}$\n"
                        f"Enjoy your cappuccino <3")
                        
                if total_cashe == cappuccino_Price:
                        sources["Coffee"] = sources["Coffee"] - cappuccino["Coffee"]
                        sources["Water"] = sources["Water"] - cappuccino["Water"]
                        sources["Milk"] = sources["Milk"] - cappuccino["Milk"]
                        print("Enjoy your cappuccino <3")

            elif cappuccino["Coffee"] > sources["Coffee"]:
                print("sorry we run out of Coffee")
            elif cappuccino["Water"] > sources["Water"]:
                print("sorry we run out of water")


        if user == "latte":
            if latte["Coffee"] <= sources["Coffee"] and latte["Water"] <= sources["Water"] and latte["Milk"] <= sources["Milk"]:
                penny_num = int(input("how much Penny inserted ? "))
                nickel_num = int(input("how much Nickel inserted ? "))
                dime_num = int(input("how much Dime inserted ? "))
                quarter_num = int(input("how much Quarter inserted ? "))
                total_cashe = penny*penny_num + nickel*nickel_num + dime* dime_num + quarter*quarter_num


                if total_cashe < latte_Price:
                    print("there's not enough money for latte")

                if total_cashe > latte_Price:               
                    sources["Coffee"] = sources["Coffee"] - latte["Coffee"]
                    sources["Water"] = sources["Water"] - latte["Water"]
                    sources["Milk"] = sources["Milk"] - latte["Milk"]

                    print(f"here's your change: {round(total_cashe - latte_Price,2)}$\n"
                        f"Enjoy your latte <3")
                                        
                if total_cashe == latte_Price:               
                    sources["Coffee"] = sources["Coffee"] - latte["Coffee"]
                    sources["Water"] = sources["Water"] - latte["Water"]
                    sources["Milk"] = sources["Milk"] - latte["Milk"]
                    print("Enjoy your latte <3")            
            
            elif latte["Coffee"] > sources["Coffee"]:
                print("sorry we run out of Coffee")
            elif latte["Water"] > sources["Water"]:
                print("sorry we run out of water")

    if sources["Coffee"] < 18 or sources["Water"] < 50 :
        print("Coffee machine is out of order asliydgfkhiyldhugildhsiyg")
        break
        
        