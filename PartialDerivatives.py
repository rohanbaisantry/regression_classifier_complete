
# program to calculate the partial derivatives
from numpy import sin
from sympy import symbols, diff
print(var[1])
def patial_derivative(f,var):
    var_str=""
    for i in len(var):
    	var_str+=str(var[i])+", "
    var_str.pop()
    var_str.pop()
    var_s = symbols(var_str,real=True)
    var_pdiff=list()
    for i in len(var):
    	var_pdiff.append(diff(f,str(var[i])))
    print(var_pdiff)

patial_derivative(f)
"""
x, y, z = symbols('x y z', real=True)

diff(f, x)

>> 4*y + sin(z) + 3*x**2

"""