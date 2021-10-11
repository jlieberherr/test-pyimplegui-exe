# How to do a pysimple-gui, make an executable and run the executable with a config-file by drag and drop

## Installation
* ```"cd path\to\venv\folder"```
* ```"path\to\Python3.8\python.exe" -m venv venv_test_pysimplegui_exe```
* ```venv_test_pysimplegui_exe/Scripts/activate```
* ```cd "path\to\dev\folder"```
* ```git clone https://github.com/jlieberherr/test-pysimplegui-exe.git```
* ```cd test-pysimplegui-exe```
* ```pip install -r requirements.txt```
* ```pyinstaller -wF gui.py``` (creates ```gui.exe``` in ```dist```-folder)

## Run with config-file from Python
* ```python gui.py config.yaml```

## Run with config-file from executable by drag and drop
* Drag and drop ```config.yaml``` on the ```gui.exe``` in the ```dist```-folder