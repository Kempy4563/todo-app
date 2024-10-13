# use default parameter for filepath
def get_todos(filepath='files/todos.txt'):
    """ Read a text file and return the list of
    to-do items. Uses a default filepath to store the to do text file.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath='files/todos.txt'):
    with open(filepath, 'w') as file_local:
        # use local scope vars for better code
        file_local.writelines(todos_arg)


