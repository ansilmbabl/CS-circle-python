# Coding Exercise: Forty Below In The Winter
In this exercise, you will create a temperature converter which will convert Fahrenheit values to Celsius and vice-versa. You will need the following two formulas which relate the temperature f in Fahrenheit to the temperature c in Celsius:

![https://s0.wp.com/latex.php?latex=%5Cdisplaystyle%7Bf+%3D+c+%5Ctimes+%5Cfrac%7B9%7D%7B5%7D+%2B+32%7D&bg=T&fg=000000&s=0](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle%7Bf+%3D+c+%5Ctimes+%5Cfrac%7B9%7D%7B5%7D+%2B+32%7D&bg=T&fg=000000&s=0)

![https://user-images.githubusercontent.com/86063895/233854689-2ce332e0-ff2d-4595-99b1-afc0e1801191.png](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle%7Bc+%3D+%28f+-32%29%5Ctimes%5Cfrac%7B5%7D%7B9%7D.%7D&bg=T&fg=000000&s=0)

The input will be a string consisting of a floating-point number followed immediately by the letter F or C, such as "13.2C". You should convert to the other temperature scale and print the converted value in the same format. For example, if the input is "8F" then the output should be (approximately) "-13.333C", and if the input is "12.5C" then the output should be "54.5F".

    def ftc(f):
       print( ((f-32)*5/9),end="C" )

    def ctf(c):
       print( ((c*9/5)+32),end= "F" )

    t = input()
    if t[-1] == "F":
       ftc(float(t[:len(t)-1]))
    if t[-1] == "C":
       ctf(float(t[:len(t)-1]))
