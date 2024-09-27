def write_to_file(text, filename="translated_text.txt"):
    if text == "":  # Do not write empty text
        return
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
