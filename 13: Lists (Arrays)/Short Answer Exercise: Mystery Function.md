# Short Answer Exercise: Mystery Function
What is the value of x which will cause mystery(x) to run forever?

    def mystery(x):
      a = [0, 4, 0, 3, 2]
      while x > 0:
        x = a[x]
      return "Done"
# Your answer: 

    3
