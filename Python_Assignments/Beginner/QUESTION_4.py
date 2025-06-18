# (Question 4). Write a Python program to find the sum of all odd  numbers between two given numbers. 
# Start = 1, stop = 10
# Sum of odd numbers: 25


start = int(input("Enter the starting number: "))
stop = int(input("Enter the stopping number: "))

odd_sum = 0

for num in range(start, stop + 1):
    if num % 2 != 0:
        odd_sum += num

print(f"Sum of odd numbers: {odd_sum}")