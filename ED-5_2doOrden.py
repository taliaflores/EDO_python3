from matplotlib.pyplot import plot, show
from sympy import *
x,y=symbols("x y")
#Resover la ED: y''=4x
print("Resolver la ED 1er Orden:")
eq= y(x).diff(x,x)-4*x
sol=dsolve(eq,y(x))
pprint(eq)
print("El resultado es:")
pprint(sol)
