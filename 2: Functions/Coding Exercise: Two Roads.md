# Coding Exercise: Two Roads

Part #2: Now we will tell you the whole story. There is also a **second route** consisting of two bridges, the first with weight limit `d`, 
and the second with weight limit `e`, as illustrated below.

Your truck can take either route. Write a program that prints out the maximum weight that can be transported between the two cities. 
Assume that the variables `a`, `b`, `c`, `d`, and `e` contain the bridge weight limits. 
<details>
  <summary>
Hint 
    </summary>
  
  ![image](https://user-images.githubusercontent.com/86063895/236965897-2ed64736-f54b-41de-a0ce-edf06c874f2e.png)

  </details>
  
<details>
  <summary>
    Hint 2 
    </summary>
  
  ![image](https://user-images.githubusercontent.com/86063895/236965956-d320d83a-25cd-4051-85ad-eb911838f8e8.png)

  </details>
  
![two-roads cs cirlce](https://user-images.githubusercontent.com/86063895/216823237-8efa2e15-1eea-4da5-b6e4-efe6fcedaa51.png)

## Answer 
```python
print(max(min(a,b,c),min(d,e)))
