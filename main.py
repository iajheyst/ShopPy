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

shop = Shop()

print(shop.products)
