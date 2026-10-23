<<<<<<< HEAD:practice_problem_solutions (2026)/practice280.py
# Valid Number

class Solution(object):
    def isNumber(self, s):
        try:
            float(s)
            s = s.lower().strip()
            return 'inf' not in s and 'nan' not in s
        except:
            return False
    
s = Solution()
print(s.isNumber(" 005047e+6")) # True
print(s.isNumber("95a54e53"))   # False
print(s.isNumber("+6e-1"))      # True
print(s.isNumber("."))          # False
=======
# HackerRank - Write a function

def is_leap(year):
    leap = False
    
    if year % 4 == 0 and (year % 100 != 0 or year % 400  == 0):
        leap = True
    
    return leap
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice280.py
