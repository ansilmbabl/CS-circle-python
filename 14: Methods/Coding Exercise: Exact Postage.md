# Coding Exercise: Exact Postage

Define a function `postalValidate(S)` which first checks if `S` represents a postal code which is *valid*:
* first, delete all spaces;
* the remainder must be of the form `L#L#L#` where `L` are letters (in either lower or upper case) and `#` are numbers.

If `S` is not a valid postal code, return the boolean `False`. If S is valid, return a version of the same postal code in the nice format `L#L#L#` where each `L` is capital.

## Answer
```python
def postalValidate(S):
   post = S.replace(" ","")
   digit = post[1:6:2]
   letter = post[0:5:2]
   if len(post)!= 6:
      return False
   elif letter.isalpha() and digit.isdigit():
      return post.upper()
   else:
      return False
