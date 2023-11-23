def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
        else:
            return value
