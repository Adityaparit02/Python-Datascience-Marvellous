import tkinter as tk
from tkinter import messagebox

BG, NAVY, BLUE, TEXT = "#F2F7FF", "#123B70", "#2878C8", "#17365D"

root = tk.Tk()
root.title("Addition of Two Numbers")
root.geometry("520x430")
root.configure(bg=BG)
root.resizable(False, False)

def calculate_sum():
    try:
        a = float(first_entry.get())
        b = float(second_entry.get())
        total = a + b
        result_label.config(text=f"Result: {total:g}", fg=NAVY)
    except ValueError:
        messagebox.showerror("Invalid input", "Enter a valid number in both fields.")

tk.Label(root, text="ADDITION STUDIO", font=("Helvetica", 11, "bold"),
         bg=NAVY, fg="#BBD9FF", padx=24, pady=10).pack(fill="x", padx=20, pady=(20, 0))
tk.Label(root, text="Addition of Two Numbers", font=("Helvetica", 21, "bold"),
         bg=NAVY, fg="white", pady=8).pack(fill="x", padx=20)
tk.Label(root, text="Enter two numbers, then press Add.",
         font=("Helvetica", 10), bg=NAVY, fg="#DDEBFF", pady=8).pack(fill="x", padx=20, pady=(0, 18))

card = tk.Frame(root, bg="white", padx=24, pady=20, highlightbackground="#D5E5F7", highlightthickness=1)
card.pack(fill="x", padx=20)

tk.Label(card, text="FIRST NUMBER", bg="white", fg=TEXT, font=("Helvetica", 10, "bold")).pack(anchor="w")
first_entry = tk.Entry(card, font=("Helvetica", 13), bg="white", fg="#111827",
                       insertbackground="#111827", relief="solid", bd=1)
first_entry.pack(fill="x", ipady=7, pady=(5, 14))

tk.Label(card, text="SECOND NUMBER", bg="white", fg=TEXT, font=("Helvetica", 10, "bold")).pack(anchor="w")
second_entry = tk.Entry(card, font=("Helvetica", 13), bg="white", fg="#111827",
                        insertbackground="#111827", relief="solid", bd=1)
second_entry.pack(fill="x", ipady=7, pady=(5, 12))

tk.Button(card, text="ADD NUMBERS", command=calculate_sum, bg=BLUE, fg="white",
          activebackground=NAVY, activeforeground="white", font=("Helvetica", 11, "bold"),
          relief="flat", cursor="hand2", pady=10).pack(fill="x")

result_label = tk.Label(root, text="Result will appear here", bg=BG, fg="#52749B",
                         font=("Helvetica", 15, "bold"), pady=18)
result_label.pack()

first_entry.focus_set()
root.bind("<Return>", lambda event: calculate_sum())
root.mainloop()
