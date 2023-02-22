"""
Coding Exercise: IHOPython

Write a program which reads an integer from input using pancakes = int(input()). If pancakes is more than 3, print out Yum! and if pancakes is not more than 3, 
print out Still hungry! instead.
"""


pancakes = int(input())
if pancakes<=3:
   print("Still hungry!")
if pancakes>3:
   print("Yum!")
