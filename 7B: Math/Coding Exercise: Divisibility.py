"""
Coding Exercise: Divisibility
Write a program that reads two positive integers a and b on separate lines. If a is divisible by b, print the message "divisible". 
Otherwise, print the message "not divisible". For example, when the input is
14
3
the program should print "not divisible".
"""

# delete this comment and enter your code here
a=int(input())
b=int(input())

if a%b==0:
   print("divisible")
else:
   print("not divisible")
