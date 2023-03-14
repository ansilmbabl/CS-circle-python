"""
Coding Exercise: Geometric Mean

The geometric mean of two numbers a and b is the number
\sqrt{ab}

(It is used to compare aspect ratios of display screens and describe the average growth rate of a population.) 
Write a program that reads two lines of positive float from input, and outputs their geometric mean.
Example: If the input is
5.0
20.0
then the output should be 10.0.
"""

# delete this comment and enter your code here
import math

a=float(input())
b=float(input())

print(math.sqrt(a*b))
