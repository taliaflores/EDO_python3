from matplotlib.pyplot import plot, show
from sympy import *
x,y=symbols("x y")
#Resover la ED: x*Y'-y-(x**2)/(y**2)=0
print("Resolver la ED 1er Orden:")
eq= x*y(x).diff(x)-y(x)-(x**2)/(y(x)**2)
sol=dsolve(eq,y(x))
pprint(eq)
print("El resultado es:")
pprint(sol)
