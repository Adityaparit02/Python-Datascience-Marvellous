import tkinter as tk
from tkinter import messagebox
import math

BG, GREEN, TEXT = "#F0F8F3", "#174D37", "#163A2A"

root = tk.Tk()
root.title("Area of a Circle")
root.geometry("520x420")
root.configure(bg=BG)
root.resizable(False, False)

def calculate_area():
    try:
        radius = float(radius_entry.get())
        if radius < 0:
            messagebox.showerror("Invalid radius", "Radius cannot be negative.")
            return
        area = math.pi * radius * radius
        result_label.config(text=f"Area = {area:,.4f} square units", fg=GREEN)
    except ValueError:
        messagebox.showerror("Invalid input", "Enter a valid numeric radius.")

tk.Label(root, text="GEOMETRY TOOL  /  TASK 03", bg=GREEN, fg="#A7F3D0",
         font=("Helvetica", 10, "bold"), padx=24, pady=12).pack(fill="x", padx=22, pady=(22, 0))
tk.Label(root, text="Area of a Circle", bg=GREEN, fg="white",
         font=("Helvetica", 22, "bold"), pady=8).pack(fill="x", padx=22)
tk.Label(root, text="Formula: Area = π × radius²", bg=GREEN, fg="#D1FAE5",
         font=("Helvetica", 10), pady=8).pack(fill="x", padx=22, pady=(0, 18))

card = tk.Frame(root, bg="white", padx=24, pady=22, highlightbackground="#CDE5D6", highlightthickness=1)
card.pack(fill="x", padx=22)
tk.Label(card, text="RADIUS (UNITS)", bg="white", fg=GREEN,
         font=("Helvetica", 10, "bold")).pack(anchor="w")
radius_entry = tk.Entry(card, font=("Helvetica", 13), bg="white", fg="#111827",
                        insertbackground="#111827", relief="solid", bd=1)
radius_entry.pack(fill="x", ipady=7, pady=(6, 14))
radius_entry.insert(0, "5")

tk.Button(card, text="CALCULATE AREA", command=calculate_area, bg="#19734E", fg="white",
          activebackground=GREEN, activeforeground="white", font=("Helvetica", 11, "bold"),
          relief="flat", cursor="hand2", pady=10).pack(fill="x")

result_label = tk.Label(root, text="Area will appear here", bg=BG, fg="#426653",
                        font=("Helvetica", 13, "bold"), pady=18)
result_label.pack()

radius_entry.focus_set()
root.bind("<Return>", lambda event: calculate_area())
root.mainloop()
