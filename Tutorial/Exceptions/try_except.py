def get_int(prompt):
    return int(input(prompt))


get_int("Please enter an integer: ")


def get_int(prompt):
    try:
        value = int(input(prompt))
        return value
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return False


a = get_int("Please enter an integer: ")
print(a)


def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
        else:
            return value


get_int("Please enter an integer: ")
