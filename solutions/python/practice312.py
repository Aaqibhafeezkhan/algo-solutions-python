<<<<<<< HEAD:practice_problem_solutions (2026)/practice312.py
# py.checkio - Common Words

def checkio(line1: str, line2: str) -> str:
    l1, l2 = line1.split(','), line2.split(',')
    return ','.join(sorted([word for word in l1 if word in l2]))

print(checkio("one,two,three", "four,three,two,one")) # "one,three,two"
print(checkio("one,two,three", "four,five,six"))      # ""
print(checkio("hello,world", "hello,earth"))          # "hello"
=======
# Multiply Strings

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return f"{int(num1) * int(num2)}"
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice312.py
