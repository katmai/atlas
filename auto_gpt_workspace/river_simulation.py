# Python script to simulate the flow of a river

import random

water_level = 0

while True:
    # Generate a random number between -1 and 1
    flow_rate = random.uniform(-1, 1)
    # Update the water level based on the flow rate
    water_level += flow_rate
    # Print the water level
    print(water_level)
