import pickle

a = {'hello': 'world'}

with open('filename.pickle', 'wb') as handle:
    pickle.dump(a, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('filename.pickle', 'rb') as handle:
    b = pickle.load(handle)

print(a == b)


class Categorie:
    nume = ""
    poza = ""

    def __init__(self, nume, poza):
        self.nume = nume

class Produs:
    titlu = ""
    pret = 0
    descriere = ""

    def __init__(self, titlu, pret, descriere):
        self.titlu = titlu
        self.titlu = titlu
        self.titlu = titlu
