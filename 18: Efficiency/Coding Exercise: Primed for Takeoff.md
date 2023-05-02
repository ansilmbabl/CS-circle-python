# Coding Exercise: Primed for Takeoff
Write a program that defines the table `isPrime` we described above (notice that `isPrime` is a list, not a function).
The grader will allow a longer-than-usual amount of time, 7 seconds, for your program to execute. However, simply using the `isItPrime` function will not be fast enough.

# Answer
```python
isPrime = [True]*1000001
isPrime[0] = False
isPrime[1] = False

for i in range(2,len(isPrime)):
   if isPrime[i] == True:
      for j in range(i*i,len(isPrime),i):
         isPrime[j] = False
