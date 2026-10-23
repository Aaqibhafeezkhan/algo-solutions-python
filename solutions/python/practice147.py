<<<<<<< HEAD:practice_problem_solutions (2026)/practice147.py
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
=======
# Number of Employees Who Met the Target

class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        return sum(1 for i in hours if i >= target)

>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice147.py
