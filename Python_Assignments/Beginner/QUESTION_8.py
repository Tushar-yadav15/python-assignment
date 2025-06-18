# (Question  8). Write a Python program to calculate the LCM (Least Common Multiple) of two numbers.
#  number1 = 12, number2 = 18
#  LCM of 12 and 18 are: 36 


def find_lcm(a, b):
    
    if a > b:
        greater = a
    else:
        greater = b

    while True:
        if greater % a == 0 and greater % b == 0:
            lcm = greater
            break
        greater += 1

    return lcm

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"LCM of {num1} and {num2} is: {find_lcm(num1, num2)}")