from pconst import const

def switch(userInput):
    if userInput == "1":
        global destination 
        global money
        global currency_name
        global currency_formatted
        global currency_per_day
        const.MEXICAN_EXCHANGE_RATE = 154.60
        destination = "Mexico"
        currency_name = "pesos"
        currency_formatted = "₱{:,.2f}".format(money * const.MEXICAN_EXCHANGE_RATE)
        currency_per_day = "₱{:,.2f}".format((money * const.MEXICAN_EXCHANGE_RATE) / days)
        
    elif userInput == "2": 
        money 
        destination = "Jamaica"
        currency_name = "Jamaican Dollars"
        const.JAMAICAN_EXCHANGE_RATE = 21.92
        currency_formatted = "J${:,.2f}".format(money * const.JAMAICAN_EXCHANGE_RATE)
        currency_per_day = "J${:,.2f}".format((money * const.JAMAICAN_EXCHANGE_RATE) / days)

    # else:   
    #     print()
    #     print("Invalid option. You must select one of the options provided.")
    #     quit() #This ends the program. Alternately a loop can be utilized to give the user another chance to enter a valid option.

const.MINUTES_PER_HOUR = 60
const.HOURS_PER_DAY = 24

attempts = 0
password = "secret"

while attempts < 3:
    attempts += 1
    login_credentials = input("Please enter your password: ")
    if login_credentials == password:
        
        keep_going = "y"

        while keep_going.upper() == "Y":
            print()
            print ('Welcome to the Vacation Budget Planner!')

            name = input("What's your name? ")
    
            print()
            print(f"Welcome {name}, where would you like to go? ")
            user_input = input("""
Choose 
(1) Mexico
(2) Jamaica

""")
            if user_input != "1" and user_input != "2":
                print()
                print("Invalid option. You must select one of the options provided.")
                quit() #This ends the program. Alternately a loop can be utilized to give the user another chance to enter a valid option.
            
            else:
                print()
                money = int(input("What's your budget for the trip in US dollars? "))
                print()
                days = int(input("How many days do you plan to spend on this trip? "))

                switch(user_input)

            print()  
            print(f"Great, {destination} sounds like an amazing trip!")
            print()
            print("**********")

            money_formatted = "${:,.2f}".format(money)
            money_per_day = "${:,.2f}".format(money / days)

            total_hours = days * const.HOURS_PER_DAY
            total_hours_formatted = "{:,}".format(total_hours)
            total_minutes = "{:,}".format(total_hours * const.MINUTES_PER_HOUR)

            print(f"""
You're going to be in {destination} for {days} days. Put another way, you'll be there for {total_hours_formatted} hours or {total_minutes} minutes.
You have {money_formatted} in US dollars for spending money. You can spend {money_per_day} per day. If you convert this to {currency_name} 
you'll have {currency_formatted} to spend for the trip. This is {currency_per_day} per day.
            
Enjoy your trip {name}!""")
    
            keep_going = input("""
Would you like to use the Vacation Budget Planner again? 
Enter 'Y' for Yes or 'N' for No: """).upper()
        print("""
Thanks for using the Vacation Budget Planner!""")   
        break
else:
    print("You've exceeded the maximum number of attempts.")
