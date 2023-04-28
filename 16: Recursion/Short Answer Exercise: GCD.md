# Short Answer Exercise: GCD
What is the output of the following recursive program?
```python
def gcd(a, b):
  if b == 0: return a
  return gcd(b, a % b)
print(gcd(20, 12))
```
# Your answer (enter a number): 
    4
This remarkably short program computes the greatest common divisor of two numbers. This is known as the Euclidean Algorithm, one of the oldest known algorithms.
