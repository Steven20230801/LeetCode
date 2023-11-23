# function without argument
def printme():
    print("I'm first call to user defined function!")


printme()


# function with argument
def printme(str: str):
    """
    Args:
        str (str, optional): _description_. Defaults to "default value".
    Returns:
        None
    """
    print(str)
    return str


a = printme("I'm second call to user defined function!")
printme("Again second call to the same function")


# function with default argument value
def printinfo(name, age=35):
    """
    Args:
        name ([type]): [description]
        age (int, optional): [description]. Defaults to 35.
    """
    print("Name: ", name)
    print("Age ", age)
    return


def example_function(*args, **kwargs):
    """
    Function that demonstrates the use of *args and **kwargs.
    *args collects positional arguments, while **kwargs collects named keyword arguments.
    """

    # Handling args
    print("Positional arguments (args):")
    for arg in args:
        print("-", arg)

    # Handling kwargs
    print("\nKeyword arguments (kwargs):")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Example usage of the function
example_function(1, 2, 3, first_name="Alice", last_name="Smith")


def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
        else:
            return value
