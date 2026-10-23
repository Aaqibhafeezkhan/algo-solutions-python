<<<<<<< HEAD:practice_problem_solutions (2026)/practice259.py
# Geeksforgeeks - Sort 0s, 1s and 2s

class Solution:
    def sort012(self, arr):
        arr[:] = [0] * arr.count(0) + [1] * arr.count(1) + [2] * arr.count(2)
        return arr

s = Solution()
print(s.sort012([0, 1, 2, 0, 1, 2])) # [0, 0, 1, 1, 2, 2]
print(s.sort012([2, 1, 0, 2, 1, 0])) # [0, 0, 1, 1, 2, 2]
print(s.sort012([0, 0, 1, 1, 2, 2])) # [0, 0, 1, 1, 2, 2]
=======
# Decompress Run-Length Encoded List

class Solution(object):
    def decompressRLElist(self, nums):
        arr = []

        for i in range(0, len(nums) - 1, 2):
            arr.extend([nums[i + 1]] * nums[i])
        
        return arr
    
s = Solution()
print(s.decompressRLElist([1,2,3,4])) # [2,4,4,4]
print(s.decompressRLElist([1,1,2,3])) # [1,3,3]
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice259.py
