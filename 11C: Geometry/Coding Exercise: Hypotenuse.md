# Coding Exercise: Hypotenuse

Define a function `hypotenuse(a, b)` which returns the length of the hypotenuse *c*, if the other two sides have lengths *a* and *b*. Hint
<details>
   <summary>
      Hint
   </summary>
   
   ![image](https://github.com/ansilmbabl/CS-circle-python/assets/86063895/50f3063c-d08f-4d22-80f4-2c4f87878635)

</details>

## Answer
```python
import math
def hypotenuse(a, b):
   return math.sqrt(a**2 + b**2)
