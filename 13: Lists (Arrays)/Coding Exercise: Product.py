"""
Coding Exercise: Product

Define a function prod(L) which returns the product of the elements in a list L.
"""

def prod(L):
   x=1
   for i in range(0,len(L)):
      x*=L[i]
   return x
