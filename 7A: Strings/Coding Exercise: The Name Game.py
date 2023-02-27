"""
Coding Exercise: The Name Game

The Name Game lets you make a song out of any person's name. Listen to the song to get an idea of how it works:

Your program should take a person's name as input, for example "pearl," and print out the song like

pearl, pearl, bo-bearl
banana-fana fo-fearl
fee-fi-mo-mearl
pearl!

Note that the entire name appears three times; in addition the name appears three more times with the first letter replaced by b, f, or m. 
(In reality, the song has rules that are more complex than this, but we ignore them for the purposes of this exercise.)
"""

n =input()

print(n+", " +n+", bo-b"+n[1:])

print("banana-fana fo-f"+n[1:])

print("fee-fi-mo-m"+n[1:])

print(n+"!")
