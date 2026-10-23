<<<<<<< HEAD:practice_problem_solutions (2026)/practice258.py
# Rank Transform of an Array

class Solution(object):
    def arrayRankTransform(self, arr):
        rank = dict(zip(sorted(set(arr)), range(1, len(set(arr))+1)))
        return [rank[x] for x in arr]

s = Solution()
print(s.arrayRankTransform([37,12,28,9,100,56,80,5,12])) # [5,3,4,2,8,6,7,1,3]
print(s.arrayRankTransform([40,10,20,30]))               # [4,1,2,3]
print(s.arrayRankTransform([100,100,100]))               # [1,1,1]
=======
# Count of Matches in Tournament

class Solution(object):
    def numberOfMatches(self, n):
        count = 0
        while n > 1:
            if n % 2 == 0:
                count += n // 2
                n //= 2
            else:
                count += (n - 1) // 2
                n = (n - 1) // 2 + 1
        return count
    
s = Solution()
print(s.numberOfMatches(n=7)) # 6
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice258.py
