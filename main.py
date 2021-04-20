from shop import Shop

from utils import read_valid_int


def print_menu():
    print("0. exit")
    print("1. add product")
    print("2. list products")
    print("3. update product")


def interpret_command(command_):
    if command_ == 1:
        shop.add_product_from_key()
    elif command_ == 2:
        print(shop.products)
    elif command_ == 3:
        shop.update_product()


shop = Shop()
print_menu()
command = read_valid_int("Introduceti comanda: ")
interpret_command(command)

while command != 0:
    print_menu()
    command = read_valid_int("Introduceti comanda: ")
    interpret_command(command)
