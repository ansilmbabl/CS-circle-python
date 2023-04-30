# Short Answer Exercise: True Count
How many times does True show up in the output of this program? (Draw a diagram to help keep track.)
```python
list1 = [9, 1, 1]
list3 = list(list1)
list2 = list1
list4 = list3[:]
list1[0] = 4
list5 = list1
print(list1 is list2, list2 is list3, list3 is list4, list4 is list5)
print(list1 == list2, list2 == list3, list3 == list4, list4 == list5)
```

# Answer
Your answer (enter a number): 
    
    3
The output is

    True False False False
    True False True False
