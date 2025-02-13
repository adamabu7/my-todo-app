FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH): #filepath="files/subfiles/todos.txt"    #filepath here is known as the parameter of the function, then skip to line 15, when you call the function, this is known as the argument value
    #having filepath above is the same as doing... filepath = "todos.txt"
    """ Read a text file and return the list of
    to-do items
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):           #filepath and todos_arg are both parameters as well
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

# print(__name__)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())