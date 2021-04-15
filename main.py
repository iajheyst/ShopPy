from pickle_library import *
from produs import Produs
from user import User

# acer = Produs("Laptop acer 15.6'", 400, "Office")
#
# print(acer.pret)
#
# ionut=User("Ionut", "adresa x", "blahblah", "ionut@gmail.com")
#
# print(ionut.adresa)

save_object('filename.pickle', ['Hello', "world"])
print(load_object('filename.pickle'))
