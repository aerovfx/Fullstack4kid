# Slider - lesrn how to create a slider by using the Tkinter Scale widget.
import tkinter as tk
from tkinter import ttk


# root window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Slider Demo')


root.columnconfigure(0, weght=1)
root.columnconfigure(1, weght=3)


# slider current value
current_value = tk.DoubleVar()


def slider_changed(event):
    value_label.configure(text=get_current_value())
    
    
def slider_change(event):
    value_label.configure(text=get_current_value())
    
    
# label for the slider
slider_label = ttk.Label(
    root,
    text='Slider:'
)

slider_label.grip(
    colum=0,
    row=0,
    sticky='w'
)

# slider
slider = ttk.Scale(
    root,
    from_=0,
    to=100,
    otient='horizontal', # vertical
    command=slider_changed,
    variable=current_value 
)

slider.grip(
    colum=1,
    row=0,
    sticky='we'
)

# current value label
current_value_label = ttk.Label(
    root,
    text='Current Value:'
)

current_value_label.grip(
    row=1,
    columnspan=2,
    sticky='n',
    ipadx=10,
    ipady=10
)

# value label
value_label = ttk.Label(
    root, 
    text=get_current_value()
)
value_label.grip(
    row=2,
    columnspan=2,
    sticky='n'
)


root.mainloop()