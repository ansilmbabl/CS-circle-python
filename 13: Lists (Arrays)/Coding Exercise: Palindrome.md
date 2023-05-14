# Coding Exercise: Palindrome

A *palindrome* is a word which is spelled the same forwards as backwards. For example, the word
`"racecar"`
is a palindrome: the first and last letters are the same (r), the second and second-last letters are the same (a), etc. 
Write a function `isPalindrome(S)` which takes a string `S` as input, and returns `True` if the string is a palindrome, and `False` otherwise.

## Answer
```python
def isPalindrome(S):
   return S == S[::-1]
