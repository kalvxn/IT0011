def get_number(prompt):
    while True:
        value = input(prompt)
        if value.replace('.', '', 1).isdigit():
            return float(value)
        else:
            print("Invalid Input. Please enter a number.")

def find_highest_number():
    while True:
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        num3 = get_number("Enter third number: ")

        if num1 >= num2 and num1 >= num3:
            highest = num1
        elif num2 >= num1 and num2 >= num3:
            highest = num2
        else:
            highest = num3

        print("The highest number is:", highest)

        again = input("Do you want to input again? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thank u!")
            break

find_highest_number()