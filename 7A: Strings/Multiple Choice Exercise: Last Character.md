# Multiple Choice Exercise: Last Character
What expression can be used to determine the **last** character in a string `S`?

## Answer
```python
S[len(S)-1]
```
Although len(S) gives you the total number of characters in the string, since it starts with index 0, the last character is at index len(S)-1.
