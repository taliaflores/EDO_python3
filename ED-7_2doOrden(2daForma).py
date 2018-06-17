from sympy import *
y=symbols('y',cls=Function)

x=symbols('x')
#Declaramos ED :2y(x)+2(dy(x)/dx)+(d**2*y(qx)/(dx**2)=x**2+sin(x)+e**-x
print("Resolver la ED:")
diffeq=Eq(y(x).diff(x,2)+2*y(x).diff(x)+2*y(x),exp(-x)+x**2+sin(x))
sol=dsolve(diffeq,y(x))
pprint(diffeq)
print("El resultado es: ")
pprint(sol)