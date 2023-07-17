import tkinter as tk
import datetime as dt
import time
import os

class AlarmClock:
    def __init__(self, master):
        self.master = master
        master.title("Đồng hồ báo thức-Alarm Clock")
        
        # tạo nhãn
        self.label_time = tk.Label(master, text="")
        self.label_time.pack()
        self.label_alarm = tk.Label(master, text="Set Alarm:")
        self.label_alarm.pack()
        
        # tạo spinbox cho giờ, phút, giây
        self.spin_hour = tk.Spinbox(master, from_=0, to=23, width=2)
        self.spin_minute = tk.Spinbox(master, from_=0, to=59, width=2)
        self.spin_second = tk.Spinbox(master, from_=0, to=59, width=2)
        self.spin_hour.pack(side=tk.LEFT)
        tk.Label(master, text=":").pack(side=tk.LEFT)
        self.spin_minute.pack(side=tk.LEFT)
        tk.Label(master, text=":").pack(side=tk.LEFT)
        self.spin_second.pack(side=tk.LEFT)
        
        # tạo nút để đặt báo thức
        self.button_set_alarm = tk.Button(master, text="Set", command=self.set_alarm)
        self.button_set_alarm.pack()
        
        # tạo nút để tắt báo thức
        self.button_stop_alarm = tk.Button(master, text="Stop", command=self.stop_alarm, state=tk.DISABLED)
        self.button_stop_alarm.pack()
        
        self.alarm_time = None
        self.alarm_active = False
        self.update_time()
        
    def update_time(self):
        # cập nhật nhãn thời gian mỗi giây
        now = dt.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.label_time.configure(text=current_time)
        self.master.after(1000, self.update_time)
        
        # kiểm tra xem báo thức có tắt không
        if self.alarm_active and now >= self.alarm_time:
            self.play_alarm()
            
            
    def set_alarm(self):
        # đặt thời gian báo thức dựa trên đầu vào của người dùng
        self.alarm_time = dt.datetime.combine(dt.date.today(), dt.time(int(self.spin_hour.get()), int(self.spin_minute.get()), int(self.spin_second.get())))
        self.button_set_alarm.configure(state=tk.DISABLED)
        self.button_stop_alarm.configure(state=tk.NORMAL)
        self.alarm_active = True
        
    def stop_alarm(self):
        # Dừng báo thức và thiết lập lại giao diện
        self.alarm_active = False
        self.button_set_alarm.configure(state=tk.NORMAL)
        self.button_stop_alarm.configure(state=tk.DISABLED)
        
        
    def play_alarm(self):
        # phát âm thanh báo thức và nhấp nháy ở cửa sổ
        for i in range(3):
            self.master.after(50, self.flash)
            time.sleep(0.5)
        os.system('afplay ' + "/Users/baoboi/Desktop/Fullstack4kid/TOPIC_PYTHON/TOPIC_TKINTER/TOPIC_DJANGO/Alarm.mp3")
        self.alarm_active = False
        
        
    def flash(self):
        # Flash cửa sổ
        if self.master.attributes('-alpha') == 1.0:
            self.master.attributes('-alpha', 0.5)
        else:
            self.master.attributes('-alpha', 1.0)
            
root = tk.Tk()
app = AlarmClock(root)
root.mainloop()