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
slider_label = ttk.Label