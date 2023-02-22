#mport hai thư viện tkinter và ttk.
import tkinter as tk
from tkinter import ttk

#Tạo một đối tượng root là cửa sổ chính (main window) của chương trình.
root = tk.Tk()

#tạo một nhãn văn bản thông thường (classic label) bằng lệnh tk.label(root, text='classic label') và đặt nó vào cửa sổ root bằng phương thức pack(). Tạo một nhãn văn bản được thiết kế (themed label) bằng lệnh ttk.label(root, text='theemed label') và đặt nó vào cửa sổ root bằng phương thức pack().


tk.label(root, text='classic label').pack()
ttk.label(root, text='themed label').pack()


# cuối cùng, gọi phương thức mainloop() để chương trình chạy và hiển thị cửa sổ.
root.mainloop()

'''
những ttk widgets khác thường được dùng
tkinter.ttk

button
checkbutton
entry
frame
label
labelframe
menubutton
panewindow
radiobutton
scale
scrollbar
spinbox
and the following widgets are new and specific to ttk:

combobox
notebook
progressbar
separator
sizegrid
treeview
'''