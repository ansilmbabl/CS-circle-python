"""
Coding Exercise: Square Census

The square numbers are the integers of the form K × K, e.g. 9 is a square number since 3 × 3 = 9.
Write a program that reads an integer n from input and outputs all the positive square numbers less than n, one per line in increasing order.
For example, if the input is 16, then the correct output would be

1
4
9
"""

n=int(input())
for i in range(1,n//2):
   if (i*i) < n:
      print(i*i)
