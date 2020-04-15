import numpy as np

inp = input().split()

x = float(inp[-1])
coef_inp = inp[0:len(inp)-1]

coef = []
for n in coef_inp:
    if n.isnumeric():
        coef.append(float(n))

print(np.polyval(coef, x))
