<<<<<<< HEAD:practice_problem_solutions (2026)/practice153.py
n = int(input())
c = {}
alpha = list(range(2005, 2023)) + [2003, 2004]

for i in range(n):
    name = input()
    ch = alpha[ord(name[0].lower()) - 97]
    c[ch] = c.get(ch, 0) + 1
sor = sorted(c.items(), key=lambda x: x[1])

res = []

for key, val in sor:
    res.append(f"{key} {val}")

print('\n'.join(res))
=======
class Solution(object):
    def decodeMessage(self, key, message):
        
        coord = {}
        alpha = 0
        for c in key.replace(' ', ''):
            if not coord:
                coord[c] = chr(97 + alpha)
                alpha += 1
            elif c not in coord:
                coord[c] = chr(97 + alpha)
                alpha += 1
        
        res = ""
        for c in message:
            if c == ' ':
                res += ' '
            else:
                res += coord[c]
        return res

s = Solution()
print(s.decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"))
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice153.py
