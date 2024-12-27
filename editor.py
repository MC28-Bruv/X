import tkinter as tk
from tkinter import filedialog, messagebox
import os

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".x", filetypes=[("Binary files", "*.x"), ("All files", "*.*")])
    if not file_path:
        return

    with open(file_path, 'r', encoding='utf-8') as file:
        binary_content = file.read()

    readable_content = binary_to_string(binary_content)
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, readable_content)
    root.title(f"Editing {os.path.basename(file_path)}")

    global current_file
    current_file = file_path

def save_file():
    if current_file:
        readable_content = text_area.get(1.0, tk.END)
        binary_content = string_to_binary(readable_content)
        with open(current_file, 'w', encoding='utf-8') as file:
            file.write(binary_content)
        messagebox.showinfo("Saved", f"File saved as {current_file}")
    else:
        save_as_file()

def save_as_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".x", filetypes=[("Binary files", "*.x"), ("All files", "*.*")])
    if not file_path:
        return

    readable_content = text_area.get(1.0, tk.END)
    binary_content = string_to_binary(readable_content)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(binary_content)
    root.title(f"Editing {os.path.basename(file_path)}")
    messagebox.showinfo("Saved", f"File saved as {file_path}")

    global current_file
    current_file = file_path

def save_as_txt():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if not file_path:
        return

    readable_content = text_area.get(1.0, tk.END)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(readable_content)
    root.title(f"Editing {os.path.basename(file_path)}")
    messagebox.showinfo("Saved", f"File saved as {file_path}")

def string_to_binary(s):
    return ' '.join(format(ord(char), '08b') for char in s)

def binary_to_string(b):
    return ''.join(chr(int(char, 2)) for char in b.split())

def create_window():
    global root, text_area, current_file
    current_file = None

    root = tk.Tk()
    root.title("Binary File Editor")

    text_area = tk.Text(root, wrap='word', font=('Arial', 12))
    text_area.pack(expand=1, fill='both')

    menu_bar = tk.Menu(root)
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Open", command=open_file)
    file_menu.add_command(label="Save", command=save_file)
    file_menu.add_command(label="Save As", command=save_as_file)
    file_menu.add_command(label="Save As .txt", command=save_as_txt)
    menu_bar.add_cascade(label="File", menu=file_menu)

    root.config(menu=menu_bar)

    root.mainloop()

if __name__ == "__main__":
    create_window()
