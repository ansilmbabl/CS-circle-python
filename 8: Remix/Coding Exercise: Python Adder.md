# Coding Exercise: Python Adder
Write a program that takes a single input line of the form `«number1»+«number2»`, where both of these represent positive integers, and outputs the sum of the two numbers. 
For example on input `5+12` the output should be `17`. 
<details>
   <summary>
      Hint 1
   </summary>
   
   ![image](https://github.com/ansilmbabl/CS-circle-python/assets/86063895/be783a48-0bbb-4e3a-9ff2-a64660be33da)

</details>

<details>
   <summary>
      Hint 2
   </summary>
   
   ![image](https://github.com/ansilmbabl/CS-circle-python/assets/86063895/d34e8b52-37f7-4a4e-b699-3a7d06d7cadd)

</details>

## Answer 
```python
S = input()
x=0
y=0
for i in range(0,len(S)):
   if S[i] == "+":
      x=int(S[i+1:])
      y=int(S[0:i])
print(x+y)
