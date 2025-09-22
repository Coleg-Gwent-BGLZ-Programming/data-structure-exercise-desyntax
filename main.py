# main.py - Personal Data Manager

# TODO: Step 1 - Prompt the user to enter their name and age
# Hint: Use input() and store the values in variables
name = input("whats ur name: ")
age = int(input("how much old do you have: "))

# TODO: Step 2 - Ask the user to enter 3 hobbies
# Hint: Use a loop to collect hobbies and store them in a list
hobbies = []
for i in range(0, 2):
  hobbies.append(str(input(f"tell me one of your hobbies (3x times): ")))

# TODO: Step 3 - Create a dictionary to store the user's name, age, and hobbies
# Hint: Use key-value pairs to organize the data
user = {"name" = name, "age" = age, "hobbies" = (hobbies)}

# TODO: Step 4 - Display the user's information using formatted strings
# Hint: Use f-strings to format the output
print(f"you are {name} and you have {age} years of old.")
print(f"your hobbies include: {hobbies[0]}, {hobbies[1]}, and {hobbies[2]}\n")

# TODO: Step 5 - Convert the hobbies list into a set to remove duplicates
# Hint: Use the set() function
set(hobbies)

# TODO: Step 6 - Calculate the user's birth year and store it in a tuple with the current year
# Hint: Use subtraction and a tuple to store both years
birthYear = 2025 - age
years = (2025, birthYear)

# TODO: Step 7 - Create a function that takes the dictionary and returns a summary string
# Hint: Use string concatenation or f-strings inside the function
print("from what you've said,")

# TODO: Step 8 - Call the function and print the summary
# Hint: Pass the dictionary to the function and print the result
