<<<<<<< HEAD:practice_problem_solutions (2026)/practice319.py
# CodeWars - Sum of Pairs

def sum_pairs(ints, s):
    
    seen = set()
    
    for num in ints:
        
        target = s - num
        
        if target in seen:
            return [target, num]
        
        seen.add(num)

print(sum_pairs([1, -2, 3, 0, -6, 1], -6)) # [0, -6]
print(sum_pairs([1, 4, 8, 7, 3, 15], 8))   # [1, 7]
print(sum_pairs([20, -13, 40], -7))        # None
=======
# Find Numbers with Even Number of Digits

from math import log10, ceil
class Solution:
    def findNumbers(self, nums) -> int:
        return sum([1 for num in nums if ceil(log10(num + 1)) % 2 == 0])
    
s = Solution()
print(s.findNumbers([12,345,2,6,7896]))  # 2
print(s.findNumbers([555,901,482,1771])) # 1
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice319.py
