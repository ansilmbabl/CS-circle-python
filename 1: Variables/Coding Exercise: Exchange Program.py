"""
Coding Exercise: Exchange Program

Write a program to swap the values of two variables. The grader will automatically define variables x and y for you, with numerical values. 
You must write code that exchanges their values: the value of x after your code runs must equal the value that y had before your code ran, 
and the value of y after your code runs must equal the value that x had before your code ran. Your program does not need to print any output.
The most common solution is short, but can be hard to find. Click on each hint if you want to read it. 
"""

x = x+y
y = x-y
x = x-y

#or
x,y=y,x

#or
a=x
x=y
y=a
