import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import math

data = {}

def calculate_fee(entry, exit_time):
    hours = (exit_time - entry).total_seconds() / 3600
    fee = 5000
    if hours > 6:
        fee += math.ceil(hours - 6) * 1000
    return fee

def register_entry():
    plate = entry_plate.get()
    if not plate:
        messagebox.showwarning("خطا", "شماره پلاک را وارد کنید.")
        return
    if plate in data and data[plate]["status"] == "in":
        messagebox.showinfo("یادآوری", "این خودرو قبلاً وارد شده است.")
        return
    data[plate] = {"entry": datetime.now(), "exit": None, "status": "in"}
    messagebox.showinfo("موفق", "ورود ثبت شد.")

def register_exit():
    plate = entry_plate.get()
    if plate not in data or data[plate]["status"] != "in":
        messagebox.showerror("خطا", "این خودرو در حال حاضر در پارکینگ نیست.")
        return
    exit_time = datetime.now()
    entry_time = data[plate]["entry"]
    fee = calculate_fee(entry_time, exit_time)
    data[plate]["exit"] = exit_time
    data[plate]["status"] = "out"
    messagebox.showinfo("خروج ثبت شد", f"هزینه: {fee} تومان")

def show_status():
    status_text.delete('1.0', tk.END)
    for plate, info in data.items():
        s = "در پارکینگ ✅" if info["status"] == "in" else "خارج شده 🚗"
        status_text.insert(tk.END, f"پلاک: {plate} | وضعیت: {s}\n")

root = tk.Tk()
root.title("سیستم پارکینگ")

tk.Label(root, text="شماره پلاک:").grid(row=0, column=0, pady=5)
entry_plate = tk.Entry(root)
entry_plate.grid(row=0, column=1, pady=5)

tk.Button(root, text="ثبت ورود", command=register_entry).grid(row=1, column=0, padx=5, pady=5)
tk.Button(root, text="ثبت خروج", command=register_exit).grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text="وضعیت خودروها", command=show_status).grid(row=2, column=0, columnspan=2, pady=5)

status_text = tk.Text(root, width=40, height=10)
status_text.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()