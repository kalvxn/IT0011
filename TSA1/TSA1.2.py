def sum_of_digits(input_string):
    total = 0
    for char in input_string:
        if char.isdigit():
            total += int(char)
    return total

while True:
    input_string = input("Enter a string with digits (or type 'exit' to quit): ")
    if input_string.lower() == 'exit':
        break
    result = sum_of_digits(input_string)
    print(f"Sum of digits: {result}")