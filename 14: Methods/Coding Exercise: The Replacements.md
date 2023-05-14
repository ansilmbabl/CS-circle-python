# Coding Exercise: The Replacements

Using index and other list methods, write a function `replace(list, X, Y)` which replaces all occurrences of `X` in `list` with `Y`. For example, 
if `L = [3, 1, 4, 1, 5, 9]` then `replace(L, 1, 7)` would change the contents of `L` to `[3, 7, 4, 7, 5, 9]`. To make this exercise a challenge, you are not allowed to use `[]`. 
Note: you don't need to use return.

<details>
      <summary>
            Hint
      </summary>
      
   ![image](https://github.com/ansilmbabl/CS-circle-python/assets/86063895/96e28d0c-50e9-4ffe-b6e2-3495e02ac2ec)

      
</details>

## Answer
```python

def replace(list, X, Y):
      while X in list:
         list.insert(list.index(X),Y)
         list.remove(X)
