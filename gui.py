import functions
import PySimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button("Add")
add_button2 = sg.Button("Show")

window = sg.Window("TO-DO App",
                   layout=[[label], [input_box, add_button], [add_button2]],
                   font=('Acme', 15))

while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = value['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)

        case "Show":
            todos = functions.get_todos()
            print(value)

        case sg.WIN_CLOSED:
            break
window.close()
