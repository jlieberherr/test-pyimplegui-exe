import sys
import PySimpleGUI as sg
import yaml

def run_gui(untis_file, inital_file_folder, initial_output_folder):
    # from https://pysimplegui.readthedocs.io/en/latest/
    layout = [
                [sg.T('Stundeplan-Checker', font='DEFAULT 25')],
                [
                    sg.Frame('Allgemeine Einstellungen',
                        [
                            [
                            sg.Text('Untis-File'),
                            sg.InputText(untis_file, size=(100, 1), key='-UNTIS-FILE-'),
                            sg.FileBrowse(initial_folder=inital_file_folder, file_types=(('Untis-Dateien', '*.untis'),))
                            ],
                            [
                                sg.Text('Output-Folder'),
                                sg.InputText(initial_output_folder,size=(100, 1), key='-OUTPUT-FOLDER-'),
                                sg.FolderBrowse(initial_folder=initial_output_folder)
                            ]
                        ]
                    )
                ],
                [
                    sg.Frame('Unterrichts-Checker',
                        [
                            [
                                sg.Checkbox('Fehlende Elemente', default=True, key='-RUN-UNTERRICHT-MEHRFACHE-ELEMENTE-'),
                                sg.Checkbox('Mehrfache Raumzuordnungen', default=True, key='-RUN-UNTERRICHT-MEHRFACHE-RAUMZUORDNUNGEN-')
                            ]
                            
                        ]
                    )
                ],
                                [
                    sg.Frame('Stundenplan-Checker',
                        [
                            [
                                sg.Checkbox('Abgleich Lektionentafel', default=True, key='-RUN-CHECK-LEKTIONENTAFEL-'),
                                sg.Text('Lektionentafel-Excel'),
                                sg.InputText('TODO', size=(100, 1), key='-LEKTIONENTAFEL-EXCEL-'),
                                sg.FileBrowse(file_types=(('Excel-Dateien', '*.exe'),))
                            ],
                            [
                                sg.Checkbox('Abgleich Pensen', default=True, key='-RUN-CHECK-PENSEN-'),
                                sg.Text('Pensen-Excel'),
                                sg.InputText('TODO', size=(100, 1), key='-PENSEN-EXCEL-'),
                                sg.FileBrowse(file_types=(('Excel-Dateien', '*.exe'),))
                            ],
                            
                        ]
                    )
                ],
                [
                    sg.Button('Ausführen'), sg.Button('Abbrechen')
                ] ,
            ]


    window = sg.Window('Stundenplan-Checker', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Abbrechen': # if user closes window or clicks cancel
            break
        elif event == 'Ausführen':
            print('values: ', values)
    window.close()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        path_yaml = sys.argv[1]
        with open(path_yaml) as file:
            config = yaml.load(file, Loader=yaml.FullLoader)
            untis_file = config['untis_file'] if 'untis_file' in config else ''
            initial_file_folder = config['initial_file_folder'] if 'initial_file_folder' in config else ''
            initial_output_folder = config['initial_output_folder'] if 'initial_output_folder' in config else ''
    else:
        untis_file = ''
        initial_file_folder = ''
        initial_output_folder = ''

    run_gui(untis_file, initial_file_folder, initial_output_folder)