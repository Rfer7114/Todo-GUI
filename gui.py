import functions
import PySimpleGUI as sg

label = sg.Text("Type in a To-Do")

input_box = sg.InputText(tooltip="Enter todo", key='item')

add_button = sg.Button("Add")

window = sg.Window("TO-DO App", layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 13))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['item'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)

        case sg.WIN_CLOSED:
            break

window.close()
