#mport hai thư viện tkinter và ttk
import tkinter as tk
from tkinter import ttk

#tạo một đối tượng root là cửa sổ chính (main window) của chương trình.
root = tk.Tk()

label = ttk.label(root)
label.config(text='hi, there')
label.pack()


#cuối cùng, gọi phương thức mainloop() để chương trình chạy và hiển thị cửa sổ.
root.mainloop()