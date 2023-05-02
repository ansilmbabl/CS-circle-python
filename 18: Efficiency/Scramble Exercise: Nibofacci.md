# Scramble Exercise: Nibofacci
Unscramble this program so that it gives a recursive definition of the Fibonacci numbers. The grader will print out the first ten of them.

# Answer
```python
def Fibonacci(n):
    if (n==1 or n==2):
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
