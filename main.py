from shop import Shop

from utils import read_valid_int


def print_menu():
    print("0. exit")
    print("1. add product")
    print("2. list products")
    print("3. update product")
    print("4. delete product")
    print("5. add category")
    print("6. list categories")
    print("7. update category")
    print("8. delete category")
    print("9. delete all products")
    print("10. delete all categories")


def interpret_command(command_):
    if command_ == 1:
        shop.add_product_from_key()
    elif command_ == 2:
        shop.show_products()
    elif command_ == 3:
        shop.update_product()
    elif command_ == 4:
        shop.delete_product()
    elif command_ == 5:
        shop.add_category_from_key()
    elif command_ == 6:
        shop.show_categories()
    elif command_ == 7:
        shop.update_category()
    elif command_ == 8:
        shop.delete_category()
    elif command_ == 9:
        shop.delete_all_products()
    elif command_ == 10:
        shop.delete_all_categories()


shop = Shop()
print_menu()
command = read_valid_int("Introduceti comanda: ")
interpret_command(command)

while command != 0:
    print_menu()
    command = read_valid_int("Introduceti comanda: ")
    interpret_command(command)
