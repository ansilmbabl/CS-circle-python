# Coding Exercise: 26 Letters

Write a program which does the reverse of the example above: it should take a character as input and output the corresponding number (between 1 and 26). 
Your program should only accept capital letters. As error-checking, print `invalid` if the input is not a capital letter.
<details>
   <summary>
      Hint
   </summary>
   
   ![image](https://github.com/ansilmbabl/CS-circle-python/assets/86063895/594583e3-b212-4851-9a79-02c0195ca773)

</details>

<details>
   <summary>
      Alternate string comparison method
   </summary>
   
   ![image](https://github.com/ansilmbabl/CS-circle-python/assets/86063895/4dd2fbb4-6304-413d-a5b9-406f79e90169)

</details>

## Answer
```python
letter = input()
# delete this comment and enter your code here
if ord(letter) >= ord("A") and ord(letter)<ord("Z"):
   print(ord(letter)-64)
else:
   print('invalid')
