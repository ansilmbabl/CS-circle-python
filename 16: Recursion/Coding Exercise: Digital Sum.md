# Coding Exercise: Digital Sum
The digital sum of a number n is the sum of its digits. Write a recursive function digitalSum(n) that takes a positive integer n and returns its digital sum. For example, digitalSum(2019) should return 12 because 2+0+1+9=12.
```python
def digitalSum(n):
  if n < 10:
    return n
  else:
      return n%10 + digitalSum(n//10)
```
