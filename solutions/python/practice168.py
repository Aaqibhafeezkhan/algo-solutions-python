<<<<<<< HEAD:practice_problem_solutions (2026)/practice168.py
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
=======
# XOR Operation in an Array

class Solution(object):
    def xorOperation(self, n, start):
        arr = []
        i = 0
        while len(arr) < n:
            arr.append(start + 2 * i)
            i += 1
        xor = arr[0]
        for i in arr[1:]:
            xor ^= i
        return xor

s = Solution()
print(s.xorOperation(5, 0)) # 8
print(s.xorOperation(4, 3)) # 8
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice168.py
