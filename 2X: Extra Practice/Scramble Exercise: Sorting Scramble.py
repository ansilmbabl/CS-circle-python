"""
Scramble Exercise: Sorting Scramble

Code scramble: make the program sort the three numbers x, y and z into increasing order, 
so that x has the smallest value, y has the next smallest value, and z has the largest value.
Drag and drop with your mouse to rearrange the lines.

""""


tmp = max(x, y)
x = min(x, y)
y = tmp

tmp = max(y, z)
y = min(y, z)
z = tmp

tmp = max(x, y)
x = min(x, y)
y = tmp
