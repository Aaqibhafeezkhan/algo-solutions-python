<<<<<<< HEAD:practice_problem_solutions (2026)/practice146.py
# CodeWars - Consonant Value

def solve(s):
    words = []
    temp = ""
    for c in s:
        if c in 'aeiou':
            words.append(temp)
            temp = ""
        else:
            temp += c
    words.append(temp)
    maxt = float('-inf')
    for word in words:
        maxt = max(maxt, sum(ord(c) - 96 for c in word))
    return maxt

print(solve("cozy"), 51)
print(solve("xyzzy"), 126)
print(solve("zodiac"), 26)
print(solve("chruschtschov"), 80)
print(solve("khrushchev"), 38)
print(solve("strength"), 57)
print(solve("catchphrase"), 73)
print(solve("twelfthstreet"), 103)
print(solve("mischtschenkoana"), 80)
=======
# Left and Right Sum Differences

class Solution(object):
    def leftRightDifference(self, nums):
        if len(nums) == 1:
            return [0]
        
        left = [0]
        right = []

        for i in range(len(nums) - 1):
            left.append(sum(nums[:i+1]))
        
        for i in range(1, len(nums)):
            right.append(sum(nums[i:]))
        right.append(0)

        res = []

        for i, j in zip(left, right):
            res.append(abs(i - j))
        
        return res

s = Solution()
print(s.leftRightDifference([10,4,8,3]))
print(s.leftRightDifference([1]))
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice146.py
