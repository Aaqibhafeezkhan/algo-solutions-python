<<<<<<< HEAD:practice_problem_solutions (2026)/practice287.py
# Geeksforgeeks: Power of 2

class Solution:
    def isPowerofTwo(self, n):
        return bin(n).count('1') == 1

s = Solution()
print(s.isPowerofTwo(1))  # True
print(s.isPowerofTwo(8))  # True
print(s.isPowerofTwo(98)) # False
=======
# HackerRank - Migratory Birds

from collections import Counter
def migratoryBirds(arr):
    c = Counter(arr)
    return min(arr, key=lambda x: (-c[x], x))

print(migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4])) # 3
print(migratoryBirds([1, 4, 4, 4, 5, 3]))                # 4
print(migratoryBirds([1, 1, 2, 2, 3]))                   # 1
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice287.py
