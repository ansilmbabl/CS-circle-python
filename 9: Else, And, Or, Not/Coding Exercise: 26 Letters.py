"""
Coding Exercise: 26 Letters

Write a program which does the reverse of the example above: it should take a character as input and output the corresponding number (between 1 and 26). 
Your program should only accept capital letters. As error-checking, print invalid if the input is not a capital letter.
"""

letter = input()
# delete this comment and enter your code here
if ord(letter) >= ord("A") and ord(letter)<ord("Z"):
   print(ord(letter)-64)
else:
   print('invalid')
