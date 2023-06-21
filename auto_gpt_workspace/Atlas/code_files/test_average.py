from average import calculate_average

# Test case 1
numbers = [1, 2, 3, 4, 5]
expected_output = 3.0
output = calculate_average(numbers)
assert output == expected_output, f'Error: expected {expected_output}, but got {output}'

# Test case 2
numbers = [0, 0, 0, 0, 0]
expected_output = 0.0
output = calculate_average(numbers)
assert output == expected_output, f'Error: expected {expected_output}, but got {output}'

# Test case 3
numbers = [2, 4, 6, 8, 10]
expected_output = 6.0
output = calculate_average(numbers)
assert output == expected_output, f'Error: expected {expected_output}, but got {output}'

print('All tests passed!')