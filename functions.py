FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Reads the todos text file and returns the
    items back to the calling client
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Writes the to-do new list back to the text file """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters
