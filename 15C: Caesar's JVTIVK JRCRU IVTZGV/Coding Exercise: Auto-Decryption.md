# Coding Exercise: Auto-Decryption
Write a program which does the following. First, it should read one line of input, which is the encoded message, and will consist of capital letters and spaces. Your program must try decoding the message with all 26 possible values of the shift S; out of these 26 possible original messages, print the one which has the highest goodness.
For your convenience, we will pre-define the variable `letterGoodness` for you, a list of length 26 which equals the values in the frequency table above,
```
letterGoodness = [.0817,.0149,.0278,.0425,.1270,.0223,.0202,...
```
<details>
    <summary>
        Click here for some general advice.
    </summary>
    
   ![image](https://github.com/ansilmbabl/CS-circle-python/assets/86063895/8bbbd2cf-b602-4bb4-8a8b-44e1bcbb1ec7)

</details>

## Answer
```python
def dc(S,shift):
   x =""
   for i in S:
      if i.isalpha():
          position = ord(i)-shift
          if position<65:
               position+=26
          x += chr(position)
      else:
         x+=i
   return x

def goodness(S):
   list = []
   list_goodness = []
   for i in range(1,27):
      decrypted = dc(S,i)
      list.append(decrypted)
      goodness = 0
      for j in decrypted:
         if j.isalpha():
            goodness_value = letterGoodness[ord(j)-65]
            goodness += goodness_value
      list_goodness.append(goodness)
   return list[list_goodness.index(max(list_goodness))]


l =input()
print(goodness(l))
```
