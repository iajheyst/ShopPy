import os

from categorie import Categorie
from pickle_library import load_object, save_object
from produs import Produs
from utils import *


class Shop:

    def __init__(self):
        self.products = load_object('produse.pickle')
        self.categories = load_object('categories.pickle')
        self.users = load_object('users.pickle')

    def next_id(self, filename):
        if os.path.exists(filename):
            id = load_object(filename)
            id += 1
            save_object(filename, id)
        else:
            id = 1
            save_object(filename, id)
        return id

    def save(self):
        save_object('produse.pickle', self.products)
        save_object('categories.pickle', self.categories)
        save_object('users.pickle', self.users)

    def add_product(self, product):
        product.id = self.next_id("product_id.pickle")
        self.products.append(product)
        self.save()

    def add_category(self, categ):
        categ.id = self.next_id("category_id.pickle")
        self.categories.append(categ)
        self.save()

    def add_user(self, user):
        self.users.append(user)
        self.save()

    def add_product_from_key(self):
        titlu = input("titlu=")
        pret = read_valid_float("pret=")
        descriere = input("descriere=")
        produs = Produs(titlu, pret, descriere)
        self.add_product(produs)

    def add_category_from_key(self):
        name = input("name=")
        poza = input("poza=")
        categ = Categorie(name, poza)
        self.add_category(categ)

    def update_category(self):
        counter = 1
        for categ in self.categories:
            print(f"{counter}. {categ.nume}")
            counter = counter + 1
        number = read_interval_valid_int("Select category to modify: \n", 1, counter - 1)
        position = number - 1
        categ = self.categories[position]
        categ.nume = input("name=")
        categ.poza = input("poza=")
        self.save()

    def update_product(self):
        counter = 1
        for product in self.products:
            print(f"{counter}. {product.titlu}")
            counter = counter + 1
        number = read_interval_valid_int("Select product to modify: \n", 1, counter - 1)
        position = number - 1
        product = self.products[position]
        product.titlu = input("titlu=")
        product.pret = read_valid_float("pret=")
        product.descriere = input("descriere=")
        self.save()

    def delete_product(self):
        counter = 1
        for product in self.products:
            print(f"{counter}. {product.titlu}")
            counter = counter + 1
        number = read_interval_valid_int("Select product to delete: \n", 1, counter - 1)
        position = number - 1
        self.products.pop(position)
        self.save()

    def delete_category(self):
        counter = 1
        for categ in self.categories:
            print(f"{counter}. {categ.nume}")
            counter = counter + 1
        number = read_interval_valid_int("Select category to delete: \n", 1, counter - 1)
        position = number - 1
        self.categories.pop(position)
        self.save()

    def show_products(self):
        counter = 1
        for product in self.products:
            print(f"{counter}. {product.titlu}")
            counter = counter + 1

    def show_categories(self):
        counter = 1
        for categ in self.categories:
            print(f"{counter}. {categ.nume}")
            counter = counter + 1

    def delete_all_products(self):
        self.products = []
        self.save()

    def delete_all_categories(self):
        self.categories = []
        self.save()
