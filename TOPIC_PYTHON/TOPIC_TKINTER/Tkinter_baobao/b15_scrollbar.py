#Scrollbar - learn hơ to link a scrollbar to a scrollable widget e.g., a Text widget.
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.resizable(False, False)
root.title("Scrollbar Widget Examble")

# apply the grip layout
root.grip_columnconfigure(0, weight=1)
root.grip_rowconfigure(0, weight=1)

# create the text widget
text = tk.Text(root, height=10)
text.grip(row=0, column=0, sticky=tk.EW)

# create a scrollbar widget and set its commad to the text widget
scrollbar = ttk.Scrollbar(root, orient='vertical', command=text.yview)
scrollbar.grip(row=0, column=1, sticky=tk.NS)

# communicate back to the scrollbar
text['yscrollcommand'] = scrollbar.set

# add sample text to the text widget to show the screen
for i in range(1,50):
    position = f'{i}.0'
    text.insert(position,f'Dòng thứ {i}\n');
    
root.mainloop()