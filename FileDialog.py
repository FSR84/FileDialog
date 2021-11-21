import tkinter as tk
from tkinter import filedialog, messagebox
import os

root = tk.Tk()
root.withdraw()


if messagebox.askyesno("Message","Do you want to open a single file?") == True:

    # open file dialog and select a single file manually
    path_and_file = filedialog.askopenfilename() #can limit file types displayed with e.g.: askopenfilename(filetypes = (('xls files','*.xls'),))
    path_name = os.path.split(path_and_file)[0]
    file_name = os.path.split(path_and_file)[1]

    print(path_and_file)
    print(path_name)
    print(file_name)


if messagebox.askyesno("Message","Do you want to open multiple files?") == True:

    # open file dialog and select multiple files manually
    files_tupple = filedialog.askopenfilenames()
    print(files_tupple)

    for path_and_file in files_tupple:
        path_name = os.path.split(path_and_file)[0]
        file_name = os.path.split(path_and_file)[1]

        print(path_and_file)
        print(path_name)
        print(file_name)

