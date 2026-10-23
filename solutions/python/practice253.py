<<<<<<< HEAD:practice_problem_solutions (2026)/practice253.py
# Merge Intervals

class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])

        res = []

        temp = []
        for l, r in intervals:
            if not temp:
                temp = [l, r]
            elif l > temp[1]:
                res.append(temp)
                temp = [l, r]
            elif r > temp[1]:
                temp[1] = r
        
        if temp:
            res.append(temp)
        
        return res

s = Solution()
print(s.merge([[1,3],[2,7],[8,10],[15,18],[17,23],[3,4],[4,5],[10,14],[11,12],[13,14]])) # [[1,7],[8,14],[15,23]]
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))                                             # [[1,6],[8,10],[15,18]]
print(s.merge([[1,4],[4,5]]))                                                            # [[1,5]]
=======
# Longest Substring Without Repeating Characters

def substring(s):
    words = []
    cur = ""
    for c in s:
        if c.lower() in cur:
            words.append(cur)
            cur = ""
            continue
        cur += c
    if cur:
        words.append(cur)
    
    return max(words, key=len) if words else ""

print(substring("abcaba"))
print(substring(""))
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice253.py
