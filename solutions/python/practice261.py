<<<<<<< HEAD:practice_problem_solutions (2026)/practice261.py
# Geeksforgeeks - Count Even Letters

from collections import Counter
class Solution:
    def count(self, s):
        alp = Counter(s)
        return sum(1 for k in alp.values() if k % 2 == 0)

s = Solution()
print(s.count("abcde"))    # 0
print(s.count("aabbcde"))  # 2
print(s.count("aabbccde")) # 3
=======
# Count Number of Pairs With Absolute Difference K

class Solution(object):
    def countKDifference(self, nums, k):
        count = 0
        for i in range(len(nums)  - 1):
            for j in range(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    count += 1
        return count
    
s = Solution()
print(s.countKDifference([1,2,2,1], 1))   # 4
print(s.countKDifference([1,3], 3))       # 0
print(s.countKDifference([3,2,1,5,4], 2)) # 3
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice261.py
