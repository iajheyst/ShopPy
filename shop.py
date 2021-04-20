from pickle_library import load_object, save_object
from produs import Produs
import utils


class Shop:
    # products = []
    # categories = []
    # users = []

    def __init__(self):
        self.products = load_object('produse.pickle')
        self.categories = load_object('categories.pickle')
        self.users = load_object('users.pickle')

    def save(self):
        save_object('produse.pickle', self.products)
        save_object('categories.pickle', self.categories)
        save_object('users.pickle', self.users)

    def add_product(self, product):
        self.products.append(product)
        self.save()

    def add_category(self, categ):
        self.categories.append(categ)
        self.save()

    def add_user(self, user):
        self.users.append(user)
        self.save()

    def add_product_from_key(self):
        titlu = input("titlu=")
        pret = utils.read_valid_float("pret=")
        descriere = input("descriere=")
        produs = Produs(titlu, pret, descriere)
        self.add_product(produs)
