# Coding Exercise: Digital Sum
The digital sum of a number n is the sum of its digits. Write a recursive function `digitalSum(n)` that takes a positive integer n and returns its digital sum. For example, `digitalSum(2019)` should return 12 because 2+0+1+9=12.
<details>
  <summary>
    Hint1
  </summary>
  
  ![image](https://github.com/ansilmbabl/CS-circle-python/assets/86063895/40be9fe7-8c98-42af-b2c4-2dfcca226187)

</details>
<details>
  <summary>
    Hint2
  </summary>
  
  ![image](https://github.com/ansilmbabl/CS-circle-python/assets/86063895/6315a71d-8a93-4572-9511-7e124bf6140a)

</details>

```python
def digitalSum(n):
  if n < 10:
    return n
  else:
  # recursive case
# delete this comment and enter your code here
```
## Answer
```python
def digitalSum(n):
  if n < 10:
    return n
  else:
      return n%10 + digitalSum(n//10)
```
