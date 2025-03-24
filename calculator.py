import tkinter as tk
from tkinter import messagebox


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


def on_button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + value)


def on_clear():
    entry.delete(0, tk.END)


def on_calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create and place the widgets
entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# fmt: off
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]
# fmt: on

row = 1
col = 0
for button in buttons:
    action = lambda x=button: on_button_click(x) if x != "=" else on_calculate()
    tk.Button(root, text=button, width=5, height=2, command=action).grid(
        row=row, column=col
    )
    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(root, text="C", width=5, height=2, command=on_clear).grid(row=row, column=col)

# Run the application
root.mainloop()
