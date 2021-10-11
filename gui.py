import sys
import PySimpleGUI as sg
import yaml

def run_gui(a_text):
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text('Text from config.yaml: {}'.format(a_text))],
                [sg.Text('Enter something on Row 2'), sg.InputText()],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Window Title', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        print('You entered ', values[0])

    window.close()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        path_yaml = sys.argv[1]
        with open(path_yaml) as file:
            a_text = yaml.load(file, Loader=yaml.FullLoader)['a_text']
    else:
        a_text = "default-text"
    run_gui(a_text)