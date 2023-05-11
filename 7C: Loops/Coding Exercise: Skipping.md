# Coding Exercise: Skipping

Extend the "Looping through all lines of input" example above (we've copied it for you) by adding a new feature: any line equal to `SKIP` should not be printed, 
and should not cause the counter to be increased. Run the program to see an example.

<details>
   <summary>
      Hint
   </summary>
  
  ![image](https://github.com/ansilmbabl/CS-circle-python/assets/86063895/0795f05a-5a44-4e94-a785-3636b71667ec)

</details>

## Answer
```python
counter = 0
while True:
  lineIn = input()
  if lineIn=='END':
    break
  if lineIn=='SKIP':
         continue
  counter = counter+1
  print('line', counter, '=', lineIn)
