# Coding Exercise: Centering Text

For this program, the first line of input is an integer `width`. Then, there are some lines of text; the line `"END"` indicates the end of the text. 
For each line of text, you need to print out a centered version of it, by adding periods `..` to the left and right, so that the total length of each line of text is width.
(All input lines will have length at most `width`.) Centering means that the number of periods added to the left and added to the right should be equal if possible; 
if needed we allow one more period on the left than the right. For example, for input
```
Text
in
the
middle!
END
```
the correct output would be
```
.....Text....
......in.....
.....the.....
...middle!...
```
<details>
   <summary>
      Hint
   </summary>
   
   ![image](https://github.com/ansilmbabl/CS-circle-python/assets/86063895/96fd3fa0-f165-4fd9-a9a6-be135b26b18b)

</details>

## Answer
```python

width = int(input())
while True:
   t=input()
   if t=="END":
      break
   l1 = (width - len(t) )//2
   l2 = width - l1 - len(t)
   print((l2*".")+t+(l1*"."))
