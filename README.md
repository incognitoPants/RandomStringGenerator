# Random String Generator
***
This creates a random 12-character alphanumeric string and automatically
copies it to the user's clipboard.

It uses `tkinter` to create the GUI to make it user friendly. This is meant
to create an executable file to have the desired result. Running the python
script through console will not result in what you are looking for as tkinter
does not display well when ran this way. 

_Note: This was developed using Python 3.7 and 3.8. No guarantees it will work
with other versions_

## Instructions
The script has to be compiled via `pyinstaller` or similar tool. You can
install it via `pip`.
```
pip install pyinstaller
```

After installing `pyinstaller` run the following command in the directory
containing the script. This will create the executable file in a folder called
*dist* in the current directory.
```
pyinstaller --onefile random_generator.py
```

It is important you include `--onefile` in order to have a single file to run.

