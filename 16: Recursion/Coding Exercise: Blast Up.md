# Coding Exercise: Blast Up
Write a recursive function `countup(n)` which prints 'Blastoff!' followed by the numbers `1` to `n` on separate lines.

<details>
  <summary>
    Hint
  </summary>
  
  ![image](https://github.com/ansilmbabl/CS-circle-python/assets/86063895/a7c900d6-35b1-4114-bf61-578e354172f5)

</details>
 
## Answer
```python
def countup(n):
  if n == 0:
    print('Blastoff!')
  else:
    countup(n - 1)
    print(n)
```
