<<<<<<< HEAD:practice_problem_solutions (2026)/practice269.py
# GeeksforGeeks - Longest Palindrome in a String

# My Sol;
class Solution:
    def longestPalindrome(self, s):
        palindrome = ""
        n = len(s)
        for i in range(n - 1):
            right = n
            while right > i:
                temp = s[i:right]
                if temp == temp[::-1] and len(temp) > len(palindrome):
                    palindrome = temp
                    break
                right -= 1
        return palindrome

# Optimized Sol;
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        res = ""
        
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        for i in range(len(s)):
            p1 = expand(i, i)
            if len(p1) > len(res):
                res = p1

            p2 = expand(i, i + 1)
            if len(p2) > len(res):
                res = p2
                
        return res

s = Solution()
print(s.longestPalindrome("bswrhxboawtdfqggqfdtwyypwnssnwpyyaobxhrwsb")) # wtdfqggqfdtw
print(s.longestPalindrome("aaaabbaa"))                                   # aabbaa
print(s.longestPalindrome("ababa"))                                      # ababa
=======
# Self Dividing Numbers

class Solution(object):
    def selfDividingNumbers(self, left, right):
        arr = []
        for i in range(left, right + 1):
            digits = list(map(int, list(str(i))))
            score = len(digits)
            for d in digits:
                if d == 0:
                    break
                if i % d == 0:
                    score -= 1
            if score == 0:
                arr.append(i)
        return arr
    
s = Solution()
print(s.selfDividingNumbers(1, 22))  # [1,2,3,4,5,6,7,8,9,11,12,15,22]
print(s.selfDividingNumbers(47, 85)) # [48,55,66,77]
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice269.py
