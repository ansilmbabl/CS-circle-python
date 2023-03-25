"""
Coding Exercise: Watch the Pendulum

In physics, for a pendulum with length L and initial angle A, its horizontal displacement X(T) at time T is given by the formula
X(T) = L × cos(A × cos(T × √9.8/L)) - L × cos(A)
Write a program which takes two lines of input; the first line is L and the second line is A. The output should be ten lines, 
giving the values of X(0), X(1), X(2), ..., X(9). For example, if the first line of input is 53.1 and the second line of input is 0.8, 
then the first line of output is 0.0 and the second line of output is 53.1*cos(0.8*cos(1*√9.8/53.1)) - 53.1*cos(0.8) ~ 2.6689.
"""

from math import *
L = float(input())
A = float(input())
# delete this comment and enter your code here
for i in range(0,10):
   x = L * cos(A * cos(i * sqrt(9.8/L)))-(L * cos(A))
   print(x)
