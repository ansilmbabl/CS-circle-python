# Coding Exercise: Heads and Tails
Write a program which reads a string using `input()`, and outputs the same string but with the first and last character **exchanged**. (You may assume the input string has length at least 2.) For example, on input `Fairy` a correct program will print `yairF`. Hint: use your solution to the previous program as part of the answer.

## Answer
```python
n = input()
print(n[-1]+n[1:len(n)-1]+n[0])
