# Kenneth Hutchinson
# 16 June 26
# P2HW1_hutchinsonKen
# Update from last week



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

print (f"{'Location:':<20}  {destination:>15}")


print(f"{'Initial Budget:':<20} {f'${budget:.2f}':>15}")
print("")
print(f"{'Fuel:':<20} {f'${gas:.2f}':>15}")
print(f"{'Accommodation:':<20} {f'${hotel:.2f}':>15}")
print(f"{'Food:':<20} {f'${food:.2f}':>15}")
print("")

print("-----------Travel Expenses-------------------")
print("")
print(f"{'Remaining Balance:':<20} {f'${balance:.2f}':>15}")




