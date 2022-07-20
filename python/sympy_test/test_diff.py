import sympy as sp
from math import pi
from sympy.stats import Normal,P

x = sp.symbols('x', positive=True)
u = (sp.log(x/100) + (0.01 + 0.5*0.11**2)*0.5)/(0.11*sp.sqrt(0.5))
N = Normal('N',0,1)
f = sp.simplify(P(N <= u))
print(f.evalf(subs={x:100})) # This should be 0.5155
f1 = sp.simplify(sp.diff(f,x))
print(f1.evalf(subs={x:100})) # This should also return a float value
