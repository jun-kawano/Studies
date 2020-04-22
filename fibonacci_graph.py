import matplotlib.pyplot as plt

r = range(-40, 40)

sqr5 = 5 ** (1/2)

def fib(n):
    result = (1/sqr5)*(((1+sqr5)/2)**n - ((1-sqr5)/2)**n)
    return result

x = []
y = []
for n in r:
    x.append(n)

for n in x:
    y.append(fib(n))

plt.axis([-50, 50, -100, 100])#graph scale
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()

print(x)
print(y)