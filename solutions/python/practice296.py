<<<<<<< HEAD:practice_problem_solutions (2026)/practice296.py
# CodeWars - Valid Phone Number

import re
def valid_phone_number(phone_number):
    return bool(re.match(r"\([0-9]{3}\)\s[0-9]{3}-[0-9]{4}$", phone_number))

print(valid_phone_number("(123) 456-7890abc")) # False
print(valid_phone_number("(123) 456-7890"))    # True
print(valid_phone_number("abc(123) 456-7890")) # False
=======
# HackerRank - Utopian Tree

def utopianTree(n):
    res = 1
    for i in range(n):
        if i % 2 == 0:
            res *= 2
        else:
            res += 1
    return res
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice296.py
