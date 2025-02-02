def count_characters(input_string):
    vowels = "aeiouAEIOU"
    num_vowels = 0
    num_consonants = 0
    num_spaces = 0
    num_others = 0

    for char in input_string:
        if char.isalpha():
            if char in vowels:
                num_vowels += 1
            else:
                num_consonants += 1
        elif char.isspace():
            num_spaces += 1
        else:
            num_others += 1

    return num_vowels, num_consonants, num_spaces, num_others

while True:
    input_string = input("Enter a string (or type 'exit' to quit): ")
    if input_string.lower() == 'exit':
        break
    vowels, consonants, spaces, others = count_characters(input_string)
    print(f"Vowels: {vowels}, Consonants: {consonants}, Spaces: {spaces}, Others: {others}")