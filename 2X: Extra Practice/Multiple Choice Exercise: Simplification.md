# Multiple Choice Exercise: Simplification

What is a simplification of the following expression?
```
max(x - 3, min(x + 10, x + 5))
```

## Answer
```python
x + 5
```

Since x + 5 is always smaller than x + 10, we can simplify min(x + 10, x + 5) to just x + 5. Then working our way outwards, the entire expression is max(x - 3, x + 5). Since x + 5 is always the maximum of these two numbers, that is the result.
