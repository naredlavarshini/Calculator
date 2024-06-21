import tkinter as tk
from tkinter import messagebox
import math

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Simple Calculator")
        self.geometry("400x600")
        self.configure(bg='lightgray')

        self.create_widgets()

    def create_widgets(self):
        self.result_var = tk.StringVar()
        self.memory = 0

        # Entry widget for displaying results
        result_entry = tk.Entry(self, textvariable=self.result_var, font=('Arial', 24), bd=10, insertwidth=2, width=14,
                                borderwidth=4)
        result_entry.grid(row=0, column=0, columnspan=4)

        # Button layout
        buttons = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', 'M+',
            '1', '2', '3', '-', 'M-',
            '0', '.', '=', '+', 'MR',
            'sqrt', 'exp', 'MC'
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            tk.Button(self, text=button, padx=20, pady=20, font=('Arial', 18), command=action).grid(row=row_val,
                                                                                                   column=col_val)
            col_val += 1
            if col_val > 4:
                col_val = 0
                row_val += 1

    def on_button_click(self, char):
        if char in '0123456789.':
            self.result_var.set(self.result_var.get() + char)
        elif char == 'C':
            self.result_var.set('')
        elif char in '+-*/':
            self.result_var.set(self.result_var.get() + ' ' + char + ' ')
        elif char == '=':
            try:
                expression = self.result_var.get()
                self.result_var.set(eval(expression))
            except ZeroDivisionError:
                messagebox.showerror("Error", "Cannot divide by zero")
                self.result_var.set('')
            except Exception as e:
                messagebox.showerror("Error", str(e))
                self.result_var.set('')
        elif char == 'sqrt':
            try:
                value = float(self.result_var.get())
                self.result_var.set(math.sqrt(value))
            except ValueError:
                messagebox.showerror("Error", "Invalid input for square root")
        elif char == 'exp':
            try:
                base, exp = map(float, self.result_var.get().split())
                self.result_var.set(math.pow(base, exp))
            except Exception as e:
                messagebox.showerror("Error", str(e))
        elif char == 'M+':
            try:
                self.memory += float(self.result_var.get())
                self.result_var.set('')
            except ValueError:
                messagebox.showerror("Error", "Invalid input for memory addition")
        elif char == 'M-':
            try:
                self.memory -= float(self.result_var.get())
                self.result_var.set('')
            except ValueError:
                messagebox.showerror("Error", "Invalid input for memory subtraction")
        elif char == 'MR':
            self.result_var.set(self.memory)
        elif char == 'MC':
            self.memory = 0
            self.result_var.set('')

if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()
