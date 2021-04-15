class Produs:
    titlu = ""
    pret = 0
    descriere = ""
    categorie = None

    def __init__(self, titlu, pret, descriere, categorie=None):
        self.titlu = titlu
        self.pret = pret
        self.descriere = descriere
        self.categorie = categorie

    def __repr__(self):
        return f"{self.titlu}, {self.pret}"

    def __str__(self):
        return f"{self.titlu}, {self.pret}"