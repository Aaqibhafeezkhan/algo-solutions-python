<<<<<<< HEAD:practice_problem_solutions (2026)/practice242.py
# Minimum Sum of Four Digit Number After Splitting Digits

class Solution:
    def minimumSum(self, num: int) -> int:
        temp = sorted(str(num))
        n1, n2 = f"{temp[0]}{temp[3]}", f"{temp[1]}{temp[2]}"
        return int(n1) + int(n2)

s = Solution()
print(s.minimumSum(2932)) # 52
print(s.minimumSum(4009)) # 13
print(s.minimumSum(2687)) # 95
=======
# Count Digit Appearances

class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        count = 0
        for num in map(str, nums):
            count += num.count(str(digit))
        return count

s = Solution()
print(s.countDigitOccurrences([12,54,32,22], 2)) # 4
print(s.countDigitOccurrences([3], 1))           # 0
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice242.py
