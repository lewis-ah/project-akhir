import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


def on_button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def on_equal_click():
    try:
        current = entry.get()
        result = eval(current)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def on_clear_click():
    entry.delete(0, tk.END)

root = ttk.Window(themename='superhero')
root.title("Kalkulator Menarik")
root.geometry("400x500")

frame = ttk.Frame(root, padding=10)
frame.pack(fill=BOTH, expand=True)

entry = ttk.Entry(frame, width=30, font=('Arial', 24), justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0
for button in buttons:
    if button == '=':
        btn = ttk.Button(frame, text=button, bootstyle=SUCCESS, command=on_equal_click)
    elif button == 'C':
        btn = ttk.Button(frame, text=button, bootstyle=DANGER, command=on_clear_click)
    else:
        btn = ttk.Button(frame, text=button, command=lambda b=button: on_button_click(b))
    
    btn.grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

btn_clear = ttk.Button(frame, text='C', bootstyle=DANGER, command=on_clear_click)
btn_clear.grid(row=row_val, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

for i in range(5):
    frame.grid_rowconfigure(i, weight=1)
    frame.grid_columnconfigure(i, weight=1)

root.mainloop()
