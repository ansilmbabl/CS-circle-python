"""
Coding Exercise: Pig Latin

Pig Latin is a nonsense language. To transform a word from English to Pig Latin, you move the first letter to the end and add "ay" after that. 
For example, monkey becomes onkeymay in Pig Latin, and word becomes ordway. Write a program that takes a single word as input and translates it to Pig Latin. 
(In reality, Pig Latin has rules that are more complex than this, but we ignore them for the purposes of this exercise.)
"""

w=input()
print(w[1:]+w[0]+'ay')
