# Coding Exercise: Substring Counting

As mentioned in lesson 7A, a substring is any consecutive sequence of characters inside another string. The same substring may occur several times inside the same string:
for example "assesses" has the substring "sses" 2 times, and "trans-Panamanian banana" has the substring "an" 6 times. Write a program that takes two lines of input, 
we call the first `needle` and the second `haystack`. Print the number of times that `needle` occurs as a substring of `haystack`.


<details>
   <summary>
      Hint
   </summary>
   
   ![image](https://github.com/ansilmbabl/CS-circle-python/assets/86063895/540966ad-614c-441a-9adf-1e57f528b61d)

</details>

## Answer
```python
needle = input()
haystack = input()

c=0
x=""
for i in haystack:
   x+=i
   if x[len(x)-1:-(len(needle)+1):-1] == needle[::-1]:
      c+=1
print(c)
