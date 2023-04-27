# Coding Exercise: Double Time
Modify this recursive program to correctly count down in increments of 2.
```python
def countdownBy2(n):
  if n <= 0:
    print('Blastoff!')
  else:
    print(n)
    countdownBy2(n - 2)
```
