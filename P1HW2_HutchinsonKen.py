# Kenneth Hutchinson
# 9 June 26
# P1HW2_hutchinsonKen
# Prompt user for travel expenses



print("This Program calculates and displays travel expenses")
print()

# This section defines the variables 

budget = int(input("Enter Trip Budget: " ))
destination = (input("Enter your travel destination: " ))
gas = int(input("How much do you think you will spend on gas? "))
hotel = int(input("Approximately how much will you need for accomodation/hotel? "))
food = int(input("Last, how much do you need for food? "))
# this is the math problem that makes this code work

balance = budget - gas - hotel - food

print("-----------Travel Expenses-------------------")

print("Location", destination)
print("Initial Budget: ", budget)
print("")
print("Fuel: ", gas)
print("Accomodation: ", hotel)
print("Food: " ,food)
print("")
print("Remaining Balance: ", balance)




