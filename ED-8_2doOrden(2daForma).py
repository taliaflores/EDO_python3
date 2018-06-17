from sympy import *
"""Este codigo muestra como resolver una ED-orden-2 con python3 ..... =)"""
y=symbols('y',cls=Function)
x=symbols('x')
#Resolver la ED-2°Orden:x**2*y"+2xy'-12y=0     /lo cual x**2 es igual a x al cuadrado
print("Resolver la ED:")
diffeq=Eq(x**2*y(x).diff(x,2)+2*x*y(x).diff(x)-12*y(x))
sol=dsolve(diffeq,y(x))
pprint(diffeq)
print("El resultado es: ")
pprint(sol)
#pprint() :lo utilizamos para poder ver la solucion o ejercicio de forma mas ordenada

"""De Esta forma seria el resultado al correr el codigo:

Resolver la ED:
     2
 2  d              d
x ⋅───(y(x)) + 2⋅x⋅──(y(x)) - 12⋅y(x) = 0
     2             dx
   dx
El resultado es:
       C₁       3
y(x) = ── + C₂⋅x
        4
       x

"""