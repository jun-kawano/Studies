import numpy as np

coef_inp = input("Enter the coefficients: ")
x = input("Enter the x value: ")
x = float(x)


coef_inp.split()
coef = []
for n in coef_inp:
    if n.isnumeric():
        coef.append(float(n))

print(np.polyval(coef, x))