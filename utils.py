def read_valid_float(user_prompt):
    try:
        number = float(input(user_prompt))
    except ValueError:
        print("Va rugam introduceti un float valid.")
        number = read_valid_float(user_prompt)

    return number


def read_valid_int(user_prompt):
    try:
        number = int(input(user_prompt))
    except ValueError:
        print("Va rugam introduceti un intreg valid.")
        number = read_valid_int(user_prompt)

    return number
