<<<<<<< HEAD:practice_problem_solutions (2026)/practice188.py
# Distribute Candies

class Solution(object):
    def distributeCandies(self, candyType):
        cd = len(set(candyType))
        ce = len(candyType) // 2
        return min(ce, cd)

s = Solution()
print(s.distributeCandies([1,1,2,2,3,3])) # 3
print(s.distributeCandies([1,1,2,3]))     # 2
print(s.distributeCandies([6,6,6,6]))     # 1
=======
# Maximum Number of Words Found in Sentences

class Solution(object):
    def mostWordsFound(self, sentences):
        cur_max = float('-inf')
        for words in sentences:
            cur_max = max(cur_max, len(words.split()))
        return cur_max

s = Solution()
print(s.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"])) # 6
print(s.mostWordsFound(["please wait", "continue to fight", "continue to win"])) # 3
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice188.py
