from sympy import *
"""*Este codigo muestra como resolver una ED-orden-3 con python3 * ..... =)"""
y=symbols('y',cls=Function)
x=symbols('x')
#Resolver la ED-2°Orden:x**3*y'''+6x**2*y"+7xy'+y=0
print("Resolver la ED_de orden 'n' :")
diffeq=Eq(x**3*y(x).diff(x,3)+6*x**2*y(x).diff(x,2)+7*x*y(x).diff(x)+y(x))
sol=dsolve(diffeq,y(x))
pprint(diffeq)
print("El resultado es: ")
pprint(sol)
"""De Esta forma seria el resultado al correr el codigo:


Resolver la ED_de orden 'n' :
     3                2
 3  d             2  d              d
x ⋅───(y(x)) + 6⋅x ⋅───(y(x)) + 7⋅x⋅──(y(x)) + y(x) = 0
     3                2             dx
   dx               dx
El resultado es:
                              2
       C₁ + C₂⋅log(x) + C₃⋅log (x)
y(x) = ───────────────────────────
                    x             



"""