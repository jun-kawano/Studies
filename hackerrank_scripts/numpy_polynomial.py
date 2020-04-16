import numpy as np

inp = input("Enter the coefficients: ").split()
inp2 = input("Enter the x value: ")

x = float(inp2)

coef = []
for n in inp:
    n = float(n)
    coef.append(float(n))

print(np.polyval(coef, x))