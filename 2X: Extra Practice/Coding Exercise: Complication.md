# Coding Exercise: Complication

Assume that the grader defines two variables A and B for you. Write a program which prints out the value
```
min(A, B)
```

However, there is a catch: your program is not allowed to use the `min` function. Instead, use `max` in a clever way to simulate `min`.
<details>
  <summary>
    Hint, Method 1
  </summary>
  
  ![image](https://user-images.githubusercontent.com/86063895/236968278-a63ab6e8-87ff-4530-a0b3-d8656ddd3dd3.png)

</details>

<details>
  <summary>
    Hint, Method 2
  </summary>
  
 ![image](https://user-images.githubusercontent.com/86063895/236968471-329e05fd-c63d-4395-8941-c3aa04c0f327.png)

</details>

# Answer 
```python
print(A+B - max(A,B))
