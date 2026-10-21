import tkinter as tk
from tkinter import messagebox

BG, PANEL, PURPLE, TEXT = "#17152B", "#211E3A", "#8B72F8", "#F5F3FF"

root = tk.Tk()
root.title("Find the Largest Number")
root.geometry("540x500")
root.configure(bg=BG)
root.resizable(False, False)

def find_largest():
    try:
        values = [float(entry.get()) for entry in entries]
        largest = max(values)
        result_label.config(text=f"LARGEST NUMBER\n{largest:g}", fg="#C4B5FD")
    except ValueError:
        messagebox.showerror("Invalid input", "Enter a valid number in all three fields.")

tk.Label(root, text="NUMBER ANALYSIS  /  TASK 02", bg=BG, fg="#B8A8FF",
         font=("Helvetica", 10, "bold")).pack(anchor="w", padx=26, pady=(24, 8))
tk.Label(root, text="Find the Largest Number", bg=BG, fg=TEXT,
         font=("Helvetica", 21, "bold")).pack(anchor="w", padx=26)
tk.Label(root, text="Compare three numbers to find the maximum.", bg=BG, fg="#C6C2DF",
         font=("Helvetica", 10)).pack(anchor="w", padx=26, pady=(6, 18))

card = tk.Frame(root, bg=PANEL, padx=22, pady=20, highlightbackground="#454064", highlightthickness=1)
card.pack(fill="x", padx=24)
entries = []
for field_name in ("NUMBER A", "NUMBER B", "NUMBER C"):
    tk.Label(card, text=field_name, bg=PANEL, fg="#E5DEFF",
             font=("Helvetica", 10, "bold")).pack(anchor="w")
    entry = tk.Entry(card, font=("Helvetica", 12), bg="#FFFFFF", fg="#17152B",
                     insertbackground="#17152B", relief="solid", bd=1)
    entry.pack(fill="x", ipady=6, pady=(5, 12))
    entries.append(entry)

tk.Button(card, text="FIND MAXIMUM", command=find_largest, bg=PURPLE, fg="white",
          activebackground="#7257E8", activeforeground="white", font=("Helvetica", 11, "bold"),
          relief="flat", cursor="hand2", pady=10).pack(fill="x")

result_label = tk.Label(root, text="Result appears here", bg=BG, fg="#C4B5FD",
                        font=("Helvetica", 17, "bold"), pady=18)
result_label.pack()

entries[0].focus_set()
root.bind("<Return>", lambda event: find_largest())
root.mainloop()
