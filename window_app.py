import tkinter as tk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "user" and password == "pass":
        messagebox.showinfo("Login Success", f"Welcome, {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

root = tk.Tk()
root.title("Login Page")
root.geometry("350x260")
root.configure(bg="#2c3e50")

frame = tk.Frame(root, bg="#34495e", bd=2, relief="groove")
frame.place(relx=0.5, rely=0.5, anchor="center", width=300, height=220)

title_label = tk.Label(frame, text="Login", font=("Arial", 16, "bold"), fg="#94e0c0", bg="#34495e")
title_label.pack(pady=(10, 5))

tk.Label(frame, text="Username:", font=("Arial", 11), fg="#ecf0f1", bg="#34495e").pack(pady=(5, 2))
username_entry = tk.Entry(frame, font=("Arial", 11), bg="#ecf0f1", fg="#2c3e50", relief="flat")
username_entry.pack(ipady=2)

tk.Label(frame, text="Password:", font=("Arial", 11), fg="#ecf0f1", bg="#34495e").pack(pady=(8, 2))
password_entry = tk.Entry(frame, show="*", font=("Arial", 11), bg="#ecf0f1", fg="#2c3e50", relief="flat")
password_entry.pack(ipady=2)

login_btn = tk.Button(frame, text="Login", command=login, font=("Arial", 11, "bold"), bg="#27ae60", fg="#ecf0f1", activebackground="#2ecc71", activeforeground="#ecf0f1", relief="flat", cursor="hand2")
login_btn.pack(padx=(10, 10), pady=(15, 10))

root.mainloop()

