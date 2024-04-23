from random import random
import numpy as np


def MonteCarlo_01(g, Nsim):
    integral = 0
    for _ in range(Nsim):
        integral += g(random())
    return integral / Nsim


def MonteCarlo_ab(g, a, b, Nsim):
    integral = 0
    for _ in range(Nsim):
        integral += g(a + (b - a) * random())
    return integral * (b - a) / Nsim


def MonteCarlo_0inf(g, Nsim):
    integral = 0
    for _ in range(Nsim):
        y = random()
        integral += g(1 / y - 1) / (y**2)
    return integral / Nsim


# Integrales múltiples, 2 variables
# Integral Monte Carlo en el intervalo (0,1)x(0,1)
def MonteCarlo_01_2(fun, Nsim):
    Integral = 0
    for _ in range(Nsim):
        Integral += fun(random(), random())
    return Integral / Nsim


# Integral Monte Carlo en el intervalo (a,b)x(c,d)
def MonteCarlo_ab_2(fun, a, b, c, d, Nsim):
    Integral = 0
    for _ in range(Nsim):
        Integral += fun(a + (b - a) * random(), c + (d - c) * random())
    return Integral * (b - a) * (d - c) / Nsim


# Integral Monte Carlo en el intervalo (0,inf)x(0,inf)
def MonteCarlo_inf_2(g, Nsim):
    Integral = 0
    for _ in range(Nsim):
        u1 = random()
        u2 = random()
        Integral += g(1 / u1 - 1, 1 / u2 - 1) / ((u1**2) * (u2**2))
    return Integral / Nsim


# Justificacion 01
"""
Por la Ley Fuerte de los grandes números, podemos considerar
una sucesión de N variables aleatorias uniformes Ui ~ Uniforme(0,1), independientes
y así aproximar el valor de la integral por el límite de promedios de evaluar la función
en los distintos puntos aleatorios generados
"""


# Justificacion ab
"""
Para estimar el valor de la integral sobre el intervalo (a, b),
se aplica un cambio de variables para transformarla en una
integral entre 0 y 1.

El cambio que se realiza es:
y  = (x-a)/(b-a)
dy = (1/(b-a))

# Luego de estimar la integral usando el método de Monte Carlo
# , al valor final se lo múltiplica por (b-a)
"""

# Justificacion 0inf
"""
Para estimar el valor de la integral sobre el intervalo (0, inf)
se aplica un cambio de variables, transformando biyectivamente 
el intervalo (0, inf) en (0,1) utilizando el siguiente cambio de variables

y  = 1/(x+1)
dy = -1/(x+1)**2 = -y**2
"""

## === Varias variables ==
# Justificación 01, 01
"""
Similar al caso 01 de una sola variable, por 
la Ley Fuerte de los grandes números, podemos considerar
una sucesión de N pares de variables aleatorias uniformes
Ui ~ Uniforme(0,1), independientes
y así aproximar el valor de la integral 
por el límite de promedios de evaluar la función g(u1, u2)
en los distintos puntos aleatorios generados
"""

# Justificación ab, ab
"""
Para estimar el valor de la integrales sobre 
los intervalos (a, b), (c, d)
aplicamos un cambio de variables a cada intervalo
para transformarlos en una
integral doble entre 0 y 1 para ambas.

Sea `x` la variable de la primera integral e 
`y` la de la segunda,
los cambios que se realizan son:
z  = (x-a)/(b-a)
dz = 1/(b-a)

w  = (y-c)/(d-c)
dw = 1/(d-c)
"""

# Justificación 0inf, 0inf
"""
Para estimar el valor de la integral doble
sobre los intervalos (0, inf), (0, inf)
se aplica un cambio de variables, transformando biyectivamente 
cada intervalo (0, inf) en (0,1) utilizando el siguiente cambio de variables

Sea `x` la variable de la primera integral e 
`y` la de la segunda,
los cambios que se realizan son:
z  =  1/(x+1)
dz = -1/(x+1)**2 = -z**2

w  =  1/(y+1)
dw = -1/(y+1)**2 = -w**2
"""


### Ejemplos de ejercicios
def fun_4a(u):
    return u / (u - np.exp(u))


def ej4a():
    # valor real = 1.10303
    """
    Para estimar el valor de la integral sobre el intervalo (a, b),
    se aplica un cambio de variables para transformarla en una
    integral entre 0 y 1.

    El cambio que se realiza es:
    y  = (x-a)/(b-a)
    dy = (1/(b-a))

    Luego de realizar la integral, al valor final se lo múltiplica por (b-a)
    """
    result_list = []
    for i in [1000, 10000, 100000, 1000000]:
        sum = MonteCarlo_ab(fun_4a, -3, 3, i)
        result_list.append((i, sum))

    return result_list
