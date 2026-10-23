<<<<<<< HEAD:practice_problem_solutions (2026)/practice158.py
# Height Checker

class Solution(object):
    def heightChecker(self, heights):
        srt = sorted(heights)
        count = 0
        for x, y in zip(heights, srt):
            if x != y:
                count += 1
        return count

s = Solution()
print(s.heightChecker([1,1,4,2,1,3])) # 3
print(s.heightChecker([5,1,2,3,4]))   # 5
print(s.heightChecker([1,2,3,4,5]))   # 0
=======
# Count Number of Maximum Bitwise-OR Subsets

class Solution(object):
    def countMaxOrSubsets(self, nums):
        cur = [[]]
        for i in range(len(nums)):
            for j in range(len(cur)):
                cur.append(cur[j] + [nums[i]])
        
        max_or = 0
        for num in nums:
            max_or |= num

        count = 0
        for arr in cur:
            or_sum = 0
            for num in arr:
                or_sum |= num
            if or_sum == max_or:
                count += 1

        return count

s = Solution()
print(s.countMaxOrSubsets([3, 1]))  # Output: 2
print(s.countMaxOrSubsets([2, 2, 2]))  # Output: 7
print(s.countMaxOrSubsets([3, 2, 1, 5]))  # Output: 6
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice158.py
