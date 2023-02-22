import tkinter as tk
from tkinter import ttk

# Hàm xử lý khi nhấn phím Return trênn button button
def return_pressed(event):
    print('Return key presed.')
    
#hàm ghi log sự kiện
def log(event):
    print(event)

#khởi tạo giaoo diện đồ hoạ
root = tk.Tk()
    
#tạo button có chữ chữ 'save', Gán sự kiện cho phím Return trên buttonn và thực hiện cả hàm log
btn = ttk.Button(root, text='Save')
btn.bind('<Return>', return_pressed)
btn.bind('<Return>', log, add='+' )

#thiết lập focus cho button và đặt button vào giao diện
btn.focus()
btn.pack(expand=True)

root.mainloop()