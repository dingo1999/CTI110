# Kenneth Hutchinson
# 23 June 26
# P3HW2_Salary_hutchinsonKen
# This program allows the user to enter a money (float) value with two places after the decimal.

#import math module to use the constant, math.pi, not 100% sure I need this. 
import math


# get user input

name = (input("Enter your name: "))
hours_worked = float(input("How many hours have you worked: "))
pay_rate = float(input("Enter your pay rate: $"))
print ("--------------------------------------------")

print(f"{'Employee Name:' :<20} {name :>15}")

print("Hours Worked      Pay Rate     Over Time   Overtime Pay    Reg hour Pay   Gross Pay")
print("-----------------------------------------------------------------------------------")

#caculations

overtime_rate = float(1.5)
over_time = float(hours_worked - 40)
regpay_rate = float(17.5)

# not sure on the ifelse statement 

# ⚙️ Initialize overtime variables
overtime_hours = 0.0
overtime_pay = 0.0
reghour_pay = 0.00
    
# 🧮 Evaluate overtime using an if-else statement

if hours_worked > 40:
        regular_hours = 40.0
        overtime_hours = hours_worked - 40.0

# Overtime is paid at 1.5 times the normal rate
        overtime_pay = overtime_hours * (regpay_rate * overtime_rate)
else:
        regular_hours = hours_worked
        overtime_hours = 0.0
        overtime_pay = 0.0

regular_hours = regular_hours * pay_rate

gross_pay = overtime_pay + regular_hours

#display required info 
print (f"{hours_worked :<10}  {pay_rate:>10} {over_time :>11} {overtime_pay :>12} {regular_hours :>15} {gross_pay: >15}")




      



