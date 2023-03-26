"""
Coding Exercise: Ending Time

This program takes two lines of input. The first line is a "starting time" expressed in a 24-hour clock with leading zeroes, like 08:30 or 14:07. 
The second line is a duration D in minutes. Print out what time it will be D minutes after the starting time. For example, for input
12:30
47
the correct output would be 13:17. 

All times should be formatted as numbers between 00:00 and 23:59, but the time period may go over midnight. For example, on input
23:59
13
the correct output is 00:12
"""

# delete this comment and enter your code here
t = input()
ta = input()

mini = int(t[0:2])*60 + int(t[3:]) + int(ta)
hour = mini//60
minb = mini - (hour*60)

while hour > 23:
   hour -= 24
if len(str(hour))==1:
   hour = "0"+str(hour)
if len(str(minb))==1:
   minb = "0"+str(minb)
print(str(hour)+":"+str(minb))
