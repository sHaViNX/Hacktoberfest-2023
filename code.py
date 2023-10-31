# Read input values
laptop_name = input()
year = input()
generation = int(input())
processor = input()

# Convert the generation number to its textual representation
if generation % 10 == 1 and generation % 100 != 11:
    generation_str = str(generation) + "st Generation"
elif generation % 10 == 2 and generation % 100 != 12:
    generation_str = str(generation) + "nd Generation"
elif generation % 10 == 3 and generation % 100 != 13:
    generation_str = str(generation) + "rd Generation"
else:
    generation_str = str(generation) + "th Generation"

# Print the output
print("Laptop Name : " + laptop_name)
print("Year : " + year)
print("Generation : " + generation_str)
print("Processor : " + processor)
