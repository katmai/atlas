distance = 5.4
hours = 2
minutes = 14

total_minutes = hours * 60 + minutes
total_hours = total_minutes / 60
speed = distance / total_hours

print(f"Average speed required to complete the trail in the given duration: {speed:.2f} miles per hour")