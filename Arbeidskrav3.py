import sympy as sp
import numpy as np


def task5c():
    # ____________________________________
    # TASK 5c
    # ____________________________________
    x, y, gxy = sp.symbols('x,y,gxy')

    gxy = y * sp.ln(y ** 2 + x ** 2)

    dg1 = sp.diff(gxy, x)
    dg12 = sp.diff(dg1, y)
    print(dg12)

    dg2 = sp.diff(gxy, y)
    dg21 = sp.diff(dg1, x)
    print(dg21)

    dg122 = sp.diff(dg12, y)
    dg1221 = sp.diff(dg122, x)

    print(dg1221)


def task6a():
    x, y, z = sp.symbols('x,y,z')

    z = x ** 2 * y ** 2 - 4 * y * x + 4

    z1 = sp.diff(z, x)
    z2 = sp.diff(z1, y)
    print(z2)
    x = -3
    y = -1
    z2 = 4 * x * y - 4
    print(z2)


def task8():
    x, y, z, T = sp.symbols('x,y,z,T')

    T = 10 * sp.exp(-x ** 2 - y ** 2 - z ** 2)

    T1 = sp.diff(T, x)
    T2 = sp.diff(T, y)
    T3 = sp.diff(T, z)

    print(f"{T1 = },\n{T2 = },\n{T3 = }")

    print("___________________________\n                       \n___________________________")

    results = {"T1": T1.subs({x: 2, y: -4, z: 4}),
               "T2": T2.subs({x: 2, y: -4, z: 4}),
               "T3": T3.subs({x: 2, y: -4, z: 4})
               }

    for key, val in results.items():
        print(f"{key}: {val}")

    print("___________________________\n                       \n___________________________")

    determinant = sp.sqrt(results["T1"] ** 2 + results["T2"] ** 2 + results["T3"] ** 2)

    print(f"{determinant = }")

    print("___________________________\n                       \n___________________________")

    directionResults = {"x": ((1 / determinant) * results["T1"]),
                        "y": ((1 / determinant) * results["T2"]),
                        "z": ((1 / determinant) * results["T3"])
                        }

    for key, val in directionResults.items():
        print(f"{key}: {val}")

    print("___________________________\n                       \n___________________________")

    gradientResults = (results["T1"] * directionResults["x"]) + (results["T2"] * directionResults["y"]) + (
                results["T3"] * directionResults["z"])

    print(f"{gradientResults = }")


def test():
    a = np.array([1, 2, 3, 4])

    print(a[2:])