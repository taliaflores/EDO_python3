from sympy import *
x,y=symbols("x y")
#Resover la ED: Y' = y*x*sin(x)
eq = y(x).diff(x)-y(x)*x*sin(x)
sol=dsolve(eq,y(x))
pprint(sol)