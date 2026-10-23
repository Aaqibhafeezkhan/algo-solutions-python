<<<<<<< HEAD:practice_problem_solutions (2026)/practice255.py
# Find the Difference

class Solution(object):
    def findTheDifference(self, s, t):
        return chr(sum([ord(c) for c in t]) - sum([ord(c) for c in s]))

s = Solution()
print(s.findTheDifference("abcd", "abcde")) # e
print(s.findTheDifference("", "y"))          # y
print(s.findTheDifference("a", "aa"))       # a
=======
# Coin Change (Minimum Coins)

def change(n):
    coins = [50, 20, 10, 5, 1]
    change = []
    while n > 0:
        for coin in coins:
            if coin <= n:
                n -= coin
                change.append(coin)
                break
    return change


print(change(25))
print(change(15))
print(change(45))
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice255.py
