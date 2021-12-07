print("DERIVADAS")

from sympy import*
x = Symbol('x')
parte1 = input("primer numero: ")
parte2 = input("exponente: ")
funcion = parte1+"*x**"+parte2
print(diff(funcion, x))
'''
from sympy import Symbol
from scipy.misc import derivative#Formulas de diferencias centradas
x = Symbol('x')
#y = n*x**e
n = int("ingrese la funcion: ")
print(diff(funcion,x))
'''

#derivada = y.diff(x)
#print(derivada)

#f = lambda x: 
#print(derivative(f, -3, dx = 1e-13))#espacio entre puntos a calcular


'''
from sympy import Symbol
from scipy.misc import derivative#Formulas de diferencias centradas
x = Symbol('x')
y = 2*x**2
derivada = y.diff(x)
print(derivada)
f = lambda x: 2*x**3
print(derivative(f, -3, dx = 1e-13))#espacio entre puntos a calcular
'''

'''
print(derivative(f, -2, dx = 1e-6))
print(derivative(f, -1, dx = 1e-6))
print(derivative(f, 0, dx = 1e-6))
print(derivative(f, 1, dx = 1e-6))
print(derivative(f, 2, dx = 1e-6))
print(derivative(f, 3, dx = 1e-6))
'''


