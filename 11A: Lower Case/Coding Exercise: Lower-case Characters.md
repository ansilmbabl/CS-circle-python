# Coding Exercise: Lower-case Characters

Define a function `lowerChar(char)` which meets the above description.
## Answer
```python
def lowerChar(char):
   if char>="A" and char<"Z":
      return chr(ord(char)+32)
   else:
      return char
