import PySimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window("TO-DO App", layout=[[label], [input_box, add_button]])

window.read()
window.close()
