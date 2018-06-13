from sympy import *
from sympy import init_printing
#Para un mejor despliegue de la ED

x,y = symbols("x y")
f,g =map(Function,'fg')

#ED : y'=y*x*sin(x)
ed = Eq(f(x)*Derivative(f(x),x),(f(x)+1)**2/(f(x)**2)
eq = y(x)*ln(x)*y(x).diff(x)-((y(x)+1)/(x))**2
sol = dsolve(ed,f(x))
print("El resultado es:")
pprint(sol)