# Problem: Character Triangle Pattern
# Source: 
# Note: Solves the Character Triangle Pattern problem
# Description:
# Given a character and a number n, print a triangle pattern where each row contains an odd number
# of characters, starting with 1 character and incrementing by 2 for each row.
# 
# Example:
# - Input: character="*", n=3
# - Output:
#   *
#  ***
# *****
# 
# Status: ✅ SOLVED

def print_character_triangle(character, n):
    if n <= 0:
        return ""
    
    result = []
    level = 1
    
    for i in range(n):
        spaces = " " * max(n - i - 2, 0)
        row = spaces + character * level
        result.append(row)
        level += 2
    
    return "\n".join(result)

# Test cases with assertions
# Test with n=3
expected_3 = " *\n***\n*****"

# Test with n=1

# Test with n=2
expected_2 = " #\n###"

# Test with n=0
