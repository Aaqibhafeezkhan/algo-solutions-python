<<<<<<< HEAD:practice_problem_solutions (2026)/practice166.py
# Maximum Subarray Sum

def maxSub(arr):
    cur_sum = []
    seen = []
    for i in range(len(arr)):
        if seen and seen[-1] > arr[i]:
            cur_sum.append(seen)
            seen = [arr[i]]
            continue
        seen.append(arr[i])
    if seen:
        cur_sum.append(seen)
    return max(cur_sum, key=lambda x: sum(x)) if cur_sum else []

print(maxSub([1,2,3,4,5,6,7,8,9]))
print(maxSub([1,2,3,4,1,7,8,9]))
=======
# Subarray Sum Equals K

# My Solution
class Solution(object):
    def subarraySum(self, nums, k):
        count = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                if sum(nums[i:j]) == k:
                    count += 1
        
        return count

# Accepted Solution
class Solution(object):
    def subarraySum(self, nums, k):
        res = 0
        curSum = 0
        prefixSums = {0 : 1}

        for n in nums:
            curSum += n
            diff = curSum - k

            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)
        return res

s = Solution()
print(s.subarraySum([1, 1, 1], 2))   # Expected: 2
# print(s.subarraySum([1, 2, 3], 3))   # Expected: 2
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice166.py
