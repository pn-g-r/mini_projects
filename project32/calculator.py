import FreeSimpleGUI as sg

# Define the layout of the calculator
layout = [
    [sg.Text('', size=(20, 1), justification='right', font=('Arial', 18), background_color='white', text_color='black', key='DISPLAY', expand_x=True, expand_y=True)],
    [sg.Button('7', expand_x=True, expand_y=True), sg.Button('8', expand_x=True, expand_y=True), sg.Button('9', expand_x=True, expand_y=True), sg.Button('/', expand_x=True, expand_y=True)],
    [sg.Button('4', expand_x=True, expand_y=True), sg.Button('5', expand_x=True, expand_y=True), sg.Button('6', expand_x=True, expand_y=True), sg.Button('*', expand_x=True, expand_y=True)],
    [sg.Button('1', expand_x=True, expand_y=True), sg.Button('2', expand_x=True, expand_y=True), sg.Button('3', expand_x=True, expand_y=True), sg.Button('-', expand_x=True, expand_y=True)],
    [sg.Button('0', expand_x=True, expand_y=True), sg.Button('.', expand_x=True, expand_y=True), sg.Button('+', expand_x=True, expand_y=True), sg.Button('=', expand_x=True, expand_y=True)],
    [sg.Button('Clear', expand_x=True, expand_y=True)]
]

# Create the window with resizable layout
window = sg.Window('Simple Calculator', layout, resizable=True, finalize=True)

# Initial window size
window.size = (300, 400)

# Initial display text and current number
display_text = ''
current_number = ''

# Calculator logic
while True:
    event, values = window.read()

    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break

    if event in '0123456789.':
        print(event)
        # Append number or decimal point to the current number
        current_number += event
        display_text += event
        window['DISPLAY'].update(display_text)
    
    if event in '+-*/':
        # Operator entered, append operator and reset current_number
        if current_number:
            display_text += event
            current_number = ''
            window['DISPLAY'].update(display_text)

    if event == '=':
        # Try to evaluate the expression when '=' is pressed
        try:
            result = str(eval(display_text))
            window['DISPLAY'].update(result)
            display_text = result
        except Exception as e:
            window['DISPLAY'].update('Error')
            display_text = ''
            current_number = ''

    if event == 'Clear':
        # Clear the display and reset variables
        display_text = ''
        current_number = ''
        window['DISPLAY'].update('')

# Close the window
window.close()
