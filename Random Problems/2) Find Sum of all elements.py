"""Question:

Input: [3, 7, 1, 9, 2]  
Output: 22

Constraints:
The array will contain at least one element.
You cannot use the built-in sum() function."""

Solution:

def find_sum(arr):
    total = 0  
    for num in arr:  
        total += num  
    return total
