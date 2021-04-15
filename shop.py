from pickle_library import load_object


class Shop:
    # products = []
    # categories = []
    # users = []

    def __init__(self):
        self.products = load_object('produse.pickle')
        self.categories = load_object('categories.pickle')
        self.users = load_object('users.pickle')

