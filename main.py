from afd import verify_afd
from read_file import read_txt
import tkinter as tk
from tkinter import filedialog

# Open a dialog box to choose the AFD definition file:
root = tk.Tk()
root.withdraw()
path_to_file = filedialog.askopenfilename()
print(path_to_file)

# Read the file and store it:
name, states, initial_state, sigma, final_states, delta = read_txt(path_to_file)

# User type the input string:
print("Type a string: ")
string = raw_input()

# Describe the AFD result, if the string is valid or not:
if verify_afd(name, final_states, initial_state, delta, string, sigma):
    print("Valid string!")
else:
    print("Invalid string!")
