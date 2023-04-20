"""
Coding Exercise: BASIC Simulator
Put together your BASIC simulator.
"""

def getBASIC():
   stringl = []
   while True:
      x = input()
      stringl.append(x)
      if x.endswith("END"):
         break
   return stringl
 
# def findLine from subtask 2
def findLine(prog, target):
   for i in prog:
      if i.startswith(target):
         return prog.index(i)
 
# def execute from subtask 3
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
         
print(execute(getBASIC()))
