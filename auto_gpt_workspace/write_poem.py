# Import the random module
import random

# Define the lines of the poem
lines = [
    "The river's banks, a lush green scene,",
    "A place of peace, where one can dream,",
    "The trees that line its winding course,",
    "A natural wonder, a powerful force.",
    "",
    "The river's journey, a never-ending tale,",
    "As it flows through the land, without fail,",
    "A symbol of life, of hope and of grace,",
    "A river's beauty, impossible to replace.",
    "",
    "The river's path, a journey of its own,",
    "A constant motion, a rhythm unknown,",
    "A force of nature, that will never cease,",
    "A river's magic, a true masterpiece."
]

# Shuffle the lines to create a unique poem
random.shuffle(lines)

# Write the poem to a file
with open('final_poem.txt', 'w') as f:
    for line in lines:
        f.write(line + '\n')
