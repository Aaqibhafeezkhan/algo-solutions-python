<<<<<<< HEAD:practice_problem_solutions (2026)/practice202.py
# HackerRank - Migratory Birds

from collections import Counter
def migratoryBirds(arr):
    c = Counter(arr)
    return min(arr, key=lambda x: (-c[x], x))

print(migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4])) # 3
print(migratoryBirds([1, 4, 4, 4, 5, 3]))                # 4
print(migratoryBirds([1, 1, 2, 2, 3]))                   # 1
=======
# Number of Steps to Reduce a Number to Zero

class Solution(object):
    def numberOfSteps(self, num):
        count = 0

        while num > 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            count += 1
        return count

s = Solution()
print(s.numberOfSteps(14)) # 6
print(s.numberOfSteps(8)) # 4
print(s.numberOfSteps(123)) # 12
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice202.py
