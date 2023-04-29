# Scramble Exercise: Fractal Ruler
Unscramble the lines to create a program that produces a recursive ruler-like design. For example, when n=3 the program should output the following design.

    -
    --
    -
    ---
    -
    --
    -
    
# Answer
    def ruler(n):
      if n == 1:
       print('-')
      else:
       ruler(n - 1)
       print(n * '-')
       ruler(n - 1)
