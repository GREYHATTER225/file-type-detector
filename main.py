import tkinter as tk
from tkinter import filedialog
import os

from detector import detect_file_type, get_category, get_hex_dump

def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        real_type = detect_file_type(file_path)
        ext = os.path.splitext(file_path)[1].replace(".", "").lower()
        category = get_category(real_type)
        hex_data = get_hex_dump(file_path, size=64)

        result = f"""File: {os.path.basename(file_path)}

Real: {real_type}
Ext: {ext}
Category: {category}
Status: {"✅ Safe" if real_type == ext else "⚠️ Suspicious"}

HEX:
{hex_data[:120]}...
"""
        label.config(text=result)

# UI
app = tk.Tk()
app.title("File Type Detector")

btn = tk.Button(app, text="Select File", command=select_file)
btn.pack(pady=20)

label = tk.Label(app, text="", justify="left")
label.pack(pady=20)

app.mainloop()