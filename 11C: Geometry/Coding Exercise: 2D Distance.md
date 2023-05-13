# Coding Exercise: 2D Distance

Assume `hypotenuse(a, b)` has already been defined. Using it, define a function `distance2D(x1, y1, x2, y2)` which calculates the distance between the point (x1, y1) and 
the point (x2, y2).
## Answer 
```python
def distance2D(x1, y1, x2, y2):
   return hypotenuse(x1-x2, y1-y2)
