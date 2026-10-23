<<<<<<< HEAD:practice_problem_solutions (2026)/practice279.py
# Combinations

from itertools import combinations
class Solution(object):
    def combine(self, n, k):
        return [list(arr) for arr in combinations(range(1, n + 1), k)]

s = Solution()
print(s.combine(4, 2)) # [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
print(s.combine(4, 3)) # [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
print(s.combine(4, 1)) # [[1], [2], [3], [4]]
print(s.combine(1, 1)) # [[1]]
=======
# HackerRank - Calendar Module

from datetime import datetime
d = list(map(int, input().split()))
da = datetime(day=d[1], month=d[0], year=d[-1])
print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][da.weekday()])
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice279.py
