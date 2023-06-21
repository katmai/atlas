# Import the random module
import random

# Define the characters to use in the password
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-='

# Define the length of the password
length = 12

# Generate the password
password = ''.join(random.choice(characters) for i in range(length))

# Print the password to the console
print(password)
