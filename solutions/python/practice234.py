<<<<<<< HEAD:practice_problem_solutions (2026)/practice234.py
# Find Numbers with Even Number of Digits

from math import log10, ceil
class Solution:
    def findNumbers(self, nums) -> int:
        return sum([1 for num in nums if ceil(log10(num + 1)) % 2 == 0])
    
s = Solution()
print(s.findNumbers([12,345,2,6,7896]))  # 2
print(s.findNumbers([555,901,482,1771])) # 1
=======
# Smallest Range I

class Solution(object):
    def smallestRangeI(self, nums, k):
        maxt = max(nums) - k
        mint = min(nums) + k
        diff = maxt - mint
        return diff if diff > 0 else 0

s = Solution()
print(s.smallestRangeI([1], 0)) # 0
print(s.smallestRangeI([0, 10], 2)) # 6
print(s.smallestRangeI([1, 3, 6], 3)) # 0
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice234.py
