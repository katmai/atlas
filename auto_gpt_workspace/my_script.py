import os

for file in os.listdir():
    if file.endswith('.txt'):
        with open(file, 'r') as f:
            print(f.read())