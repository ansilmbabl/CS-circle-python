# Coding Exercise: Poetic Analysis
A writer is working on their newest poem, Turing and the Machines. They have hired you to determine the word which appears the most times. You can access the lines of the poem by calling `input()` repeatedly, and the last line contains the three characters `###`. All lines consist of words separated by single spaces; there are no digits or punctuation. Convert all the words to lower-case, and **print the word that occurs the most time** (we guarantee there will not be a tie). For example, if the input is
    
    Here is a line like sparkling wine
    Line up fast or be the last
    ###
Then the output should be
    
    line
since it appears twice and no other word appears twice.

## Answer 
```python
# delete this comment and enter your code here
t = ""
list = []
count = []
while t!= "###":
   t=input()
   words = t.lower().split()
   for i in words:
      if i in list:
         count [list.index(i)] +=1
      else:
         list.append(i)
         count.append(1)
print( list[count.index(max(count))] )
