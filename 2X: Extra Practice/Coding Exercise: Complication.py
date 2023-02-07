"""
Coding Exercise: Complication

Assume that the grader defines two variables A and B for you. Write a program which prints out the value
--> min(A, B)

However, there is a catch: your program is not allowed to use the min function. Instead, use max in a clever way to simulate min.
"""
#Answer 

print(A+B - max(A,B))
