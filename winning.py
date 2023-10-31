def battle_numbers(number):
    # Check for invalid input
    if not isinstance(number, int) or number < 0:
        return "Invalid input."

    number_str = str(number)
    result = []
    length = len(number_str)
    
    if length % 2 == 1:
        result.append(number_str[0])  # Add the lone digit if the length is odd
        number_str = number_str[1:]
    
    for i in range(0, len(number_str), 2):
        digit1 = int(number_str[i])
        digit2 = int(number_str[i + 1])
        
        if digit1 > digit2:
            result.append(str(digit1))
        elif digit1 < digit2:
            result.append(str(digit2))
    
    if not result:
        return "No winners."
    
    return f"Battle outcome: {int(''.join(result))}"

# Read the input
input_number = input("Enter a non-negative integer: ")

try:
    input_number = int(input_number)
    result = battle_numbers(input_number)
    print(result)
except ValueError:
    print("Invalid input.")
