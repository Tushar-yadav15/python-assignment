#1.Turn the following snippet into a function:
# numbers = [1,2,3,4,5]
# squares = []
# for n in numbers:
# squares.append(n*n)
# print(squares)
# Requirements:
# Create def compute_squares(nums: list[int]) -> list[int]
# Add a docstring and type hints
# Call it on at least two different lists

from typing import List

def compute_squares(nums: List[int]) -> List[int]:
    """
    Takes a list of integers and returns a list of their squares.

    Args:
        nums (List[int]): A list of integers.

    Returns:
        List[int]: A list of squared integers.
    """
    squares = []
    for n in nums:
        squares.append(n * n)
    return squares

print(compute_squares([1, 2, 3, 4, 5]))  
print(compute_squares([6, 7, 8]))