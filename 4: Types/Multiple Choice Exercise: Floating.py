"""
Multiple Choice Exercise: Floating
If we change 1.2 to 1.5 in the above program, what is first line of output?
"""

Your choice: 
1.5 2 3.0

"""
We have to explain two facts here, to see why z was printed as 3.0.
Computing x * y is mixing an int and a float, which Python treats as two floats, giving back z as a float.
The mathematical value of z is 1.5 times 2, which is 3, but stored in inexact decimal form, of type float. 
When Python prints any float, even if its value is a whole number, it is printed ending with .0 to clarify that it is an inexact value.
Also, note that the value and type of y never changed.
"""
