import tkinter as tk
from tkinter import messagebox
import sqlite3
import re

# ===== DB =====
def connect_db():
    return sqlite3.connect("members.db")

# ===== VALIDATE =====
def validate():
    if not first.get() or not last.get() or not phone.get() or not password.get():
        messagebox.showerror("Lỗi", "Nhập đầy đủ thông tin")
        return False

    if not gender.get():
        messagebox.showerror("Lỗi", "Chọn giới tính")
        return False

    if not agree.get():
        messagebox.showerror("Lỗi", "Phải đồng ý điều khoản")
        return False

    if len(password.get()) < 8 or not re.search(r"[!@#$%^&*]", password.get()):
        messagebox.showerror("Lỗi", "Mật khẩu >=8 ký tự + ký tự đặc biệt")
        return False

    return True

# ===== REGISTER =====
def register():
    if not validate():
        return

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO members(first_name,last_name,phone,password,gender)
    VALUES(?,?,?,?,?)
    """, (first.get(), last.get(), phone.get(), password.get(), gender.get()))

    conn.commit()
    conn.close()

    messagebox.showinfo("OK", "Đăng ký thành công!")

# ===== UI =====
root = tk.Tk()
root.title("Facebook Register Clone")
root.geometry("500x650")
root.configure(bg="#f0f2f5")

# ===== Container =====
frame = tk.Frame(root, bg="white", bd=0)
frame.place(relx=0.5, rely=0.5, anchor="center", width=380, height=550)

# ===== Title =====
tk.Label(frame, text="facebook", fg="#1877f2",
         bg="white", font=("Arial", 28, "bold")).pack(pady=10)

tk.Label(frame, text="Đăng ký nhanh chóng và dễ dàng",
         bg="white", font=("Arial", 10)).pack(pady=5)

# ===== Inputs =====
first = tk.StringVar()
last = tk.StringVar()
phone = tk.StringVar()
password = tk.StringVar()
gender = tk.StringVar()
agree = tk.IntVar()

def entry_style(parent, textvar, show=None):
    e = tk.Entry(parent, textvariable=textvar, font=("Arial", 11),
                 bd=1, relief="solid")
    e.pack(pady=5, ipadx=10, ipady=8, fill="x", padx=20)
    if show:
        e.config(show=show)
    return e

entry_style(frame, first)
entry_style(frame, last)
entry_style(frame, phone)
entry_style(frame, password, "*")

# ===== Gender =====
g_frame = tk.Frame(frame, bg="white")
g_frame.pack(pady=5)

tk.Radiobutton(g_frame, text="Nam", variable=gender, value="Nam",
               bg="white").pack(side="left", padx=10)
tk.Radiobutton(g_frame, text="Nữ", variable=gender, value="Nữ",
               bg="white").pack(side="left", padx=10)

# ===== Terms =====
tk.Checkbutton(frame,
               text="Tôi đồng ý với điều khoản",
               variable=agree,
               bg="white").pack(pady=10)

# ===== Button =====
tk.Button(frame, text="Đăng ký",
          bg="#42b72a", fg="white",
          font=("Arial", 12, "bold"),
          bd=0, padx=10, pady=10,
          command=register).pack(pady=20, ipadx=40)

root.mainloop()