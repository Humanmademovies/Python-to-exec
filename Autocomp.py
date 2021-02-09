import tkinter as tk
from tkinter import filedialog
import os
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(title="sélectionnez votre script", filetypes=[("fichiers python","*.py;*.pyc")])
rep = os.path.dirname(file_path)
fic = os.path.basename(file_path)
command = ("cd " +str(rep)+ " & " + "pyinstaller --onefile "+ (fic))
os.system(command)
