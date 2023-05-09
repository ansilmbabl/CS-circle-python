# Coding Exercise: Growth Debugging
  
Fix the logic error in this program: it should calculate the population of your country for the next 3 years, assuming it starts with 1000 people in 2012, 
and the number of people increases by 10% each year. You can change at most three characters.
<details>
  <summary>
    If you get stuck, click here for a hint.
  </summary>
  
  ![image](https://user-images.githubusercontent.com/86063895/236968690-76651da7-1f14-4e97-b31e-e2ab4d0cbca5.png)

</details>

## Answer
```python
populationIn2012 = 1000
populationIn2013 = populationIn2012 * 1.1
populationIn2014 = populationIn2013 * 1.1
populationIn2015 = populationIn2014 * 1.1

