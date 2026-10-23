<<<<<<< HEAD:practice_problem_solutions (2026)/practice315.py
# Sort Array by Increasing Frequency

from collections import Counter
class Solution(object):
    def frequencySort(self, nums):
        c = Counter(nums)
        return sorted(nums, key=lambda x: (c[x], -x))



s = Solution()
print(s.frequencySort([-1,1,-6,4,5,-6,1,4,1])) # [5,-1,4,4,-6,-6,1,1,1]
print(s.frequencySort([1,1,2,2,2,3])) # [3,1,1,2,2,2]
print(s.frequencySort([2,3,1,3,2]))   # [1,3,3,2,2]
=======
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
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice315.py
