"""
Coding Exercise: Skipping

Extend the "Looping through all lines of input" example above (we've copied it for you) by adding a new feature: any line equal to SKIP should not be printed, 
and should not cause the counter to be increased. Run the program to see an example.
"""

counter = 0
while True:
  lineIn = input()
  if lineIn=='END':
    break
  if lineIn=='SKIP':
         continue
  counter = counter+1
  print('line', counter, '=', lineIn)
