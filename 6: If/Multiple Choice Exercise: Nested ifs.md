# Multiple Choice Exercise: Nested ifs
Which of the following outputs is **not** possible for this program?

## Answer
```
one line: 'User logged on.'
```
Correct! If any messages are shown, it must be the case that the outer (blue) block was executed, or in other words the password was correct. 
In this case, even if `hour>17` is false (and the inner block is skipped), the line `print('Enter a command:')` of the outer block will still be executed.
