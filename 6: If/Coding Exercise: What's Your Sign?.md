# Coding Exercise: What's Your Sign?
Write a program that reads an integer from input, then outputs one of the capitalized words `Positive`, `Negative`, or `Zero` 
according to whether the number is positive, negative, or zero.

## Answer
```python
x=int(input())
if x>0:
 print("Positive")
if x<0:
 print("Negative")
if x==0:
 print("Zero")
