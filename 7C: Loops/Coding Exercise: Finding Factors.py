"""
Coding Exercise: Finding Factors

If a × b = n, we call a × b a factorization of n. In this exercise, write a program that takes a positive integer n from input, 
and then outputs all factorizations of n; you should follow the formatting given by the following example for n=10.

1 times 10 equals 10
2 times 5 equals 10
5 times 2 equals 10
10 times 1 equals 10
"""

n = int(input())
for i in range(1,n+1):
   for j in range(1,n+1):
      if i*j == n:
         print(i,"times",j,"equals",n)
