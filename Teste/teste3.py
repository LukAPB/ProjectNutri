import PySimpleGUI as sg
import keyboard

def toggle_maximize(window):
    keyboard.press('F11')
    keyboard.release('F11')
    window.TKroot.focus_force()

layout = [[sg.Text('Hello, World!')],
          [sg.Button('Maximize', key='-MAXIMIZE-')]]
window = sg.Window('My Window', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == '-MAXIMIZE-':
        toggle_maximize(window)

window.close()
