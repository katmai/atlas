# Python script to automate a repetitive task

import os

# Define the directory to search for files
path = '/path/to/directory'

# Define the file extension to search for
extension = '.txt'

# Get a list of all files in the directory
files = os.listdir(path)

# Filter the list of files to only include files with the specified extension
files = [file for file in files if file.endswith(extension)]

# Loop through the list of files and perform the repetitive task
for file in files:
    # Perform the repetitive task on the file
    # ...
    pass
