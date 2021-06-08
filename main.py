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
Alright, I know it might not seem very impressive, but it does do something. 
The user can click a button to choose an input, then click another button to choose an operation.

Looking at the code now, especially the while true loop, it looks really simple, but it actually took me a long time to figure out how to get it to work, and it's because I just wasn't sure the exact notation. All the pysimplegui documentation was really basic, but then never really said how to go on to the next level, probably because I should've been looking through basic python docs instead, but I didn't know that.

So what the program does is you can select a number, 1 through 9, and then you can either press the + button to add it by itself, or press the * button to multiply it by itself. Then when you click the X it closes the window. I didn't make the - or / buttons functional, because the result for all of them would be 0 so there wouldn't really be a point.


I think to make it a real calculator, I would have to make it so that as long as you click integers, it stores them as a list. Then when you click an operator it starts a new list, then when you click enter it would have to convert both of those lists into integers, then do the operation, and then output the result.

But, it's 11:10pm on the 7th, tomorrow is my last day of high school ever, and I just now got a functional MVP. Honestly I'm just going to turn it in and call it good. 
It's not that I just did the visual parts at the beggining of may, then didn't do anything, then did some crunch time at the last moment, even though that's definantly what it looks like. I put in time regularly throughout may and the first week of june, its just that I tried lots of different things and none of them worked, because I didn't know how to do what I wanted to do.
Honestly I should've asked for help in like mid may, but I didn't. 
Because I would say to myself "ok jacob it's time to do some coding", then I would spend 2 hours googling how to get the buttons to do what I want them to, and then I would give up, and then 2 or 3 days later I would try again and I would really not want to bother. I thought my problem was procrastintion but looking back it was just that I didn't know where to go. It's completly my fault for not having a functioning calculator, because I should've asked for help.
"""