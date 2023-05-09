# Coding Exercise: Second Guessing

Debug this program so that it prints out the number of seconds in a week.
```python
# goal: print out the number of seconds in a week 
secondsPerMinute = 60
secondsPerHour = secondsPerMinute * 50 # todo: check this!
secondsPerDay = secondsPerHour * 24
daysPerWeek = 5
# daysPerWeek = daysPerWeek + 2 # weekends are disabled!?
print(secondsPerDay * daysPerWeek)
```
<details>
  <summary>
    Hint
  </summary>
  
  ![image](https://github.com/ansilmbabl/CS-circle-python/assets/86063895/af37a2e2-e5fa-4ebe-bf34-113e651e7455)
  
</details>

## Answer
```python
# goal: print out the number of seconds in a week 
secondsPerMinute = 60
secondsPerHour = secondsPerMinute * 60 # todo: check this!
secondsPerDay = secondsPerHour * 24
daysPerWeek = 5
daysPerWeek = daysPerWeek + 2 # weekends are disabled!?
print(secondsPerDay * daysPerWeek)
