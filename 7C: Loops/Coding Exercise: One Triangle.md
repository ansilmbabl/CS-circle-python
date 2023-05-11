# Coding Exercise: One Triangle

Modify the previous program in two ways. First, instead of a square, make it draw a triangle shaped like this: ◤. 
Second, instead of always having `5` lines, it should take the desired size as input from `input()`. 
For example, if the input is `3`, then the output should be
```
111
11
1
```
<details>
   <summary>
      Click here for a hint
   </summary>
   
   ![image](https://github.com/ansilmbabl/CS-circle-python/assets/86063895/eb7f6d98-dec6-458e-80c5-03a13118855b)

</details>

## Answer
```python
n=int(input())

for i in range(0,n):
   x=0
   for j in range(i,n):
      x=(x*10)+1

   print(x)
