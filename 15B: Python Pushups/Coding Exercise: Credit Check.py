"""
Coding Exercise: Credit Check

You have been hired by MeisterCard to write a function which checks if a given credit card number is valid. Your function check(S) should take a string S as input. 
First, if the string does not follow the format "#### #### #### ####" where each # is a digit, then it should return False. 
Then, if the sum of the digits is divisible by 10 (a "checksum" method), then the procedure should return True, else it should return False. For example, 
if S is the string "9384 3495 3297 0123" then although the format is correct, the digit sum is 72 so you should return False.
"""

def check(S):
   if len(S) == 19:
      numbers = S.split()
      sum = 0
      for i in numbers:
         if len(i) == 4 and i.isdigit():
            for j in i:
               sum+=int(j)
         else:
            return False
      if sum%10 != 0:
         return False
      return True
   return False
