# Coding Exercise: Next Letter

Write a program that takes a character as input (a string of length 1), which you should assume is an upper-case character; 
the output should be the next character in the alphabet. If the input is 'Z', your output should be 'A'. (You will need to use an `if` statement.)

<details>
   <summary>
      For another hint click here
   </summary>
   
   ![image](https://github.com/ansilmbabl/CS-circle-python/assets/86063895/af3c02b8-fab8-4c65-8c2f-76fff407d176)

</details>

## Answer
```python
n=input()

if n == 'Z':
   print("A")
else:
   print(chr(ord(n)+1))
