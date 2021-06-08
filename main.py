import PySimpleGUI as sg

layout = [
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
    elif event == '1':
      num = 1
    elif event == '2':
      num = 2
    elif event == '3':
      num = 3
    elif event == '3':
      num = 3
    elif event == '4':
      num = 4
    elif event == '5':
      num = 5
    elif event == '6':
      num = 6
    elif event == '7':
      num = 7
    elif event == '8':
      num = 8
    elif event == '9':
      num = 9
    elif event == '*':
      print(num * num)
    elif event == '+':
      print(num + num)
    

window.close()

"""
The code is simple, and the project is not what I wanted it to be, but it is at least an MVP, and it is functional.

The program lets you choose a number between 1 and 9, then you can either select "+" to recieve the output of that number added to itself, or select "*" to recieve the output of that number multiplied by itself. Then you can select the "X" to exit the program.

I think to make it a real calculator, I would have to make it so that as long as you click integers, it stores them as a list. Then when you click an operator it starts a new list, then when you click enter it would have to convert both of those lists into integers, then do the operation, and then output the result.
But it's the last day, and I just got my MVP, so I'm just going to turn it in.
"""