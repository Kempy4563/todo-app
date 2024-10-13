import functions
import time


while True:

    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith('add'):

        # string slice and add a newline
        todo = (f"{user_action[4:]}" + "\n")

        todos = functions.get_todos()
        todos.append(todo)

        functions.write_todos(todos_arg=todos)

    elif user_action.startswith('show'):

        todos = functions.get_todos()

        # List comprehension to strip the new lines - need to add new_todos in enumerate
        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            # remove newline
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)

            todos = functions.get_todos()
            number = number - 1
            new_todo = input("Enter new todo: ") + "\n"
            todos[number] = new_todo

            functions.write_todos(todos_arg=todos)

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(number - 1)

            functions.write_todos(todos_arg=todos)
            message = f"Todo {todo_to_remove} has been removed from the list."
            print(message)

        except IndexError:
            print("There is no item with that number")
            continue
    elif 'exit' in user_action:
        break
    else:
        print("Command is not valid.")
print("Bye!")
