<<<<<<< HEAD:practice_problem_solutions (2026)/practice316.py
# CodeWars - Return pyramids

def pyramid(n):
    
    sp = n - 1
    mid = 0
    
    res = []
    
    for _ in range(n - 1):
        
        res.append(' ' * sp + '/' + ' ' * mid + '\\')
        
        sp -= 1
        mid += 2
    
    res.append('/' + '_' * mid + '\\')
    
    return '\n'.join(res) + '\n'

print(pyramid(1)) # '/\\\n'
print(pyramid(2)) # ' /\\\n/__\\\n'
print(pyramid(3)) # '  /\\\n /  \\\n/____\\\n'
=======
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
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice316.py
