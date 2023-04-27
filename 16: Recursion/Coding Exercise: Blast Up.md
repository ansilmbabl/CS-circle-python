# Coding Exercise: Blast Up
Write a recursive function countup(n) which prints 'Blastoff!' followed by the numbers 1 to n on separate lines.

```python
def countup(n):
  if n == 0:
    print('Blastoff!')
  else:
    countup(n - 1)
    print(n)
```
