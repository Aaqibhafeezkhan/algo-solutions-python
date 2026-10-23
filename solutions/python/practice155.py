<<<<<<< HEAD:practice_problem_solutions (2026)/practice155.py
# Decode XORed Array

class Solution(object):
    def decode(self, encoded, first):
        decoded = [first]
        for i in range(len(encoded)):
            decoded.append(encoded[i] ^ decoded[-1])
        return decoded

s = Solution()
print(s.decode([1,2,3], 1))   # [1,0,2,1]
print(s.decode([6,2,7,3], 4)) # [4,2,0,7,4]
=======
# Running Sum of 1d Array

class Solution(object):
    def runningSum(self, nums):
        res = []
        for i in range(1, len(nums) + 1):
            print(nums[:i])
            res.append(sum(nums[:i]))
        return res
    
s = Solution()
print(s.runningSum([1, 2, 3, 4])) # [1,3,6,10]
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice155.py
