<<<<<<< HEAD:practice_problem_solutions (2026)/practice294.py
# Find Pivot Index

class Solution(object):
    def pivotIndex(self, nums):        
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        
        return -1

s = Solution()
print(s.pivotIndex([1,7,3,6,5,6]))   # 3
print(s.pivotIndex([2,1,-1]))        # 0
print(s.pivotIndex([1,2,3]))         # -1
=======
# Minimum Distance to the Target Element

class Solution(object):
    def getMinDistance(self, nums, target, start):
        closest = float('inf')
        for i in range(start, len(nums)):
            if nums[i] == target:
                closest = min(closest, abs(start - i))
        
        for i in range(start, -1, -1):
            if nums[i] == target:
                closest = min(closest, abs(start - i))
        
        return closest
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice294.py
