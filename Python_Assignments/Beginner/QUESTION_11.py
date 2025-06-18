# (Question 11). Write a Python program to calculate the sum of digits of a given number until the sum becomes a single-digit number.
#      Sample Input: num = 987
#      Sample Output: Sum_of_digits = 24,
#      Again compute the sum of digits so that it can be reduced
#  to
#      on single digit.
#      Final Output: 6

def sum_of_digits(num):
    while num >= 10:
        total = 0
        while num > 0:
            total += num % 10
            num //= 10
        print(f"Intermediate sum: {total}")
        num = total
    return num

num = int(input("Enter a number: "))

final_sum = sum_of_digits(num)
print("Final Output:", final_sum)