import tkinter as tk
from tkinter import messagebox
import math

class BiswajitCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Biswajit Calculator")
        self.root.geometry("300x400")
        self.root.configure(bg='#f0f0f0')
        self.root.resizable(False, False)  

        self.background_frame = tk.Frame(root, bg='#FFDEE9')
        self.background_frame.place(relwidth=1, relheight=1)

        self.entry = tk.Entry(self.background_frame, width=20, font=('Arial', 24), bd=5, relief=tk.RAISED, bg='#ffffff')
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

        button_style = {'bg': '#4CAF50', 'fg': '#FFFFFF', 'font': ('Arial', 14), 'relief': tk.RAISED, 'bd': 3}

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('√', 5, 1), ('^', 5, 2), ('%', 5, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.background_frame, text=text, width=5, height=2, **button_style,
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')

        for i in range(6):
            self.background_frame.grid_rowconfigure(i, weight=1)
            self.background_frame.grid_columnconfigure(i, weight=1)

    def on_button_click(self, text):
        current_entry = self.entry.get()

        if text == '=':
            try:
                if '√' in current_entry:
                    sqrt_value = math.sqrt(float(current_entry.replace('√', '')))
                    self.entry.delete(0, tk.END)
                    self.entry.insert(tk.END, str(sqrt_value))
                else:
                    result = eval(current_entry)
                    self.entry.delete(0, tk.END)
                    self.entry.insert(tk.END, str(result))
            except ZeroDivisionError:
                messagebox.showerror("Error", "Cannot divide by zero!")
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
        elif text == 'C':
            self.entry.delete(0, tk.END)
        elif text == '^':
            self.entry.insert(tk.END, '**')
        elif text == '%':
            try:
                result = eval(current_entry) / 100
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
        else:
            self.entry.insert(tk.END, text)

def main():
    root = tk.Tk()
    app = BiswajitCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
