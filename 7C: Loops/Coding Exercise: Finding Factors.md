# Coding Exercise: Finding Factors

If *a × b = n*, we call *a × b* a factorization of *n*. In this exercise, write a program that takes a positive integer *n* from input, 
and then outputs all factorizations of *n*; you should follow the formatting given by the following example for *n*=10.
```
1 times 10 equals 10
2 times 5 equals 10
5 times 2 equals 10
10 times 1 equals 10
```
<details>
   <summary>
      Hint
   </summary>
   
   ![image](https://github.com/ansilmbabl/CS-circle-python/assets/86063895/8431bf5d-ea47-4606-9a5e-72ecc2b096e4)

</details>

## Answer
```python
n = int(input())
for i in range(1,n+1):
   for j in range(1,n+1):
      if i*j == n:
         print(i,"times",j,"equals",n)
