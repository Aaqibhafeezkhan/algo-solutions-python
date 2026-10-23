<<<<<<< HEAD:practice_problem_solutions (2026)/practice250.py
# Jump Game II

class Solution:
    def jumps(self, arr):
        jump = 0
        
        l, r = 0, 0
        
        while r < len(arr) - 1:
            farthest = 0
            
            for i in range(l, r + 1):
                farthest = max(farthest, i + arr[i])
            
            l = r
            r = farthest
            
            jump += 1
        
        return jump

s = Solution()
print(s.jumps([2, 3, 1, 1, 4])) # 2
print(s.jumps([2, 3, 0, 1, 4])) # 2
print(s.jumps([0])) # 0
=======
# Palindrome Check (Ignoring Non-Alphanumeric)

def palindrome(s):
    new_s = ''.join(c for c in s if c.isalpha() or c.isdigit()).lower()
    return new_s == new_s[::-1]

print(palindrome("A man, a plan, a canal: Panama"))
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice250.py
