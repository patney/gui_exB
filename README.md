#QtDesigner
Download as an application.
To edit the main ui file navigate to src/ui/raw_ui and open main_window.ui
After the file is saved it has to be converted to  .py file.

#Convert .ui to .py
Select 'terminal' in pycharm and enter:
pyuic5.exe .\src\ui\raw_ui\main_window.ui -o .\src\ui\main_window.py
NOTE: uic is part of PyQt5


