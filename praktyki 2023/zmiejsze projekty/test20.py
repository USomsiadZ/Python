import PySimpleGUI as sg
layout = [ [sg.Text('My Window')],
 [sg.Input(key='-IN-')],
 [sg.Text(size=(20,1), key='-OUT-')],
 [sg.Button('Go'), sg.Button('Exit')] ]
window = sg.Window('Window Title', layout)
while True: # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
       break
    if event == 'Go':
        window['-OUT-'].update(values['-IN-'])

