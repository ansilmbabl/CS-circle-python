"""
Coding Exercise: Eggsactly

Egg cartons each hold exactly 12 eggs. Write a program which reads an integer number of eggs from input(), 
then prints out two numbers: how many cartons can be filled by these eggs, and how many eggs will be left over. 
For example, the output corresponding to 27 eggs is
2
3
since 27 eggs fill 2 cartons, leaving 3 eggs left over. Hint
"""
# delete this comment and enter your code here

n=int(input())
print(n//12)
print(n%12)
