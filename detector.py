import os

from signatures import MAGIC_NUMBERS

def detect_file_type(file_path):
    try:
        with open(file_path, 'rb') as f:
            header = f.read(16)
            for sig, file_type in MAGIC_NUMBERS.items():
                if header.startswith(sig):
                    return file_type
            return "unknown"
    except:
        return "error"

def get_category(file_type):
    categories = {
        "jpg": "Image",
        "png": "Image",
        "gif": "Image",
        "mp3": "Media",
        "mp4": "Media",
        "pdf": "Document",
        "zip": "Archive",
        "rar": "Archive",
        "exe": "Executable",
        "elf": "Executable"
    }
    return categories.get(file_type, "Unknown")

def get_hex_dump(file_path, size=64):
    try:
        with open(file_path, "rb") as file:
            data = file.read(min(size, 512))  # max 512 bytes

        hex_data = " ".join(f"{byte:02x}" for byte in data)
        return hex_data
    except Exception as e:
        return f"Error reading file: {e}"
