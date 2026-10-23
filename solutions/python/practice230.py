<<<<<<< HEAD:practice_problem_solutions (2026)/practice230.py
# Group Anagrams

class Solution:
    def groupAnagrams(self, strs):
        groups = {}
        for w in strs:
            srt = ''.join(sorted(w))
            if groups and srt in groups:
                groups[srt].append(w)
            else:
                groups[srt] = [w]
        return list(groups.values())

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        groups = defaultdict(list)
        for w in strs:
            srt = ''.join(sorted(w))
            groups[srt].append(w)
        return list(groups.values())

s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])) # [["eat","tea","ate"],["tan","nat"],["bat"]]
print(s.groupAnagrams(["a"]))                                 # [["a"]]
print(s.groupAnagrams([""]))                                  # [[""]]
=======
# CodeWars - N-th Fibonacci

def nth_fib(n):
    a, b = 0, 1
    count = 2
    if n < 2:
        return [a, b][n - 1]
    while count < n:
        a, b = b, a + b
        count += 1
    return b

print(nth_fib(1)) # 0
print(nth_fib(2)) # 1
print(nth_fib(100)) # 218922995834555169026
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice230.py
