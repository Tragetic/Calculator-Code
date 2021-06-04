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

original = 0
operation = '0'
change = 0
result = 0

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    print('You entered ', values[0])
    
#set original value
if original == 0:
  if event == '1':
    original = 1
  elif event == '2':
    original = 2
  elif event == '3':
    original = 3
  elif event == '4':
    original = 4
  elif event == '5':
    original = 5
  elif event == '6':
    original = 6
  elif event == '7':
    original = 7
  elif event == '8':
    original = 8
  elif event == '9':
    original = 9
  print(original)

#set operation
if original != 0 and operation == '0':
  if event == '-':
    operation = '-'
  elif event == '+':
    operation = '+'
  elif event == '*':
    operation = '*'
  elif event == '/':
    operation = '/'
  print(operation)

#set change
if original != 0 and operation != '0' and change == 0:
  if event == '1':
    change = 1
  elif event == '2':
    change = 2
  elif event == '3':
    change = 3
  elif event == '4':
    change = 4
  elif event == '5':
    change = 5
  elif event == '6':
    change = 6
  elif event == '7':
    change = 7
  elif event == '8':
    change = 8
  elif event == '9':
    change = 9
  print(change)



window.close()

"""
We want 1 variable that is result, and 1 variable that is change.
Then after change, it will check what operator, and then when they press enter it will output the result.
This will only work for single digit numbers, but at least it will work.

There will need to be multiple functions:
1. a while loop to close if the x is pressed
2. an if statement to set the orignial value
3. an if statement to select the operator
3. an if statement to select the change
4. a function to print the result
5. I will need to make the 1 textbox fit this all in
"""