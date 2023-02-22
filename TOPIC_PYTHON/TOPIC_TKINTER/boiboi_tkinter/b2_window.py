
#import module tkinter và đặt tên là tk
import tkinter as tk

#tạo một cửa sổ gốc. Đặt tiêu đề cho cửa sổ là ứng dụng của tôi
root = tk.Tk()
root.title('ứng dụng của mchau')

#Thiết lập chiều rộng và chiều cao cho cửa sổ
window_width = 300
window_height = 200

# lấy kích thước màn hình
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#lấy tọa độ trung tâm của màn hình
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

#Đặt vị trí của cửa sổ ở giữa màn hình
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

#Hiển thị cửa sổ
root.mainloop()
