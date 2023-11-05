import functions

while True:
    user_action = input("add, delete, show, edit or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'
        todos = functions.get_todos()
        todos.append(todo)
        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()
        # list comprehension new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos):  # (new_todos)
            item = item.strip('\n')
            item = item.title()
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo item: ")

            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Invalid input, try again like edit # from list...")
            continue

    elif user_action.startswith('delete'):
        try:
            no = int(user_action[7:])

            todos = functions.get_todos()

            index = no - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"The todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("Item number not present in list")
            todos = functions.get_todos()
            for index, item in enumerate(todos):
                index = index + 1
            print(f"Current list has {index} items")
            continue
        except ValueError:
            print("Enter list item number to delete and not list value...")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Option not valid, type add delete show edit or exit")

print("bye..")
