<<<<<<< HEAD:practice_problem_solutions (2026)/practice186.py
# CodeWars - Meeting

def meeting(s):
    names = []
    for name in s.split(';'):
        first, last = name.upper().split(':')
        names.append([last, first])
    
    return ''.join(f"({last}, {name})" for last, name in sorted(names, key=lambda x: (x[0], x[1])))
=======
# Sum of Multiples

class Solution(object):
    def sumOfMultiples(self, n):
        return sum(num for num in range(1, n + 1) if num % 3 == 0 or num % 5 == 0 or num % 7 == 0)
    
s = Solution()
print(s.sumOfMultiples(7)) # 21
print(s.sumOfMultiples(10)) # 40
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice186.py
