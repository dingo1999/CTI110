# Kenneth Hutchinson
# 15 June 26
# P2LAB1_hutchinsonKen
# program will calculate the diameter, circumference, and area of a circle. 

#import math module to use the constant, math.pi
import math

#get the redius from the user
radius = float (input("What is the radius of the circle? "))
print ()

#calculate the diameter 
diameter = 2 * radius

#Display diameter with 1 decimal; point 
print(f"The diametr of the circle is {diameter:.1f}\n")

#calculate circumrefence
circumference = 2 * math.pi * radius

#Display circumference with 2 decimal place
print(f"The circumference of the circle is {circumference:.2f}\n")

# calcuylate the area
area = math.pi *radius**2

print (f"The area of the circle is {area:.3}")



