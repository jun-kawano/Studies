# user input block (w, x, y, z, a11, a12, a13, a14, a15, a21, a22, a23, a24, a25)

userInput = "arrozarroz"
BAcheckBox = False #BAcheckBox == False => unencoding| BAcheckBox == True => encoding
# B * A = C
# B**(-1) * C = A
# a11    a12    a13    a14    a15
# a21    a22    a23    a24    a25
# w    x
# y    z
#
# p    q
# r    s

def splitter(word):
    a11 = word[0]
    a12 = word[1]
    a13 = word[2]
    a14 = word[3]
    a15 = word[4]
    a21 = word[5]
    a22 = word[6]
    a23 = word[7]
    a24 = word[8]
    a25 = word[9]
    return a11, a12, a13, a14, a15, a21, a22, a23, a24, a25
result = splitter(userInput)
#dictionary
tabela = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9, "k":10, "l":11, "m":12, "n":13, "o":14, "p":15, "q":16, "r":17, "s":18, "t":19, "u":20, "v":21, 
"w":22, "x":23, "y":24, "z":25, "1":26, "2":27, "3":28, "4":29, "5":30, "6":31, "7":32, "8":33, "9":34, "0":35, " ":36}

a11, a12, a13, a14, a15, a21, a22, a23, a24, a25 = result
lista = [a11, a12,a13,a14,a15,a21,a22,a23,a24,a25]
ramen = []

for variable in lista:
    if variable in tabela.keys():
        variable = tabela[variable]
        ramen.append(variable)

def product(b1, b2, c1, c2):
    a = b1 * c1 + b2 * c2
    return a

detB = (w * z - x * y)
"""
    #p = z / (w * z - x * y)
    #q = -x / (w * z - x * y)
    #r = -y / (w * z - x * y)
    #s = w / (w * z - x * y)
"""

if w * z - (x * y) == 0:
    print("B element is invalid")
elif BAcheckBox == True:
    c11 = a11
    c12 = a12
    c13 = a13
    c14 = a14
    c15 = a15
    c21 = a21
    c22 = a22
    c23 = a23
    c24 = a24
    c25 = a25

    p = z / detB
    q = -x / detB
    r = -y / detB
    s = w / detB

    a1 = product(p, q, c11, c21)
    a2 = product(p, q, c12, c22)
    a3 = product(p, q, c13, c23)
    a4 = product(p, q, c14, c24)
    a5 = product(p, q, c15, c25)
    a6 = product(r, s, c11, c21)
    a7 = product(r, s, c12, c22)
    a8 = product(r, s, c13, c23)
    a9 = product(r, s, c14, c24)
    a10 = product(r, s, c15, c25)
    print(str(a1) +"    "+ str(a2) + "    " + str(a3) +"    "+ str(a4) +"    "+ str(a5))
    print(str(a6) +"    "+ str(a7) + "    " + str(a8) +"    "+ str(a9) +"    "+ str(a10))
else:

    a1 = product(w, x, a11, a21)
    a2 = product(w, x, a12, a22)
    a3 = product(w, x, a13, a23)
    a4 = product(w, x, a14, a24)
    a5 = product(w, x, a15, a25)
    a6 = product(y, z, a11, a21)
    a7 = product(y, z, a12, a22)
    a8 = product(y, z, a13, a23)
    a9 = product(y, z, a14, a24)
    a10 = product(y, z, a15, a25)
    print(str(a1) +"    "+ str(a2) + "    " + str(a3) +"    "+ str(a4) +"    "+ str(a5))
    print(str(a6) +"    "+ str(a7) + "    " + str(a8) +"    "+ str(a9) +"    "+ str(a10))
