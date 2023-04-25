# Coding Exercise: Be Choosy
The number of combinations of k things out of a total of n things is equal to
![](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle%7B%5Cfrac%7Bn%7D%7Bk%7D%5Ctimes%5Cfrac%7Bn-1%7D%7Bk-1%7D%5Ctimes%5Cfrac%7Bn-2%7D%7Bk-2%7D%5Ctimes%5Ccdots%5Ctimes%5Cfrac%7Bn-k%2B2%7D%7B2%7D%5Ctimes%5Cfrac%7Bn-k%2B1%7D%7B1%7D%7D&bg=T&fg=000000&s=2)

Write a function `choose(n, k)` which takes two integers n and k; we guarantee n>k>0. The function should return the value given in the formula above.
Note that for this exercise, we expect you to just mechanically compute this formula without trying to understand it. But if you're interested, here's a [sample YouTube video explaining it.](https://youtu.be/w1nlzDAVyzk?t=3130)

# Answer 
    # delete this comment and enter your code here
    def choose(n, k):
       c = n/k
       for i in range(k-1):
          n-=1
          k-=1
          c*= n/k
       return c
