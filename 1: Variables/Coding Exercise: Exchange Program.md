# Coding Exercise: Exchange Program
Write a program to `swap` the values of two variables. The grader will automatically define variables x and y for you, with numerical values. 
You must write code that exchanges their values: the value of x after your code runs must equal the value that y had before your code ran, 
and the value of y after your code runs must equal the value that x had before your code ran. Your program does not need to print any output.

*The most common solution is short, but can be hard to find. Click on each hint if you want to read it.*

<details><summary>
Hint, part 1
</summary>
You do not need to use any arithmetic (+-*/) to solve this problem. You only need to use variables and =. You can define new variables with any name, if you need to.
</details>

<details><summary>
Hint, part 2
</summary>
We have two goals: put the original value of y into x, and put the original value of x into y. If all we wanted to do was the first goal (in other words, if we only wanted to put the value of y into x), we could use the one-line program

  ``` 
  x = y 
  ```
How can we do both goals at once?
</details>

<details><summary>
Hint, part 3
</summary>
The following program might seem promising,
  
  ```
  x = y
  y = x
  ```
But there is a problem. For example, let's say that the grader starts by defining x equal to 10 and y equal to 99. If we run the two-line program above, after the first line both x and y will equal 99. The second line has no effect. *You can try submitting this solution to the grader to check for yourself what happens*. How can we keep the original value of x somewhere, in order to put it into y later?
</details>

<details><summary>
Hint, part 4
</summary>
Your first line should be something like xOriginal = x, to store the original value of x for later. Then you can set x = y. Finally, set y equal to the original value of x.
</details>
  
<details><summary>
Hint, part 5
</summary>

[Click to read a wikipedia page](http://en.wikipedia.org/wiki/Swap_(computer_science)#Using_a_temporary_variable) giving pseudocode (in a different language) for swapping. Here is a link to a [second method](http://en.wikipedia.org/wiki/Swap_by_addition_and_subtraction#Variations) that uses arithmetic in a sneaky way, but it will only work with numbers and not with text.
</details>

## Answer
```python
x = x+y
y = x-y
x = x-y

#or
x,y=y,x

#or
a=x
x=y
y=a
