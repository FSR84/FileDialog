import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
root.withdraw()

#open file dialog and select a file manually
path_and_file = filedialog.askopenfilename()
path_name = os.path.split(path_and_file)[0]
file_name = os.path.split(path_and_file)[1]

print(path_and_file)
print(path_name)
print(file_name)


