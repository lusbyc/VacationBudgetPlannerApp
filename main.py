import constant

def switch(userInput):
    if userInput == 1:
        global destination 
        global money
        global currencyName
        global currencyFormatted
        global currencyPerDay
        destination = "Mexico"
        currencyName = "pesos"
        currencyFormatted = "₱{:,.2f}".format(money * constant.MEXICAN_EXCHANGE_RATE)
        currencyPerDay = "₱{:,.2f}".format((money * constant.MEXICAN_EXCHANGE_RATE) / days)
        
    elif userInput == 2: 
        money 
        destination = "Jamaica"
        currencyName = "Jamaican Dollars"
        currencyFormatted = "J${:,.2f}".format(money * constant.JAMAICAN_EXCHANGE_RATE)
        JAMAICAN_EXCHANGE_RATE = 100 #This line attempts to change the constant value. When program is run line 76 shows that the value wasn't changed.
        currencyPerDay = "J${:,.2f}".format((money * constant.JAMAICAN_EXCHANGE_RATE) / days)

    else:   
        print()
        print("Invalid option. You must select one of the options provided.")
        quit() #This is acting as a break
        #convertUserInput() Ideally this method would be called again so that the user can try again

attempts = 0
password = "secret"

while attempts < 3:
    attempts += 1
    loginCredentials = input("Please enter your password: ")
    if loginCredentials == password:
        
        keepGoing = "y"

        while keepGoing.upper() == "Y":
            print()
            print ('Welcome to the Vacation Budget Planner!')

            name = input("What's your name? ")
    
            print()
            print(f"Welcome {name}, where would you like to go? ")
            userInput = int(input("""
Choose 
(1) Mexico
(2) Jamaica

"""))
            print()
            money = int(input("What's your budget for the trip? "))
            print()
            days = int(input("How many days do you plan to spend on this trip? "))
        
            switch(userInput)
            print()  
            print('Great,',destination,'sounds like an amazing trip!')
            print()
            print("**********")
            print()

            moneyFormatted = "${:,.2f}".format(money)
            moneyPerDay = "${:,.2f}".format(money / days)

            totalHours = days * constant.MINUTES_PER_HOUR
            totalHoursF = "{:,}".format(totalHours)
            totalMinutes = "{:,}".format(totalHours * constant.HOURS_PER_DAY)

            print(f"You're going to be in {destination} for {days} days. Put another way, you'll be there for {totalHoursF} hours or {totalMinutes} minutes.") 
            print()
            print(f"You have {moneyFormatted} in USD for spending money. You can spend {moneyPerDay} per day.")
            print()
            print(f"If you convert this to {currencyName} you'll have {currencyFormatted} to spend for the trip. This is {currencyPerDay} per day.")
            print()
            print(f"Enjoy your trip {name}!")
    
            keepGoing = input("""
Would you like to use the Vacation Budget Planner again? 
Enter 'Y' for Yes or 'N' for No: """).upper()
            print (keepGoing)
        print("""
Thanks for using the Vacation Budget Planner!""")   
        break
else:
    print("You've exceeded the maximum number of attempts.")
