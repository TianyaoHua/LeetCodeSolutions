from sympy import *
from scipy.optimize import fsolve
def func(x1):
    return x1**2*(2-x1)**2+x1**2*(1-x1)**2-(2-x1)**2*(1-x1)**2

r = fsolve(func,0)
print(r)