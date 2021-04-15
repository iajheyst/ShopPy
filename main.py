from pprint import pprint

from pickle_library import *
from produs import Produs
from shop import Shop
from user import User


# acer = Produs("Laptop acer 15.6'", 400, "Office")
#
# print(acer.pret)
#
# ionut=User("Ionut", "adresa x", "blahblah", "ionut@gmail.com")
#
# print(ionut.adresa)

# lista = []
# lista.append(Produs("Acer", 100, "descriere 1"))
# lista.append(Produs("Asus", 200, "descriere 2"))
# lista.append(Produs("Dell", 150, "descriere 3"))
#
# save_object('produse.pickle', lista)
# save_object('categories.pickle', [])
# save_object('users.pickle', [])

# shop = Shop()
# #citire de la tastatura produs?
# #plus da
# #shop.add_product_from_key()
# pprint(shop.products)
# print(shop.products)

def print_menu():
    print("0. exit")
    print("1. add product")
    print("2. list products")

def interpret_command(command):
    if command == "1":
        shop.add_product_from_key()
    elif command == "2":
        print(shop.products)

shop = Shop()
print_menu()
command = input("Introduceti comanda: ")
interpret_command(command)

while command != '0':
    print_menu()
    command = input("Introduceti comanda: ")
    interpret_command(command)


