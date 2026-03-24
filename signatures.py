MAGIC_NUMBERS = {
    # Images
    b"\xff\xd8\xff": "jpg",
    b"\x89PNG": "png",
    b"GIF87a": "gif",
    b"GIF89a": "gif",

    # Documents
    b"%PDF": "pdf",

    # Executables
    b"MZ": "exe",

    # Archives
    b"PK": "zip",      # zip/jar/docx/xlsx
    b"Rar!": "rar",

    # Media
    b"ID3": "mp3",     # mp3
    b"\x00\x00\x00\x18ftyp": "mp4",  # mp4 (may vary)

    # Others
    b"\x7fELF": "elf",  # linux executable
    
    # Additional
    b"PK\x03\x04": "zip_docx",  # better zip/docx
    b"\xd0\xcf\x11\xe0": "doc",  # MS Office doc
    b"#!": "script",
    b"<html": "html",
    b"\x1f\x8b": "gz"  # gzip
}
