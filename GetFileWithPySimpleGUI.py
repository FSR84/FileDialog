import PySimpleGUI as sg

# sg.theme('dark grey 9')

filename = sg.popup_get_file('Enter the file you wish to process')
sg.popup('You entered', filename)

# https://pypi.org/project/PySimpleGUI/
