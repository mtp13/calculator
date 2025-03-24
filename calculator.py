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


def calculate():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        operation = operation_var.get()

        if operation == "Add":
            result = add(a, b)
        elif operation == "Subtract":
            result = subtract(a, b)
        elif operation == "Multiply":
            result = multiply(a, b)
        elif operation == "Divide":
            result = divide(a, b)
        else:
            result = "Error: Invalid operation"

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")


# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create and place the widgets
tk.Label(root, text="First Number:").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Second Number:").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

operation_var = tk.StringVar(root)
operation_var.set("Add")
operations_menu = tk.OptionMenu(
    root, operation_var, "Add", "Subtract", "Multiply", "Divide"
)
operations_menu.grid(row=2, column=0, columnspan=2)

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2)

# Run the application
root.mainloop()
