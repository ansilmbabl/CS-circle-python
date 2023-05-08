# Scramble Exercise: Speed Calculator

You are in a bike race which goes up and down a hill. 
The grader will pre-define four variables for you: `uphillDistance` and `downhillDistance` give the distance (in km) of both parts of the race, 
and `uphillTime` and `downhillTime` give the time (in minutes) of how long it took you to complete each part of the race. 
Write a program that will print out your average speed (in km/min) for the entire race.

*Drag and drop with your mouse to rearrange the lines.*

<details>
  <summary>
    Click for a hint if you're stuck 
  </summary>
  
  ![image](https://user-images.githubusercontent.com/86063895/236763388-28d85f9e-8041-4b55-8bc9-a75ba290faa7.png)
</details>

## Answer
```python
totalDistance = uphillDistance + downhillDistance
totalTime = uphillTime + downhillTime
averageSpeed = totalDistance / totalTime
print(averageSpeed)
