<<<<<<< HEAD:practice_problem_solutions (2026)/practice148.py
# Number of 1 Bits

class Solution(object):
    def hammingWeight(self, n):
        return bin(n)[2:].count('1')

s = Solution()
print(s.hammingWeight(11)) # 3
print(s.hammingWeight(128)) # 1
print(s.hammingWeight(4294967293)) # 31
=======
# Permutation Difference between Two Strings

class Solution(object):
    def findPermutationDifference(self, s, t):
        res = 0
        for i in range(len(s)):
            res += abs(i - t.index(s[i]))
        return res
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice148.py
