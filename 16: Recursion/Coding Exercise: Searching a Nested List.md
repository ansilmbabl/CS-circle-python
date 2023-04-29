# Coding Exercise: Searching a Nested List
By writing something similar to nestedListSum, define a recursive function
<br>`nestedListContains(NL, target)`<br>
that takes a nested list NL of integers and an integer target, and indicates whether target is contained anywhere in the nested list. Your code should return the boolean value True when it is contained in the nested list, and False if it is not contained in it.
For example, nestedListContains([1, [2, [3], 4]], 3) should give True and nestedListContains([1, [2, [3], 4]], 5) should give False
# Answer 
```python
# delete this comment and enter your code here
def nestedListContains(NL, target):
   if target in NL:
      return True
   for i in NL:
      if type(i) == list:
         val = nestedListContains(i, target)
         if val == True:
            return True
   return False
```
