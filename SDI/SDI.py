import tkinter as tk
from tkinter import messagebox
import sys

window = tk.Tk()
window.withdraw()

def checked_import(StringModuleName):
    try:
        exec("import " + StringModuleName)
    except ImportError:
        if messagebox.askyesno('Install Dependencies', 'There are missing dependencies needed for the program to work\
        (module "' + StringModuleName + '"). Would you like the program to install them?\nRestart the app after\
        installation.') == True:    
            import subprocess
            try:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--user', StringModuleName])
                exec("import " + StringModuleName)
            except subprocess.CalledProcessError:
                messagebox.showinfo("Error", "Module does not exist (or permission denied)")
        else:
            sys.exit()
