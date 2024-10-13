import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="enter todo")

"""Window contailns layout of the gui. Below there are 2 layout options"""
#window = sg.Window('My To-Do App', layout=[[label, input_box]])

add_button = sg.Button("Add")

window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]])



window.read()
window.close()