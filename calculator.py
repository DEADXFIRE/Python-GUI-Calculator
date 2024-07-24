import tkinter as tk

def update_display(entry, value):
    current_text = entry.get()
    if current_text == "0":
        entry.delete(0, tk.END)
        entry.insert(tk.END, value)
    else:
        entry.insert(tk.END, value)


def clear_display(entry):
    entry.delete(0, tk.END)
    entry.insert(tk.END, "0")

def calculate_expression(entry):
    try:
        result = eval(entry.get().replace('×', '*').replace('÷', '/'))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def delete_last_character(entry):
    current_text = entry.get()
    if len(current_text) > 1:
        entry.delete(len(current_text)-1, tk.END)
    else:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "0")

root = tk.Tk()
root.title("Calculator")
root.geometry("350x480")
root.iconbitmap("calculator.ico")
root.resizable(0, 0)
root.configure(bg="#f0f0f0")

entry = tk.Entry(root, font=("Helvetica", 20), bd=0, insertwidth=2, borderwidth=2, bg="#ffffff", justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=20, padx=20, ipady=10, sticky="nsew")
entry.insert(0, "0")

entry.config(highlightbackground="#3b3b3b", highlightcolor="#1e90ff", highlightthickness=2, relief="solid", borderwidth=0)
entry.bind("<FocusIn>", lambda event: entry.config(bg="#e0e0e0"))
entry.bind("<FocusOut>", lambda event: entry.config(bg="#ffffff"))

button_params = {
    "font": ("Helvetica", 14, "bold"),
    "bd": 0,
    "fg": "white",
    "height": 2,
    "width": 5
}

buttons = [
    ('7', 1, 0, "#1e90ff"), ('8', 1, 1, "#1e90ff"), ('9', 1, 2, "#1e90ff"), ('÷', 1, 3, "#ff6347"),
    ('4', 2, 0, "#1e90ff"), ('5', 2, 1, "#1e90ff"), ('6', 2, 2, "#1e90ff"), ('×', 2, 3, "#ff6347"),
    ('1', 3, 0, "#1e90ff"), ('2', 3, 1, "#1e90ff"), ('3', 3, 2, "#1e90ff"), ('-', 3, 3, "#ff6347"),
    ('0', 4, 0, "#1e90ff", 2), ('.', 4, 2, "#1e90ff"), ('+', 4, 3, "#ff6347"),
    ('=', 5, 0, "#32cd32", 2), ('C', 5, 2, "#ff6347"), ('⌫', 5, 3, "#ff6347")
]

for button in buttons:
    text, row, col, color = button[0], button[1], button[2], button[3]
    colspan = button[4] if len(button) == 5 else 1
    if text == '=':
        action = lambda x=text: calculate_expression(entry)
    elif text == 'C':
        action = lambda x=text: clear_display(entry)
    elif text == '⌫':
        action = lambda x=text: delete_last_character(entry)
    else:
        action = lambda x=text: update_display(entry, x)
    btn = tk.Button(root, text=text, command=action, bg=color, **button_params)
    btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=5, pady=5)

label = tk.Label(root, text="Developed by DeadXFire", font=("Helvetica", 10), bg="#f0f0f0")
label.grid(row=6, column=0, columnspan=4, pady=10)

root.mainloop()
