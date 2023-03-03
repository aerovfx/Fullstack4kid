from tkinter import *
from tkcalendar import Calendar
from datetime import datetime

# pip install tkcalendar before run program
# nếu còn lỗi thì tạo môi trường chạy cho app: python -m venv myenv
# sau ddos active: source dduonwgf daaxn file activeate

root = Tk()
root.title("cung hoàng đạo: Zodiac App")
root.geometry("400x400")

# define function to determine Zodiac based on date
def get_zodiac(month, day):
    if month == 1:
        if day <= 19:
            return "Capricorn: Cung ma kết"
        else:
            return "Aquarius: Cung Bảo Bình"



# Define function to get date from calendar widget
def get_date():
    date_label.config(text=cal.selection_get())
    date = cal.selection_get()
    month = date.month
    day = date.day
    zodiac = get_zodiac(month, day)
    zodiac_label.config(text=f"Cung Hoàng Đạo của bạn là {zodiac}")

# Create calendar widget
cal = Calendar(root, selectmode="day", year=2022, month=1, day=1)
cal.pack(pady=20)

# Create button to get selected date
date_btn = Button(root, text="Get Date", command=get_date)
date_btn.pack(pady=10)

# Create label to display selected date
date_label = Label(root, text="")
date_label.pack(pady=10)

# Create label to display Zodiac sign
zodiac_label = Label(root, text="")
zodiac_label.pack(pady=10)

root.mainloop()