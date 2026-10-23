<<<<<<< HEAD:practice_problem_solutions (2026)/practice162.py
def zeros(n):
    count = 0
    while n:
        n //= 5
        count += n
    return count
    
print(zeros(6))          # 1
print(zeros(30))         # 7
print(zeros(1000000000)) # 249999998
=======
# Find Closest Person

class Solution(object):
    def findClosest(self, x, y, z):
        if abs(x - z) == abs(y - z):
            return 0
        elif abs(x - z) > abs(y - z):
            return 2
        else:
            return 1

s = Solution()
print(s.findClosest(1, 2, 3))
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice162.py
