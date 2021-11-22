
print ('Welcome to the Vacation Budget Planner App!')

name = input("Please enter your name: ")

destination = input(f"Hi {name}, where would you like to travel? ")

days = int(input(f"That sounds like fun. How many days will you be in {destination}? "))

money = float(input(f"Thanks for the info {name}. How much money will you bring on the trip? "))
moneyFormatted = format(money,".2f") #I've been trying to avoid doing this as a separate step but I get errors otherwise

moneyPerDay = format(money / days,".2f")

print(f"Hey {name}, you are going to {destination} for {days} days with ${moneyFormatted} for spending money. You can spend ${moneyPerDay} per day.")
