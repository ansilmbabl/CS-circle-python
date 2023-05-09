# Exercise

This is a two-part exercise using the min and max functions. There are connections between the cities of Maxime and Miniac with several bridges. 
There is a separate limit on the amount of weight that can be transported across each bridge.

## Coding Exercise: One Road
For part 1, there is a single road between the two cities. The road has three bridges with weight limits `a`, `b`, `c`, as shown in the picture below:

In order to drive along the route, your truck needs to drive first over the bridge with weight limit a, then the one with weight limit b, 
then the one with weight limit c. Your truck will crash if you overload any of the three weight limits. 
*Write a program that prints out the maximum weight that can be transported along this road.*

Your code should assume that the variables `a`, `b`, and `c` already contain the bridge weight limits.

![one-road cscircle](https://user-images.githubusercontent.com/86063895/216822700-e8155a9c-5eb0-4f06-82d2-055ec0f1333a.png)


## Answer
```python
print(min(a,b,c))

