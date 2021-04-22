class Produs:
    id = 0
    titlu = ""
    pret = 0
    descriere = ""
    categorie = None

    def __init__(self, titlu, pret, descriere, categorie=None, id=0):
        self.id = id
        self.titlu = titlu
        self.pret = pret
        self.descriere = descriere
        self.categorie = categorie

    def __repr__(self):
        return f"{self.id}, {self.titlu}, {self.pret}"

    def __str__(self):
        return f"{self.id}, {self.titlu}, {self.pret}"
