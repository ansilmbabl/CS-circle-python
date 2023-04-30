# Short Answer Exercise: List Argument
What number is output by the following program?
```python
def func(list):
    list[0] = list[0] + list[1]
    list[1] = list[1] + list[0]
data = [3, 4]
func(data)
print(data[0]*data[1])
```

# Answer
Your answer (enter a number): 

    77
Inside func, we change the element at index 0 to 7, and the element at index 1 to 7+4=11. So we print 7*11.
