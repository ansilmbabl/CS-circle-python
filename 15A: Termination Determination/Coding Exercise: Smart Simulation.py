"""
Coding Exercise: Smart Simulation

Write a function execute(prog) to do the following. Assume prog is a list of strings containing the BASIC program, like before. 
Then, your function should return either "success" or "infinite loop" depending on whether the program terminates, or loops forever. 
Important: you should assume the procedure findLine(prog, target) defined in sub-task 2 is already defined, you do not need to re-write it.
"""

def execute(prog):
  location = 0
  visited = [False]*len(prog)
  while True:
    if location==len(prog)-1: 
         return "success"
    #get T from prog[location] via str.split
    elif visited[location] == True:
         return "infinite loop"
    else:
         visited[location] = True
         T = (prog[location].split())[2]
         location = findLine(prog, T)
