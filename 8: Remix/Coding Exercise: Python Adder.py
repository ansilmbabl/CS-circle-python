"""
Coding Exercise: Python Adder
Write a program that takes a single input line of the form «number1»+«number2», where both of these represent positive integers, and outputs the sum of the two numbers. 
For example on input 5+12 the output should be 17. 
"""
S = input()
# delete this comment and enter your code here
x=0
y=0
for i in range(0,len(S)):
   if S[i] == "+":
      x=int(S[i+1:])
      y=int(S[0:i])
print(x+y)
