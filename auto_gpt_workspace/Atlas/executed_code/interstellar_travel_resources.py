import math

# Constants
SPEED_OF_LIGHT = 299792458 # m/s
DISTANCE_TO_CENTER_OF_MILKY_WAY = 25000 # ly
SPEED_OF_INTERSTELLAR_TRAVEL = 0.1 * SPEED_OF_LIGHT # m/s

# Calculate the time required to travel to the center of the Milky Way
time = (DISTANCE_TO_CENTER_OF_MILKY_WAY * 9.461e+15) / SPEED_OF_INTERSTELLAR_TRAVEL

# Calculate the amount of resources needed for the mission
mass_of_spacecraft = 1000 # kg
distance_per_day = SPEED_OF_INTERSTELLAR_TRAVEL * 86400 # m/day
fuel_efficiency = 0.1 # kg/m
fuel_required = distance_per_day * fuel_efficiency
duration_of_mission = time * 365 # days
resources_required = fuel_required * duration_of_mission * mass_of_spacecraft

# Print the estimated amount of resources required for the mission\print(f'The estimated amount of resources required for a hypothetical interstellar travel mission is approximately {math.ceil(resources_required):,} kg of fuel.')