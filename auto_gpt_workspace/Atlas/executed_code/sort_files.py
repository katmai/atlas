import os

file_types = {}

for file in os.listdir():
    if os.path.isfile(file):
        file_type = file.split('.')[-1]
        if file_type not in file_types:
            file_types[file_type] = []
        file_types[file_type].append(file)

with open('file_types.txt', 'w') as f:
    for file_type in sorted(file_types.keys()):
        f.write(f'{file_type.upper()} FILES:\n')
        for file in file_types[file_type]:
            f.write(f'    {file}\n')

print('File types sorted and output to file.')