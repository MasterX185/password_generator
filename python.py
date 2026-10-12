import string
import secrets

import tkinter as tk
from tkinter import messagebox

def gen_pw():
    try:
        length = int(length_entry.get())
        if length < 1:
            raise ValueError("Password length must be at least 1.")
    except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))
            return
        
    characters = ""
    if var_include_numbers.get():
        characters += string.digits
    if var_include_special.get():
        characters += string.punctuation
    if var_include_letters.get():
        characters += string.ascii_letters
    
    if not characters:
        messagebox.showerror("Invalid Input", "No character types selected.")
        return
    
    password = ''.join(secrets.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    
def copy_pw():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard.")
    else:
        messagebox.showwarning("No Password", "No password to copy.")
        

root = tk.Tk()
root.title("Password Generator")
root.geometry("500x300")
root.resizable(True, True)

frame_length = tk.Frame(root)
frame_length.pack(pady=5)
label_length = tk.Label(frame_length, text="Password Length:")
label_length.pack(side=tk.LEFT)
length_entry = tk.Entry(frame_length, width=5)
length_entry.pack(side=tk.LEFT)

var_include_numbers = tk.BooleanVar(value=True)
var_include_special = tk.BooleanVar(value=True)
var_include_letters = tk.BooleanVar(value=True)
frame_options = tk.Frame(root)
frame_options.pack(pady=5)
check_numbers = tk.Checkbutton(frame_options, text="Include Numbers", variable=var_include_numbers)
check_numbers.pack(side=tk.LEFT)
check_special = tk.Checkbutton(frame_options, text="Include Special Characters", variable=var_include_special)
check_special.pack(side=tk.LEFT)
check_letters = tk.Checkbutton(frame_options, text="Include Letters", variable=var_include_letters)
check_letters.pack(side=tk.LEFT)

btn_generate = tk.Button(root, text="Generate Password", command=gen_pw)
btn_generate.pack(pady=10)
password_entry = tk.Entry(root, width=30)
password_entry.pack(pady=5)
btn_copy = tk.Button(root, text="Copy to Clipboard", command=copy_pw)
btn_copy.pack(pady=10)  

root.mainloop()
