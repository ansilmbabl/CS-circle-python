"""
Scramble Exercise: Speed Calculator

You are in a bike race which goes up and down a hill. 
The grader will pre-define four variables for you: uphillDistance and downhillDistance give the distance (in km) of both parts of the race, 
and uphillTime and downhillTime give the time (in minutes) of how long it took you to complete each part of the race. 
Write a program that will print out your average speed (in km/min) for the entire race.
Drag and drop with your mouse to rearrange the lines.

"""

totalDistance = uphillDistance + downhillDistance
totalTime = uphillTime + downhillTime
averageSpeed = totalDistance / totalTime
print(averageSpeed)
