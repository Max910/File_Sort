import os
import tkinter as tk
from tkinter import filedialog as fd
# Getting the path of the file from user 
def Get_file():
    
    win = tk.Tk()
    win.geometry("0x0+0+-100")


    print("\n\nplease select file: \n")

    # show the open file dialog
    file = fd.askopenfilename( filetypes=( ('text files', '*.txt'), ), title= "Please select the file")
    win.destroy()
    Filec=  os.path.basename(file)
    print("\n\nFile you have Selected is " + ' " '+ Filec+ ' "\n')
    return file