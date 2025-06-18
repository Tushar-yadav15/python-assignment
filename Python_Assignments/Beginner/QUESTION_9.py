# (Question 9). Write a Python program to count the frequency of each element in a list.
#   Input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
#   Frequency count: {1: 2, 2: 3, 3: 1, 4: 2, 5: 1}


input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
frequency = {}

for item in input_list:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print("Frequency count:", frequency)