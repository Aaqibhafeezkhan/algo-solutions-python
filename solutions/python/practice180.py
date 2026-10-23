<<<<<<< HEAD:practice_problem_solutions (2026)/practice180.py
# GeeksForGeeks - Kadane's Algorithm

class Solution:
    def maxSubarraySum(self, arr):
        cur_max = float('-inf')
        cur_sum = 0
        for i in range(len(arr)):
            cur_sum += arr[i]
            cur_max = max(cur_max, cur_sum)
            if cur_sum < 0:
                cur_sum = 0
        return cur_max
    
s = Solution()
print(s.maxSubarraySum([-3, -2, -6, -1, -7, -4]))
=======
# Truncate Sentence

class Solution(object):
    def truncateSentence(self, s, k):
        return " ".join(s.split()[:k])
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice180.py
