# Coding Exercise: Reading the Program

Write a function `getBASIC()` which takes no arguments, and does the following: it should keep reading lines from input using a while loop; 
when it reaches the end it should return the whole program in the form of a list of strings. (Hints: about lists and stopping)
<details>
   <summary>
      lists
   </summary>
   
   ![image](https://github.com/ansilmbabl/CS-circle-python/assets/86063895/dcf98d8b-3578-4908-9e66-968555188112)

</details>

<details>
   <summary>
      stopping
   </summary>
   
   ![image](https://github.com/ansilmbabl/CS-circle-python/assets/86063895/cb794434-53e1-4803-840f-f638d30d58f9)

</details>


## Answer
```python
def getBASIC():
   stringl = []
   while True:
      x = input()
      stringl.append(x)
      if x.endswith("END"):
         break
   return stringl
