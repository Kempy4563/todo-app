# NOTE: This script runs only on your local IDE

import FreeSimpleGUI as sg
conversion = float(0.0254)


feet_label = sg.Text("Enter feet: ")
feet_input = sg.Input(key="feet")

inches_label = sg.Text("Enter inches: ")
inches_input = sg.Input(key="inches")

button = sg.Button("Convert")
output_label = sg.Text("", key="output")

window = sg.Window("Convertor",
                   layout=[[feet_label, feet_input],
                           [inches_label, inches_input],
                           [button, output_label]])

while True:
    event, values = window.read()
    feet = float(values["feet"])
    inches = float(values["inches"])
    result_inches = feet * 12 + inches
    result = result_inches * conversion


    window["output"].update(value=f"{result} m", text_color="white")

window.close()
