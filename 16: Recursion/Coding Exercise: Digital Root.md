# Coding Exercise: Digital Root
The digital root of a non-negative integer n is computed as follows. Begin by summing the digits of n. The digits of the resulting number are then summed, and this process is continued until a single-digit number is obtained. For example, the digital root of 2019 is 3 because 2+0+1+9=12 and 1+2=3. Write a recursive function `digitalRoot(n)` which returns the digital root of n.<br>
**Assume** that a working definition of `digitalSum` will be provided for your program.

## Answer
```python
# delete this comment and enter your code here   
def digitalRoot(n):
   if n>=10:
      return digitalRoot(digitalSum(n))
   else:
      return n
```
