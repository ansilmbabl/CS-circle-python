"""
Coding Exercise: Gravity

A parcel is thrown downward at a speed of v m/s from an airplane at altitude 11000 m. 
As it falls, its distance from the ground is given by the formula -4.9t2 - vt + 11000, where t is the time in seconds since it was dropped. 
Write a program to output the time it will take to reach the ground. The input to your program is the positive floating-point number v.
The required time is given by the quadratic formula

"""
import math
v=float(input())

t = (v-math.sqrt((v**2)-4*(-4.9)*11000))/(2*(-4.9))
print(t)
