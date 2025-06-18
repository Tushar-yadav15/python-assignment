# (Question 12). Write a Python program to reverse a number using
#  a while loop.
#      Sample Input: num = 12345
#      Sample Output: revnum = 54321

num = int(input("Enter a number: "))

revnum = 0

while num > 0:
    digit = num % 10       
    revnum = revnum * 10 + digit  
    num = num // 10          

print("Reversed number:", revnum)