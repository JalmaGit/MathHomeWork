import sympy as sp
import numpy as np


def task2a():
    x, y = sp.symbols('x y')

    z = 2*y**2 - 2*y + 2*x**2 - 22*x + 67

    z1 = sp.diff(z, x)
    z11 = sp.diff(z1, x)
    z12 = sp.diff(z1, y)

    z2 = sp.diff(z, y)
    z21 = sp.diff(z2, x)
    z22 = sp.diff(z2, y)

    print(f"{z11 = }, {z12 = }, {z21 = }, {z22 = }")

    print(round(np.linalg.det((np.array([[float(z11),float(z12)],[float(z21),float(z22)]]))),1))

task2a()
