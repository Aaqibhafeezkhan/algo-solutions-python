<<<<<<< HEAD:practice_problem_solutions (2026)/practice231.py
# Count and Say

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        prev = self.countAndSay(n - 1)
        res = ""
        c = 1

        for i in range(len(prev)):
            if i + 1 < len(prev) and prev[i] == prev[i + 1]:
                c += 1
            else:
                res += str(c) + prev[i]
                c = 1
        
        return res
    
s = Solution()
print(s.countAndSay(1)) # "1"
print(s.countAndSay(4)) # "1211"
=======
# CodeWars - Consonant Value

def solve(s):
    words = []
    temp = ""
    for c in s:
        if c in 'aeiou':
            words.append(temp)
            temp = ""
        else:
            temp += c
    words.append(temp)
    maxt = float('-inf')
    for word in words:
        maxt = max(maxt, sum(ord(c) - 96 for c in word))
    return maxt

print(solve("cozy"), 51)
print(solve("xyzzy"), 126)
print(solve("zodiac"), 26)
print(solve("chruschtschov"), 80)
print(solve("khrushchev"), 38)
print(solve("strength"), 57)
print(solve("catchphrase"), 73)
print(solve("twelfthstreet"), 103)
print(solve("mischtschenkoana"), 80)
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice231.py
