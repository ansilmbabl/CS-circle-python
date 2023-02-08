"""
Coding Exercise: Second Guessing

Debug this program so that it prints out the number of seconds in a week.

"""

# goal: print out the number of seconds in a week 
secondsPerMinute = 60
secondsPerHour = secondsPerMinute * 60 # todo: check this!
secondsPerDay = secondsPerHour * 24
daysPerWeek = 5
daysPerWeek = daysPerWeek + 2 # weekends are disabled!?
print(secondsPerDay * daysPerWeek)

