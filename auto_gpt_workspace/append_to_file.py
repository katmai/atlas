def append_to_file(filename, text):
    with open(filename, 'a') as f:
        f.write(text)
