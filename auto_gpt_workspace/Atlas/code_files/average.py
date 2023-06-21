def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

numbers = [1, 2, 3, 4, 5]
average = calculate_average(numbers)
print('The average of the numbers is:', average)