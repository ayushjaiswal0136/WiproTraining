'''Do the following in a single program using built-in functions
Take a list of numbers as input and print the largest and smallest numbers in the list.
Take a string as input and print the length of the string.
Take a list of names as input and print the list in alphabetical order.
Take a list of numbers as input and print the total sum of the elements in the list.
Takes a string as input and print the string in uppercase. '''

numbers = [21,3,43,92,67,31,78]
names = ["Jonas","Martha","Ulrich","Claudia","Noah"]
text = "Everything"

# Largest and Smallest
print("List of numbers:",numbers)
print("Largest:",max(numbers))
print("Smallest:",min(numbers))

# Length of a string
print("\nString",text)
print("Length:",len(text))

# Alphabetical Order
print("\nNames",names)
print("Sorted:",sorted(names))

# Sum of elements
print("\nSum of numbers:",sum(numbers))

# Uppercase
print("\nUppercase:",text.upper())