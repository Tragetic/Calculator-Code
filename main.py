import PySimpleGUI as sg

layout = [
    [sg.InputText()],
    [
        sg.Button('CE', size=(5, 5)),
        sg.Button('Backspace', size=(8, 5)),
        sg.Button('Enter', size=(8, 5))
    ],
    [
        sg.Button('7', size=(5, 5)),
        sg.Button('8', size=(5, 5)),
        sg.Button('9', size=(5, 5)),
        sg.Button('/', size=(5, 5))
    ],
    [
        sg.Button('4', size=(5, 5)),
        sg.Button('5', size=(5, 5)),
        sg.Button('6', size=(5, 5)),
        sg.Button('*', size=(5, 5))
    ],
    [
        sg.Button('1', size=(5, 5)),
        sg.Button('2', size=(5, 5)),
        sg.Button('3', size=(5, 5)),
        sg.Button('-', size=(5, 5))
    ],
    [
        sg.Button('+/-', size=(5, 5)),
        sg.Button('0', size=(5, 5)),
        sg.Button('.', size=(5, 5)),
        sg.Button('+', size=(5, 5))
    ],
]

window = sg.Window('Py Calculator', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()

"""
I think to add functionality I will have to give each button a variablee, for example:
button1 = sg.Button('CE', size=(5, 5)),
and then to add functionality I think I will just write like:
num = 3
if button1:
  num = 0
something like that?
"""