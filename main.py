from tkinter import *
import tkinter.messagebox

#contants
WIDTH = 200
HEIGHT = 150

#functions
def calculate():
    try:
        f = fahrenheit.get()
        c = celsius.get()
        f.strip()
        c.strip()
        if c!='' and f=='':
            c = float(c)
            ans = (c * 9/5) + 32
            fahrenheit.insert(END, f'{ans}')
            celsius.delete(0, END)
        elif c=='' and f!='':
            f = float(f)
            ans = (f -32) * 5/9
            celsius.insert(END, f'{ans}')
            fahrenheit.delete(0, END)
        elif c!='' and f!='':
            tkinter.messagebox.showinfo(title="that ain't right", message=f'One box must be blank. How else will I know what to convert?')
        
    except ValueError:
        tkinter.messagebox.showerror(title="that ain't right", message=f'Please give an integer value or float.')

#main window
root = Tk()
root.config(bg='black')
root.title('c2f')
try:
    root.iconbitmap('icon.ico')
except:
    pass

#geometry
root.geometry(f'{WIDTH}x{HEIGHT}')
root.minsize(WIDTH, HEIGHT)
root.maxsize(WIDTH, HEIGHT)

#widgets
flabel = Label(root, text='fahrenheit', font='Terminal', fg='limegreen', bg='black')
clabel = Label(root, text='celsius', font='Terminal', fg='limegreen', bg='black')
fahrenheit = Entry(root, width=30, font='Terminal', bd=-1, fg='limegreen', bg='#101C15')
celsius = Entry(root, width=30, font='Terminal', bd=-1, fg='limegreen', bg='#101C15')
calculatebtn = Button(root, text='calculate', font='Terminal', command=calculate, bd=-1, fg='limegreen', bg='black')

#packing
flabel.pack(padx=3, pady=3)
fahrenheit.pack(padx=5, pady=5)
clabel.pack(padx=3, pady=3)
celsius.pack(padx=5, pady=5)
calculatebtn.pack(padx=5, pady=5)
root.mainloop()