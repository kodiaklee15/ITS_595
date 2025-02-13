def reverse_string(input_string) -> str:
    reversed_string = ""
    for char in input_string:
        reversed_string = char + reversed_string
    return reversed_string