# Coding Exercise: Divisibility
Write a program that reads two positive integers a and b on separate lines. If a is divisible by b, print the message "divisible". 
Otherwise, print the message "not divisible". For example, when the input is
```
14
3
```
the program should print "not divisible".
<details>
   <summary>
      Hint
   </summary>
   
   ![image](https://github.com/ansilmbabl/CS-circle-python/assets/86063895/b5f1ad9e-70d6-4151-b414-df700c98b8dc)

</details>


## Answer

```python
a=int(input())
b=int(input())

if a%b==0:
   print("divisible")
else:
   print("not divisible")
