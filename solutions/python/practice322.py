<<<<<<< HEAD:practice_problem_solutions (2026)/practice322.py
# CodeChum - Longest subarray with sum k

ln, r = map(int, input().split())
arr = list(map(int, input().split()[:ln]))

seen = []

for i in range(ln - 1):
    for j in range(i + 1, ln):
        if sum(arr[i:j+1]) == r:
            seen.append(len(arr[i:j+1]))

print(min(seen) if seen else 0)
=======
from collections import Counter
class Solution:
    def isPossibleToSplit(self, nums) -> bool:
        num = Counter(nums)
        for n in num.values():
            if n > 2:
                return False
        return True

s = Solution()
print(s.isPossibleToSplit([1,1,2,2,3,4]))     # True
print(s.isPossibleToSplit([1,1,2,2,2,2,3,4])) # False
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice322.py
