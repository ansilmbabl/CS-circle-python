"""
Coding Exercise: Reading the Program

Write a function getBASIC() which takes no arguments, and does the following: it should keep reading lines from input using a while loop; 
when it reaches the end it should return the whole program in the form of a list of strings. (Hints: about lists and stopping)
"""

def getBASIC():
   stringl = []
   while True:
      x = input()
      stringl.append(x)
      if x.endswith("END"):
         break
   return stringl
