<<<<<<< HEAD:practice_problem_solutions (2026)/practice236.py
# Trim Trailing Vowels

class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        return s.rstrip('aeiou')
    
s = Solution()
print(s.trimTrailingVowels("a"))    # ""
print(s.trimTrailingVowels("ba"))   # "b"
print(s.trimTrailingVowels("idea")) # "id"
=======
# Sum of Variable Length Subarrays

class Solution(object):
    def subarraySum(self, nums):
        arr = []

        for i in range(len(nums)):
            s = max(0, i - nums[i])
            arr.append(sum(nums[s:i + 1]))

        return sum(arr)

s = Solution()
print(s.subarraySum([2,3,1]))   # 11
print(s.subarraySum([3,1,1,2])) # 13
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice236.py
