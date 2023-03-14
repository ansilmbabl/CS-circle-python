"""
Coding Exercise: Pizza Circles

Your friends have eaten their square pizzas and are now ordering a round pizza. Write a program to calculate the area of this circular pizza. 
The input is a float r, which represents the radius in cm. The output should be the area in cm2, calculated using the formula  A=pi*r2. 
Use Python's pi feature instead of typing 3.1415...
"""

# delete this comment and enter your code here
import math

r=float(input())
A=math.pi*(r**2)
print(A)
