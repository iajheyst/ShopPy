import pickle


def save_object(filename, object_):
    with open(filename, 'wb') as handle:
        pickle.dump(object_, handle, protocol=pickle.HIGHEST_PROTOCOL)


def load_object(filename):
    with open(filename, 'rb') as handle:
        b = pickle.load(handle)
        return b


if __name__ == '__main__':
    a = {'hello': 'world'}
    save_object('filename.pickle', a)
    b = load_object('filename.pickle')
    print(a == b)
