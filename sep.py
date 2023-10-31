# Read the array length
n = int(input())

employeeNames = []
positiveValues = []
negativeValues = []

# Read the array values and categorize them
for _ in range(n):
    value = input()
    if value.isnumeric() or (value[0] == '-' and value[1:].isnumeric()):
        value = int(value)
        if value >= 0:
            positiveValues.append(value)
        else:
            negativeValues.append(value)
    else:
        employeeNames.append(value)

# Print the results
print("Employee Names")
for name in employeeNames:
    print(name)

print("Positive Values")
for value in positiveValues:
    print(value)

print("Negative Values")
for value in negativeValues:
    print(value)
