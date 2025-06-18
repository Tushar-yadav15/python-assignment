# (Question 10). Write a Python program to reverse the order of words in a given sentence.
#  Input_sentence = “Hello, World! Welcome to Python programming.”
#  Output after reverse = “programming. Python to Welcome World! Hello,”

input_sentence = "Hello, World! Welcome to Python programming."

reversed_words = input_sentence.split()[::-1]

reversed_sentence = ' '.join(reversed_words)

print("Output after reverse:", reversed_sentence)