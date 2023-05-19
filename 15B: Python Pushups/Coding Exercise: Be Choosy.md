# Coding Exercise: Be Choosy
The number of combinations of k things out of a total of n things is equal to
$$\displaystyle{\frac{n}{k}\times\frac{n-1}{k-1}\times\frac{n-2}{k-2}\times\cdots\times\frac{n-k+2}{2}\times\frac{n-k+1}{1}}$$

Write a function `choose(n, k)` which takes two integers n and k; we guarantee n>k>0. The function should return the value given in the formula above.<br>
*Note that for this exercise, we expect you to just mechanically compute this formula without trying to understand it. But if you're interested, here's a [sample YouTube video explaining it.](https://youtu.be/w1nlzDAVyzk?t=3130)*

## Answer 
```python
# delete this comment and enter your code here
def choose(n, k):
   c = n/k
   for i in range(k-1):
      n-=1
      k-=1
      c*= n/k
   return c
