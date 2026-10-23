<<<<<<< HEAD:practice_problem_solutions (2026)/practice254.py
# Maximum Subarray

class Solution:
    def maxSubArray(self, nums) -> int:
        max_sub = nums[0]
        cur_sum = 0

        for n in nums:
            if cur_sum < 0:
                cur_sum = 0
            
            cur_sum += n
            max_sub = max(max_sub, cur_sum)
        
        return max_sub

s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # 6
print(s.maxSubArray([5,4,-1,7,8]))            # 23
print(s.maxSubArray([1]))                     # 1
=======
# Number of Islands

def islands(arr):
    island = 0

    for ar in arr:
        for num in ar:
            if num == '1':
                island += 1
    
    return island


print(islands([['1','0','1'], ['1','1','1'], ['1','0','1']]))
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice254.py
