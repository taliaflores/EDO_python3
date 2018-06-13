from sympy import *
import numpy as np
#import math
x,y=symbols("x y")
#Resover la ED: y*ln(x)Y' = (y+1)**2/x**2
eq = y(x)*ln(x)*y(x).diff(x)-((y(x)+1)/(x))**2
sol=dsolve(eq,y(x))
print(eq)
print("El resultado es:")
print(sol)