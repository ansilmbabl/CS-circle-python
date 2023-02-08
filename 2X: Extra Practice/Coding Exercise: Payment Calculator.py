"""
Coding Exercise: Payment Calculator

A credit card company computes a customer's "minimum payment" according to the following rule. 
The minimum payment is equal to either $10 or 2.1% of the customer's balance, whichever is greater; but if this exceeds the balance, 
then the minimum payment is the balance. Write a program to print out the minimum payment using min and max. 
Assume that the variable balance contains the customer's balance. Your program does not need to print the dollar sign.


Example 1: if your balance is 1000, then your program should print 21.
Example 2: if your balance is 600, then your program should print 12.6.
Example 3: if your balance is 25, then your program should print 10.
Example 4: if your balance is 8, then your program should print 8.
"""

#Answer

print(min(balance,max(10,balance*.021)))
