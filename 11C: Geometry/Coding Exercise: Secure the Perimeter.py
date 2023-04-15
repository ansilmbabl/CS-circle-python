"""
Coding Exercise: Secure the Perimeter

Assume distance2D(x1, y1, x2, y2) has already been defined. Using it, define a function trianglePerimeter(xA, yA, xB, yB, xC, yC) which calculates 
the perimeter of a triangle whose three points are (xA, yA), (xB, yB) and (xC, yC).
"""

def trianglePerimeter(xA, yA, xB, yB, xC, yC):
   return (distance2D(xA, yA,xB, yB) + distance2D(xB, yB,xC, yC) + distance2D(xA, yA,xC, yC))
