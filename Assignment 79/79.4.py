import tkinter as tk
from tkinter import messagebox

BG, ORANGE, DARK = "#FFF7ED", "#C2410C", "#7C2D12"

root = tk.Tk()
root.title("Voting Eligibility Checker")
root.geometry("540x460")
root.configure(bg=BG)
root.resizable(False, False)

def check_eligibility():
    name = name_entry.get().strip()
    age_text = age_entry.get().strip()

    if not name:
        messagebox.showwarning("Missing name", "Please enter the person's name.")
        name_entry.focus_set()
        return

    try:
        age = int(age_text)
        if age < 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid age", "Enter age as a non-negative whole number.")
        age_entry.focus_set()
        return

    if age >= 18:
        result_label.config(text=f"ELIGIBLE TO VOTE\n{name}, age {age}", fg="#166534")
    else:
        result_label.config(text=f"NOT YET ELIGIBLE\n{name} must be at least 18.", fg="#B91C1C")

header = tk.Frame(root, bg="#FFEDD5", padx=24, pady=20, highlightbackground="#FED7AA", highlightthickness=1)
header.pack(fill="x", padx=22, pady=(22, 18))
tk.Label(header, text="CITIZEN SERVICES  /  TASK 04", bg="#FFEDD5", fg=ORANGE,
         font=("Helvetica", 10, "bold")).pack(anchor="w")
tk.Label(header, text="Voting Eligibility", bg="#FFEDD5", fg=DARK,
         font=("Helvetica", 22, "bold")).pack(anchor="w", pady=(6, 4))
tk.Label(header, text="The minimum voting age is 18 years.", bg="#FFEDD5", fg="#9A6042",
         font=("Helvetica", 10)).pack(anchor="w")

card = tk.Frame(root, bg="white", padx=24, pady=20, highlightbackground="#FED7AA", highlightthickness=1)
card.pack(fill="x", padx=22)
tk.Label(card, text="PERSON'S NAME", bg="white", fg=DARK, font=("Helvetica", 10, "bold")).pack(anchor="w")
name_entry = tk.Entry(card, font=("Helvetica", 12), bg="white", fg="#111827",
                      insertbackground="#111827", relief="solid", bd=1)
name_entry.pack(fill="x", ipady=6, pady=(5, 13))
tk.Label(card, text="AGE IN YEARS", bg="white", fg=DARK, font=("Helvetica", 10, "bold")).pack(anchor="w")
age_entry = tk.Entry(card, font=("Helvetica", 12), bg="white", fg="#111827",
                     insertbackground="#111827", relief="solid", bd=1)
age_entry.pack(fill="x", ipady=6, pady=(5, 13))

tk.Button(card, text="CHECK ELIGIBILITY", command=check_eligibility, bg=ORANGE, fg="white",
          activebackground=DARK, activeforeground="white", font=("Helvetica", 11, "bold"),
          relief="flat", cursor="hand2", pady=10).pack(fill="x")

result_label = tk.Label(root, text="Eligibility result appears here", bg=BG, fg="#9A6042",
                        font=("Helvetica", 12, "bold"), pady=16)
result_label.pack()

name_entry.focus_set()
root.bind("<Return>", lambda event: check_eligibility())
root.mainloop()
