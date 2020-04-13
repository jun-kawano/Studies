import numpy as np
#user input --> outputs a word (word)
word = input("word")

#transform to numbers
tabela = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9, "k":10, "l":11, "m":12, "n":13, "o":14, "p":15, "q":16, "r":17, "s":18, "t":19, "u":20, "v":21, 
"w":22, "x":23, "y":24, "z":25, "1":26, "2":27, "3":28, "4":29, "5":30, "6":31, "7":32, "8":33, "9":34, "0":35, " ":36}

lista = []
i1 = [] #row1
i2 = [] #row2
j = [] #columns

for letter in word:
    if letter in tabela.keys():
        lista.append(tabela[letter])
if len(word) % 2 == 1:
    index = len(word) + 1
else:
    index = len(word)

#word matrix
i1 = lista[:index // 2]
i2 = lista[index //2:]
m1 = np.array([i1, i2])

#encoding matrix
m2 = np.array([[2, 3], [1, 2]])

print(m1)
print(m2)
result = m2.dot(m1) #matrix multiplication
print(result)

