# Coding Exercise: Absolute Value

The absolute value of a number is defined as follows. For a number x that is positive or zero, the absolute value of x is x. 
Otherwise, when x is a negative number, the absolute value of x is -x, or in other words the same as x but without the minus sign. 
For example the absolute value of `5` is `5`, and the absolute value of `-10` is `10`. Using `if` and `else`, write a program that reads an integer as input, 
and prints its absolute value.

## Answer
```python

x=int(input())
# delete this comment and enter your code here
if x>=0:
   print(x)
else:
   print(-x)
