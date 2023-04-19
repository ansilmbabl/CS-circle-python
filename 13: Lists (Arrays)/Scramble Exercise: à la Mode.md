# Scramble Exercise: à la Mode
The mode of a list is the element which occurs most frequently (the one which appears the maximum number of times). 
Unscramble the following program so that mode(L) correctly finds the mode, assuming L is a list of numbers from 0 to 9. 
(On our tests, there won't be two numbers tied for the maximum frequency.)

    def mode(L):
      frequency = [0]*10
      for i in L:
        frequency[i] = frequency[i] + 1
      for i in range(0, 10):
        if frequency[i]==max(frequency):
          return i
