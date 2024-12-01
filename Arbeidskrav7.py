import sympy as sp
import numpy as np

x, y, z, t = sp.symbols('x y z t')

def div(F_):
    f1 = sp.diff(F_[0], 'x')
    f2 = sp.diff(F_[1], 'y')
    f3 = sp.diff(F_[2], 'z')

    return f1 + f2 + f3

def curl(F_):

    # i
    f1 = sp.diff(F_[2], 'y')
    f2 = sp.diff(F_[1], 'z')
    i = f1.copy() - f2.copy()

    # j
    f1 = sp.diff(F_[2], 'x')
    f2 = sp.diff(F_[0], 'z')
    j = f1.copy() - f2.copy()

    # k
    f1 = sp.diff(F_[1], 'x')
    f2 = sp.diff(F_[0], 'y')
    k = f1.copy() - f2.copy()

    return i - j + k

def phi(F_):
    int1 = F_[0].integrate(x)

    f2 = sp.diff(int1, 'y')

    if F_[1]-f2 != 0:
        pass

    f3 = sp.diff(int1, 'z')

    if F_[2]-f3 != 0:
        pass

    return int1

def task1():
    F1 = -2*(3*y-6*z)*sp.exp(3*x*y-6*x*z)-7*y*z
    F2 = -6*x*sp.exp(3*x*y-6*x*z)-7*x*z
    F3 = 12*x*sp.exp(3*x*y-6*x*z)-7*x*y

    F = np.array([F1, F2, F3])

    print(curl(F.copy()).simplify())

    print(phi(F.copy()))

def task4():
    dS = 120*sp.sin(t)**2*sp.cos(t)**4
    print(dS)

    int = sp.integrate(dS, (t, 0, 2*sp.pi))
    print(int)

    results = int.evalf()

task4()