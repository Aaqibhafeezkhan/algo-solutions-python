<<<<<<< HEAD:practice_problem_solutions (2026)/practice151.py
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
=======
# Count Asterisks

class Solution(object):
    def countAsterisks(self, s):
        if '*' not in s:
            return 0
        elif '|' not in s:
            return s.count('*')
        
        had_f = False
        count = 0
        for c in s:
            if c == '|':
                had_f = not had_f
            elif not had_f and c == '*':
                count += 1
        return count
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice151.py
