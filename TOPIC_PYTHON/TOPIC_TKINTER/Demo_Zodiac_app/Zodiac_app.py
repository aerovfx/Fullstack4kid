from tkinter import *
from tkcalendar import Calendar
from datetime import datetime

#pip install tkcalendar before run program 
#Nếu còn lỗi thì tạo môi trường chạy cho app: python -m venv myenv 
# Sau đó active: source đường dẫn file activate

root = Tk()
root.title("Cung Hoàng Đạo: Zodiac App")
root.geometry("400x400")

# Define function to determine Zodiac based on date
def get_zodiac(month, day):
    if month == 1:
        if day <= 19:
            return "Capricorn: Cung Ma Kết"
        else:
            return "Aquarius: Cung Bảo Bình"
    elif month == 2:
        if day <= 18:
            return "Aquarius: Cung Bảo Bình"
        else:
            return "Pisces: Cung Song Ngư"
    elif month == 3:
        if day <= 20:
            return "Pisces: Cung Song Ngư"
        else:
            return "Aries: Cung Bạch Dương"
    elif month == 4:
        if day <= 19:
            return "Aries: Cung Bạch Dương"
        else:
            return "Taurus: Cung Kim Ngưu"
    elif month == 5:
        if day <= 20:
            return "Taurus: Cung Kim Ngưu"
        else:
            return "Gemini: Cung Song Tử"
    elif month == 6:
        if day <= 20:
            return "Gemini: Cung Song Tử"
        else:
            return "Cancer: Cự Giải"
    elif month == 7:
        if day <= 22:
            return "Cancer: Cung Cự Giải"
        else:
            return "Leo: Cung Sư tử"
    elif month == 8:
        if day <= 22:
            return "Leo: Cung Sư tử"
        else:
            return "Virgo: Cung Xử Nữ"
    elif month == 9:
        if day <= 22:
            return "Virgo: Cung Xử Nữ"
        else:
            return "Libra: Cung Thiên Bình"
    elif month == 10:
        if day <= 22:
            return "Libra: Cung Thiên Bình"
        else:
            return "Scorpio: Cung Bọ Cạp"
    elif month == 11:
        if day <= 21:
            return "Scorpio: Cung Bọ Cạp"
        else:
            return "Sagittarius: Cung Nhân Mã"
    else:
        if day <= 21:
            return "Sagittarius: Cung Nhân Mã"
        else:
            return "Capricorn: Cung Ma Kết"

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
