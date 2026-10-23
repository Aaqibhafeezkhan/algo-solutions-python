<<<<<<< HEAD:practice_problem_solutions (2026)/practice240.py
# Sum of Values at Indices With K Set Bits

class Solution:
    def sumIndicesWithKSetBits(self, nums, k) -> int:
        return sum(num for i, num in enumerate(nums) if bin(i)[2:].count('1') == k)

s = Solution()
print(s.sumIndicesWithKSetBits([5,10,1,5,2], 1)) # 13
print(s.sumIndicesWithKSetBits([4,3,2,1], 2))    # 1
=======
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
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice240.py
