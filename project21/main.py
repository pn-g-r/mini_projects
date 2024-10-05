import FreeSimpleGUI as sg

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Function to write input temperature and conversion result to a file
def write_file(input_text):
    with open('project21/file.txt', 'a') as file:
        file.write(input_text + '\n')

# Define the layout of the window
layout = [
    [sg.Text("Temperature Converter", font=("Helvetica", 16))],
    [sg.Text("Enter Temperature: "), sg.InputText(key="input_temp")],
    [sg.Radio('Celsius to Fahrenheit', "RADIO1", default=True, key="C_to_F"),
     sg.Radio('Fahrenheit to Celsius', "RADIO1", key="F_to_C")],
    [sg.Button("Convert"), sg.Button("Exit")],
    [sg.Text("Converted Temperature: "), sg.Text("", key="output_temp", size=(20, 1))],
]

# Create the window
window = sg.Window("Temperature Converter", layout)

# Event loop to process user inputs
while True:
    event, values = window.read()
    print(values)

    # If user closes window or clicks Exit
    if event == sg.WIN_CLOSED or event == "Exit":
        break

    # If user clicks Convert
    if event == "Convert":
        try:
            input_temp = float(values["input_temp"])  # Get the input temperature
            # Check which conversion to apply
            if values["C_to_F"]:
                converted_temp = celsius_to_fahrenheit(input_temp)
                result_text = f"{input_temp} °C = {converted_temp:.2f} °F"
                window["output_temp"].update(f"{converted_temp:.2f} °F")
            elif values["F_to_C"]:
                converted_temp = fahrenheit_to_celsius(input_temp)
                result_text = f"{input_temp} °F = {converted_temp:.2f} °C"
                window["output_temp"].update(f"{converted_temp:.2f} °C")
            write_file(result_text)
        except ValueError:
            window["output_temp"].update("Invalid input!")

# Close the window
window.close()
