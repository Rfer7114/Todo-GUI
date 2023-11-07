import functions
import PySimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter todo", key='item')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), enable_events=True, key='list', size=(45, 10))
edit_button = sg.Button("Edit")

window = sg.Window("TO-DO App", layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=('Helvetica', 13))

while True:
    event, values = window.read()
    print(1, "EVENT:", event)
    print(2, "VALUES:", values)

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['item'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)

            window['list'].update(values=todos)

        case "Edit":
            todo_to_edit = values['list'][0]
            new_todo = values['item']

            todo_list = functions.get_todos()
            index = todo_list.index(todo_to_edit)
            todo_list[index] = new_todo
            functions.write_todos(todo_list)

            window['list'].update(values=todo_list)

        case "list":
            window['item'].update(value=values['list'][0])

        case sg.WIN_CLOSED:
            break

window.close()
