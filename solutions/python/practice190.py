<<<<<<< HEAD:practice_problem_solutions (2026)/practice190.py
# Uncommon Words from Two Sentences

from collections import Counter
class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        arr = []
        c = Counter((s1 + " " + s2).split())
        for key, val in c.items():
            if val == 1:
                arr.append(key)
        return arr

s = Solution()
print(s.uncommonFromSentences("this apple is sweet", "this apple is sour")) # ["sweet","sour"]
print(s.uncommonFromSentences("apple apple", "banana"))                     # ["banana"]
=======
# Find Indices of Stable Mountains

class Solution(object):
    def stableMountains(self, height, threshold):
        
        stables = []
        n = len(height)
        for i in range(1, n):
            if height[i - 1] > threshold and height[i] > 0:
                stables.append(i)
        return stables

s = Solution()
print(s.stableMountains([1,2,3,4,5], 2)) # [3, 4]
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice190.py
