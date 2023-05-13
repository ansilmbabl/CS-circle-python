# Coding Exercise: Alphabet Aerobics

Using what we just introduced, debug the following program so that it outputs the upper-case alphabet *all on one line*.
## Answer
```python
for c in range(0, 26):
 print(chr(ord('A')+c),end="")
