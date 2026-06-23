# Kenneth Hutchinson
# 23 June 26
# P3LAB_hutchinsonKen
# This program allows the user to enter a money (float) value with two places after the decimal.

#import math module to use the constant, math.pi, not 100% sure I need this. 
import math


# get user input
change = float(input("Enter an amount of money: $"))
print(f"Change Amount: {change}")

#make the number a whole number
change = round(change * 100)
# number of dollars
num_dollars = change // 100
change = change - (num_dollars * 100)
# number of quarters
num_quarters = change // 25
change = change - (num_quarters * 25)
#number of dimes
num_dimes = change // 10
change = change - (num_dimes * 10)
#of nickels
num_nickels = change // 5
change = change - (num_nickels * 5)
# of pennies
num_pennies = change



# display the number of dollars
if num_dollars > 0:
    if num_dollars == 1:
        print (f"{num_dollars} Dollar")
    else:
        print(f"{num_dollars} Dollars")

# display the number of quarters

if num_quarters > 0:
    if num_quarters == 1:
        print(f"{num_quarters} quarter")
    else:
        print(f"{num_quarters} quarters")

#display the number of dimes

if num_dimes > 0:
    if num_dimes == 1:
        print(f"{num_dimes} dime")
    else:
        print(f"{num_dimes} dimes")

#display the numbers of nickels

if num_nickels > 0:
    if num_nickels == 1:
        print(f"{num_nickels} nickel")
    else:
        print(f"{num_nickels} nickels")

#display the number of pennies

if num_pennies > 0:
    if num_pennies == 1:
        print(f"{num_pennies} penny")
    else:
        print(f"{num_pennies} pennies")





