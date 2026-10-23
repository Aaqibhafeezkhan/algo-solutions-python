<<<<<<< HEAD:practice_problem_solutions (2026)/practice232.py
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
=======
# CodeWars - Validate Credit Card Number

def validate(n):
    digits = str(n)
    res = []
    count = 0
    l = len(digits)
    for i in range(l):
        if i % 2 == 0 and l % 2 == 0:
            res.append(int(digits[i]) * 2)
        elif i % 2 != 0 and l % 2 != 0:
            res.append(int(digits[i]) * 2)
        else:
            res.append(int(digits[i]))

    for i, digit in enumerate(res):
        temp = str(digit)
        while len(temp) > 1:
            temp = str(sum(int(c) for c in temp))
        res[i] = int(temp)
    return sum(res) % 10 == 0

print(validate(1230)) # True
print(validate(1714)) # False
print(validate(2121)) # True
print(validate(891)) # False
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice232.py
