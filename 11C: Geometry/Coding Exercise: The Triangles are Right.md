# Coding Exercise: The Triangles are Right
Using `hypotenuse(a, b)`, define a function `rightTrianglePerimeter(a, b)` which returns the length of the perimeter in a right triangle whose non-hypotenuse 
sides have lengths *a* and *b*.

## Answer
```python
def rightTrianglePerimeter(a, b):
   return (hypotenuse(a, b) + a+b)
