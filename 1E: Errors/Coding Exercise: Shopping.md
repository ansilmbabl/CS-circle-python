# Coding Exercise: Shopping

You are going shopping for meat and milk, but there is tax. You buy $2.00 of milk and $4.00 of meat, and the tax rate is 3%. 
Print out the total cost of your groceries (you don't need to print the dollar sign). 
<details>
  <summary>
    Hint
    </summary>
  
![image](https://user-images.githubusercontent.com/86063895/236764930-6ffb3ec8-3d21-4a03-96c8-4b2632527a53.png)
  
  [rubber duck debugging](http://www.codinghorror.com/blog/2012/03/rubber-duck-problem-solving.html)
</details>

## Answer 
```python
meatPrice = 4.00
meatTax = 0.03 * meatPrice
milkPrice = 2.00
milkTax = 0.03 * milkPrice
print(meatTax + meatPrice + milkTax + milkPrice)

