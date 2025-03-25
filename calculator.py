import tkinter as tk
from tkinter import messagebox, ttk
import operator


def on_button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + value)


def on_clear():
    entry.delete(0, tk.END)


def on_calculate():
    try:
        expression = entry.get()
        result = evaluate_expression(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Error", str(e))


def evaluate_expression(expression):
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }
    stack = []
    current_number = ""
    current_operator = "+"
    for char in expression:
        if char in operators:
            stack.append(float(current_number))
            current_number = ""
            current_operator = char
        else:
            current_number += char
    stack.append(float(current_number))
    result = 0
    for i in range(0, len(stack), 2):
        number = stack[i]
        if i > 0:
            operator_fn = operators[current_operator]
            result = operator_fn(result, number)
        else:
            result = number
    return result


root = tk.Tk()
root.title("Calculator")
style = ttk.Style()
style.theme_use("alt")
style.configure(
    "TButton", padding=(6, 6), relief="flat", background="#ccc", height=50, width=50
)

entry = ttk.Entry(root, width=16, font=("Arial", 24))
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

    def action(x=button):
        if x != "=":
            on_button_click(x)
        else:
            on_calculate()

    ttk.Button(root, text=button, width=5, style="TButton", command=action).grid(
        row=row, column=col, rowspan=2
    )
    col += 1
    if col > 3:
        col = 0
        row += 2

ttk.Button(root, text="C", width=5, style="TButton", command=on_clear).grid(
    row=row, column=col
)

root.mainloop()
