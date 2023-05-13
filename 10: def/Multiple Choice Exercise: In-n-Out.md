# Multiple Choice Exercise: In-n-Out


What is the output of the following program?
```python
def f():          # function of 0 arguments
   print("in f")
print("not in f")
f()               # call f now
```

# Your choice: 
```
2 lines: 'not in f', then 'in f'
```
The function f is defined first of all, but its body is not executed immediately. After the function is defined we print out not in f. Then the function is called, and the body is executed, printing in f.
