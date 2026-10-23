<<<<<<< HEAD:practice_problem_solutions (2026)/practice317.py
# CodeWars - Area of a Square

from math import pi
def square_area(A):
    return round((4 * A ** 2) / pi ** 2, 2)

print(square_area(14.05)) # 80.0
print(square_area(2))     # 1.62
print(square_area(0))     # 0.0
=======
# Wildcard Matching

# Other sol
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        ar = [[False] * (n + 1) for _ in range(m + 1)]

        ar[0][0] = True

        for j in range(1, n + 1):
            if p[j - 1] == '*':
                ar[0][j] = ar[0][j - 1]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    ar[i][j] = ar[i - 1][j] or ar[i][j - 1]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    ar[i][j] = ar[i - 1][j - 1]
        
        return ar[m][n]
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice317.py
