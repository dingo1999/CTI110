# Kenneth Hutchinson
# 16 June 26
# P2HW2_hutchinsonKen
# User grade caculation 



# This section defines varibles and gets the input from the student
import math
module_one = float(input("Enter Grade for module 1: " ))
module_two = float(input("Enter Grade for module 2: " ))
module_three = float(input("Enter Grade for module 3: " ))
module_four = float(input("Enter Grade for module 4: " ))
module_five = float(input("Enter Grade for module 5: " ))
module_six = float(input("Enter Grade for module 6: " ))

grades = [module_one, module_two, module_three,module_four, module_six]

lowest_grade = min(grades)
highest_grade = max(grades)
total_sum = sum(grades)
average = sum(grades) / len(grades)


print("\n-----------Results-------------------")

print(f"{'Lowest Grade:':<20}{lowest_grade:>15.2f}")
print(f"{'Highest Grade:':<20}{highest_grade:>15.2f}")
print(f"{'Sum of Grades:':<20}{total_sum:>15.2f}")
print(f"{'Average:':<20}{average:>15.2f}")
print("\n-------------------------------------")



