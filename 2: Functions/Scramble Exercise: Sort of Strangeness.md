# Exercise: Code Scramble
Here is another code scramble, where you must drag-and-drop the lines to rearrange them into a correct program.

## Scramble Exercise: Sort of Strangeness
Arrange the code so that it prints the three numbers `x`, `y` and `z` **sorted** in increasing order, so that the smallest is printed first, 
then the middle one, and then the largest one.

*Drag and drop with your mouse to rearrange the lines.*

## Answer
```python
print(min(x, y, z))
print(x+y+z-min(x, y, z)-max(x, y, z))
print(max(x, y, z))
