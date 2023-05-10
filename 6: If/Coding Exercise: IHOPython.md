# Coding Exercise: IHOPython

Write a program which reads an integer from input using `pancakes = int(input())`. If pancakes is more than 3, print out `Yum!` and if pancakes is not more than 3, 
print out `Still hungry!` instead.

<details>
   <summary>
      Hint
   </summary>
   
   ![image](https://github.com/ansilmbabl/CS-circle-python/assets/86063895/d9d68803-f233-4cc9-9c92-ec0a78605bdc)
   
</details>

## Answer
```python
pancakes = int(input())
if pancakes<=3:
   print("Still hungry!")
if pancakes>3:
   print("Yum!")
