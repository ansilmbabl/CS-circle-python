"""
Coding Exercise: String Shaving
Write a program which reads a string using input(), and outputs the same string but with the first and last character deleted. 
(You may assume the input string has length at least 2.) For example, on input Fairy a correct program will print air.
"""

n = input()
print(n[1:len(n)-1])
