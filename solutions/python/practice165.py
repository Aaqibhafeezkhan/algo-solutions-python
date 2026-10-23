<<<<<<< HEAD:practice_problem_solutions (2026)/practice165.py
# Palindrome Check (Ignoring Non-Alphanumeric)

def palindrome(s):
    new_s = ''.join(c for c in s if c.isalpha() or c.isdigit()).lower()
    return new_s == new_s[::-1]

print(palindrome("A man, a plan, a canal: Panama"))
=======
# Remove Outermost Parentheses

class Solution(object):
    def removeOuterParentheses(self, s):
        
        seen = []
        ans = ""
        for c in s:
            if not seen:
                seen.append(c)
            elif c == '(':
                seen.append(c)
                ans += c
            elif c == ')':
                seen.pop()
                if seen:
                    ans += c
        
        return ans
    
s = Solution()
print(s.removeOuterParentheses("(()())(())"))           # Expected: "()()()"
print(s.removeOuterParentheses("(()())(())(()(()))"))   # Expected: "()()()()(())"
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice165.py
