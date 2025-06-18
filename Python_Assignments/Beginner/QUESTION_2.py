#(Question 2). Write a program that accepts a string as input from the user and calculates the number of digits and letters.
# Input: Hello123
# Output: Alphabets: 5 & Number : 3

user_input = input("Enter a string: ")

letters = 0
digits = 0

for char in user_input:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1

print(f"Alphabets: {letters} & Number: {digits}")