# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 19:03:45 2019

@author: Prateek Chandra Jha

Roll Number -> MDS-2019-22
"""

from sympy import *
import numpy as np
import matplotlib


#Question Number 1 - Graphing of a few functions - The plots are not attached, ONLY CODE BELOW

# Plotting Sine Function
ques1_x_range = np.arange(math.radians(-270), math.radians(270) , math.radians(0.01))
ques1_y_range = np.sin(ques1_x_range)
plt.plot(ques1_x_range, ques1_y_range)

# Plotting Tan Function
ques2_x_range = np.linspace(0, 4*np.pi, 650)
ques2_y_range = np.tan(ques2_x_range)
plt.plot(ques2_x_range, ques2_y_range)
plt.ylim(-3,3)

# Plotting Hyperbolic Cosine Function
ques3_x_range = np.linspace(-15, 15, 1000)
ques3_y_range = np.cosh(ques3_x_range)
plt.plot(ques3_x_range, ques3_y_range)

# Plotting the Bell Shaped Function
ques4_x_range = np.linspace(-10, 10, 1000)
ques4_y_range = np.exp(-(ques4_x_range**2))
plt.plot(ques4_x_range, ques4_y_range)


# Question Number 2 - Graphing a function f(x)

ques2_x_range_2 = np.arange(-15, 15 , 0.01)
ques2_y_range_2 = (ques2_x_range_2)**3 - 4*(ques2_x_range_2**2) + 1
plt.plot(ques2_x_range_2, ques2_y_range_2)

""" This is the case of (Casus irredicibilis). Let f(X) be an irreducible polynomial having 3 real zeros
and coefficients in a real number field K. Then f(X) is not solvable by real radicals over the
field K. We discussed this in class and the issue was resolved by an experienced 
programmer (I'm attaching the solution offered by him) - https://stackoverflow.com/questions/58462975/sympy-solveset-showing-imaginary-solutions
"""

x = Symbol('x')
[i.n(2, chop=True) for i in solve(x**3 - 4*(x**2) + 1)]
# The above gives all the 3 real roots as [0.54, -0.47, 3.9]

j = Symbol('j') 
y = j**3 - 4*(j**2) + 1
yprime = y.diff(j)

solveset(yprime,j)
# f(x) has a relative maxima/minima at 0 and 8/3

solveset(yprime>0,j,S.Reals)
pprint(solveset(yprime>0,j,S.Reals))
# f(x) is increasing in the interval (-∞, 0) ∪ (8/3, ∞)

solveset(yprime<0,j,S.Reals)
pprint(solveset(yprime>0,j,S.Reals))
# f(x) is decreasing in the interval (0, 8/3)


# Question Number 3 - Calculation of Limits

x = Symbol('x')
ques1_3 = (x**2+3*x-4)/(x-1)
limit(ques1_3,x,1)

# The answer is 5

ques2_3 = sin(x)/x
limit(ques2_3,x,0)

# The answer is 1

ques3_3 = x * ln(x)
limit(ques3_3,x,0)

# The answer is 0



# Question Number 4 - Differentiation



ques1_4 = (x**2+5*x-1)**100
ques1_4_prime = ques1_4.diff(x)

# The answer in LaTeX is \left(200 x + 500\right) \left(x^{2} + 5 x - 1\right)^{99}

ques2_4 = ((x**2 * sympy.exp(x))-1)/(x**2+2)
ques2_4_prime = ques2_4.diff(x)

""" The answer in LaTeX is - \frac{2 x \left(x^{2} e^{x} - 1\right)}{\left(x^{2} + 2\right)^{2}} + \frac{
x^{2} e^{x} + 2 x e^{x}}{x^{2} + 2} """

ques3_4 = ((sin(x))**5 * (cos(x))**3)
ques3_4_prime = ques3_4.diff(x)

""" The answer in LaTeX is - 3 \sin^{6}{\left(x \right)} \cos^{2}{\left(x \right)} + 5 \sin^{4}{\left(x \
right)} \cos^{4}{\left(x \right)} """

ques4_4 = (atan(sympy.exp(x)))
ques4_4_prime = ques4_4.diff(x)

""" The answer in LaTeX is \frac{e^{x}}{e^{2 x} + 1} """



# Question Number 5 - Integration


init_printing(use_unicode=False, wrap_line=False)
x = Symbol('x')

ques1 = integrate(((x**2 + 5*x - 1)**10)*(2*x+5), x)

""" The answer in LaTeX is \frac{x^{22}}{11} + 5 x^{21} + 124 x^{20} + 1825 x^{19} + 17630 x^{18} + 11647
5 x^{17} + 529485 x^{16} + 1608150 x^{15} + 2961405 x^{14} + 2255425 x^{13} - 
1890542 x^{12} - \frac{38773235 x^{11}}{11} + 1890542 x^{10} + 2255425 x^{9} -
 2961405 x^{8} + 1608150 x^{7} - 529485 x^{6} + 116475 x^{5} - 17630 x^{4} + 1
825 x^{3} - 124 x^{2} + 5 x """

ques2 = integrate((x**5)*((1-x**2)**(3/2)), (x,0,1))

# The answer is ￼￼0.0253968253968254

ques3 = integrate(sin(x**3), (x,0,1))

""" The answer in LaTeX is \frac{\Gamma\left(\frac{2}{3}\right) {{}_{1}F_{2}\left(\begin{matrix} \frac{2}{3} \\ \frac{3}{2}, \frac{5}{3} \end{matrix}\middle| {- \frac{1}{4}} \right)}}{6 \Gamma\left(\frac{5}{3}\right)} """

""" gamma(2/3)*hyper((2/3,), (3/2, 5/3), -1/4)/(6*gamma(5/3)) """

