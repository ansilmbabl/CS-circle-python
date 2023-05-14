# Multiple Choice Exercise: Meta-Stuff
What is the output of the following code fragment?

```python
stuff = [2, 25, 80, 12]
stuff[stuff[0]] = stuff[3]
print(stuff)
```

## Answer
```python
[2, 25, 12, 12]
```
Look at the assignment statement (the 2nd line). The value of stuff[3] on the right side is 12. For the left side, stuff[0] is 2, so stuff[stuff[0]] refers to the variable stuff[2]. The value of this variable is updated (from 80) to 12.
