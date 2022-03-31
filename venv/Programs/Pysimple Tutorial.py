import PySimpleGUI as sg

sg.theme("DarkAmber")

layout=[[sg.Text("Enter Name")],
        [sg.InputText(key='-Name-')],
        [sg.Text("Enter Radius")],
        [sg.InputText(key='-Radius-')],
        [sg.Submit(), sg.Cancel()],
]

window = sg.Window('First Window', layout)

event, values = window.read()

window.close()

sg.popup('You entered', values['-Name-'])