# Coding Exercise: Lower-case Strings

Define a function `lowerString(string)` which returns the result of converting `string` to lower case.

## Answer
```python
# first, copy your definition of lowerChar() here
def lowerChar(char):
   if char>="A" and char<"Z":
      return chr(ord(char)+32)
   else:
      return char
   
# then define lowerString(string)
def lowerString(string):
   x=""
   for i in string:
      x+=lowerChar(i)
   return x
