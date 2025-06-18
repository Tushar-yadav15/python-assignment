# (Question 3). Write a Python program to input marks for five subjects Physics, Chemistry, Biology, Mathematics, and Computer.
#  Calculate the percentage and grade
#  according to the following:
#  Percentage >= 90% : Grade A
#  Percentage >= 80% : Grade B
#  Percentage >= 70% : Grade C
#  Percentage >= 60% : Grade D
#  Percentage >= 40% : Grade E
#  Percentage < 40% : Grade F


physics = float(input("Enter marks for Physics: "))
chemistry = float(input("Enter marks for Chemistry: "))
biology = float(input("Enter marks for Biology: "))
mathematics = float(input("Enter marks for Mathematics: "))
computer = float(input("Enter marks for Computer: "))

total_marks = physics + chemistry + biology + mathematics + computer
percentage = (total_marks / 500) * 100

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
elif percentage >= 40:
    grade = "E"
else:
    grade = "F"

print(f"\nTotal Marks: {total_marks}/500")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")