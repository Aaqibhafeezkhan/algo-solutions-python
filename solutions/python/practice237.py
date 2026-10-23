<<<<<<< HEAD:practice_problem_solutions (2026)/practice237.py
from collections import Counter
class Solution:
    def isPossibleToSplit(self, nums) -> bool:
        num = Counter(nums)
        for n in num.values():
            if n > 2:
                return False
        return True

s = Solution()
print(s.isPossibleToSplit([1,1,2,2,3,4]))     # True
print(s.isPossibleToSplit([1,1,2,2,2,2,3,4])) # False
=======
# Clear Digits

class Solution(object):
    def clearDigits(self, s):

        seen = []
        for letter in s:
            if not seen and letter.isalpha():
                seen.append(letter)
            elif letter.isalpha():
                seen.append(letter)
            else:
                if seen:
                    seen.pop()
                
        return ''.join(seen)

s = Solution()
print(s.clearDigits("abc")) # "abc"
print(s.clearDigits("cb34")) # ""
print(s.clearDigits("1234")) # ""
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice237.py
