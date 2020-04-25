from tkinter import filedialog
from tkinter import *

def browse_button():
    global directory_path
    file_name = filedialog.askdirectory()
    directory_path.set(file_name)
    print(file_name)


root = Tk()
directory_path = StringVar()
lbl1 = Label(master=root,textvariable=directory_path)
lbl1.grid(row=0, column=1)
button2 = Button(text="Browse file", command=browse_button)
button2.grid(row=0, column=3)

mainloop()