# function without argument
def printme():
    print("I'm first call to user defined function!")


printme()


# function with argument
def printme(str: str = "default value"):
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
