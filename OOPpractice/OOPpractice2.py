class Snack:
    types = {}#keys=kind, values=amount
    def __init__(self, amount, kind):
        self.amount = amount
        self.kind = kind.lower()

        if self.kind not in Snack.types.keys():
            Snack.types[self.kind] = self.amount
        else:
            Snack.types[self.kind] += self.amount

    @classmethod
    def types_of(cls):
        lista = []
        for key in cls.types.keys():
            lista.append(key)
        return lista

    @classmethod
    def number_of(cls):
        for key, value in cls.types.items():
            print("There are {} {}".format(value, key))

lays = Snack(10, "chips")
pringles = Snack(7, "Chips")
coxinha = Snack(16, "coxinhas")
doritos = Snack(9, "doritos")

print(Snack.types_of())
print(Snack.number_of())