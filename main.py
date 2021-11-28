def convertUserOption():
    userInput = int(input("""
Where would you like to travel? 

Choose 
(1) Mexico
(2) Jamaica

"""))
    if userInput == 1:
        global destination 
        global currencyName
        global currencyFormatted
        global currencyPerDay
        destination = "Mexico"
        currencyName = "pesos"
        currencyFormatted = "₱{:,.2f}".format(money * 21.92)
        currencyPerDay = "₱{:,.2f}".format((money * 21.92) / days)

    elif userInput == 2: 
        destination = "Jamaica"
        currencyName = "Jamaican Dollars"
        currencyFormatted = "J${:,.2f}".format(money * 154.60)
        currencyPerDay = "J${:,.2f}".format((money * 154.60) / days)

    else:   
        print()
        print("Invalid option. You must select one of the options provided.")
        convertUserOption()

keepGoing = "y"

while keepGoing.upper() == "Y":
    print()
    print ('Welcome to the Vacation Budget Planner!')

    name = input("What's your name? ")

    money = int(input(f"Hi {name}, what's your budget for the trip? "))

    days = int(input(f"How many days do you plan to vacation? "))
        
    convertUserOption()
    print()  
    print('Great,',destination,'sounds like an amazing trip!')
    print("**********")

    moneyFormatted = "${:,.2f}".format(money)
    moneyPerDay = "${:,.2f}".format(money / days)

    totalHours = days * 24
    totalHoursF = "{:,}".format(totalHours)
    totalMinutes = "{:,}".format(totalHours * 60)

    print(f"You're going to be in {destination} for {days} days. Put another way, you'll be there for {totalHoursF} hours or {totalMinutes} minutes.") 

    print(f"You have {moneyFormatted} in USD for spending money. You can spend {moneyPerDay} per day.")
    print(f"If you convert this to {currencyName} you'll have {currencyFormatted} to spend for the trip. This is {currencyPerDay} per day.")
    print()
    print(f"Enjoy your trip {name}!")
    
    keepGoing = input("""
Would you like to use the Vacation Budget Planner again? 
Enter 'Y' for Yes or 'N' for No: """).upper()
    
print("""
Thanks for using the Vacation Budget Planner!""")
