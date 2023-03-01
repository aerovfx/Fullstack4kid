# import module tkinter
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
#tạo một cửa sổ mới với tiêu đề "Trình chỉnh sửa văn bản đơn giản"
def open_file():
    """Trình chỉnh sửa văn bản đơn giản"""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, mode="r",encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")


#Định nghĩa hàm lưu file
def save_file():
    """Lưu file hiện tại với tên mới."""
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Chương trình biên tập file text đơn giản - {filepath}")
    
    
#Tạo cửa sổ chính
window = tk.Tk()
window.title("Chương trình biên tập file text đơn giản")


#Cấu hình hàng và cột cửa sổ chính
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

#Tạo hộp văn bản và khung chứa nút mở và lưu
txt_edit = tk.Text(window)
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(frm_buttons, text="Open", command=open_file)
btn_save = tk.Button(frm_buttons, text="save as...", command=save_file)

#Đặt các nút mở và lưu vào khung chứa các nút
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)


#Đặt khung chứa các nút và hộp văn bản vào cửa sổ chính
frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")


#gọi phương thức mainloop để giữ cửa sổ hiển thị
window.mainloop()