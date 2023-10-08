# function definition
def printme(str: str = "default value"):
    """
    Args:
        str (str, optional): _description_. Defaults to "default value".
    Returns:
        None
    """
    print(str)
    return


a = printme("I'm first call to user defined function!")
print(a)
printme("Again second call to the same function")
