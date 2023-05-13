# Multiple Choice Exercise: Inner and Outer
What is the output of the following program?
```PYTHON
x = "outer"
def xReplace(value):
   x = value
xReplace("inner")
print(x)
```
# Your choice: 
    outer

The statement x = value only affects the local version of variable x inside the function. The global version of x does not change. (So, the function xReplace is useless and never has any effect.)
