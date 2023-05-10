# Coding Exercise: Age checker

Write a program that reads an integer from input, representing someone's age. If the age is 18 or larger, print out `You can vote`. 
If the age is between 0 and 17 inclusive, print out `Too young to vote`. If the age is less than 0, print out `You are a time traveller`.

## Answer
```python
age = int(input())
if age >=18:
 print("You can vote")
if age <18:
 if  age>=0:
  print("Too young to vote")
if age<0:
  print("You are a time traveller")


