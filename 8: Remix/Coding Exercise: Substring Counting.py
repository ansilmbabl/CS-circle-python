"""
Coding Exercise: Substring Counting

As mentioned in lesson 7A, a substring is any consecutive sequence of characters inside another string. The same substring may occur several times inside the same string:
for example "assesses" has the substring "sses" 2 times, and "trans-Panamanian banana" has the substring "an" 6 times. Write a program that takes two lines of input, 
we call the first needle and the second haystack. Print the number of times that needle occurs as a substring of haystack.
"""
needle = input()
haystack = input()

c=0
x=""
for i in haystack:
   x+=i
   if x[len(x)-1:-(len(needle)+1):-1] == needle[::-1]:
      c+=1
print(c)
