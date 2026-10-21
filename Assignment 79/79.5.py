import tkinter as tk
from tkinter import messagebox

VALID_USERNAME = "admin"
VALID_PASSWORD = "python123"

BG, PURPLE, ACCENT = "#F4F1FF", "#4C1D95", "#7C3AED"

root = tk.Tk()
root.title("Basic Login Form")
root.geometry("500x470")
root.configure(bg=BG)
root.resizable(False, False)

def login():
    username = username_entry.get().strip()
    password = password_entry.get()

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        status_label.config(text=f"Login successful. Welcome, {username}!", fg="#166534")
        messagebox.showinfo("Login successful", f"Welcome, {username}!")
    else:
        status_label.config(text="Login failed. Check your credentials.", fg="#B91C1C")
        messagebox.showerror("Login failed", "Invalid username or password.")

header = tk.Frame(root, bg=PURPLE, padx=26, pady=23)
header.pack(fill="x", padx=22, pady=(22, 18))
tk.Label(header, text="ACCOUNT ACCESS", bg=PURPLE, fg="#DDD6FE",
         font=("Helvetica", 10, "bold")).pack(anchor="w")
tk.Label(header, text="Welcome back", bg=PURPLE, fg="white",
         font=("Helvetica", 24, "bold")).pack(anchor="w", pady=(7, 4))
tk.Label(header, text="Enter the demo username and password below.", bg=PURPLE,
         fg="#EDE9FE", font=("Helvetica", 10)).pack(anchor="w")

card = tk.Frame(root, bg="white", padx=24, pady=22, highlightbackground="#DDD6FE", highlightthickness=1)
card.pack(fill="x", padx=22)

tk.Label(card, text="USERNAME", bg="white", fg="#2E1065",
         font=("Helvetica", 10, "bold")).pack(anchor="w")
username_entry = tk.Entry(card, font=("Helvetica", 12), bg="white", fg="#111827",
                          insertbackground="#111827", relief="solid", bd=1)
username_entry.pack(fill="x", ipady=6, pady=(5, 13))

tk.Label(card, text="PASSWORD", bg="white", fg="#2E1065",
         font=("Helvetica", 10, "bold")).pack(anchor="w")
password_entry = tk.Entry(card, font=("Helvetica", 12), bg="white", fg="#111827",
                          insertbackground="#111827", show="*", relief="solid", bd=1)
password_entry.pack(fill="x", ipady=6, pady=(5, 14))

tk.Button(card, text="LOGIN", command=login, bg=ACCENT, fg="white",
          activebackground=PURPLE, activeforeground="white", font=("Helvetica", 11, "bold"),
          relief="flat", cursor="hand2", pady=10).pack(fill="x")

status_label = tk.Label(root, text="Demo username: admin   |   password: python123",
                        bg=BG, fg="#6D5A99", font=("Helvetica", 9), pady=14)
status_label.pack()

username_entry.focus_set()
root.bind("<Return>", lambda event: login())
root.mainloop()
