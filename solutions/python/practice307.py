<<<<<<< HEAD:practice_problem_solutions (2026)/practice307.py
# CodeWars - Most frequently used words in a text

from collections import Counter
import re

def top_3_words(text):
    
    words = re.findall(r"[a-z']+", text.lower())
    
    words = [w for w in words if any(c.isalpha() for c in w)]
    
    return [word for word, _ in Counter(words).most_common(3)]

print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")) # ['e', 'ddd', 'aa']
print(top_3_words("  //wont won't won't "))                                 # ["won't", "wont"]
print(top_3_words(" ''' , e   .. "))                                        # ["e"]
=======
# Find Missing Elements

class Solution:
    def findMissingElements(self, nums):
        complete = list(range(min(nums), max(nums) + 1))
        arr = []
        for num in complete:
            if num not in nums:
                arr.append(num)
        return arr

s = Solution()
print(s.findMissingElements([1,4,2,5])) # [3]
print(s.findMissingElements([5,1]))     # [2,3,4]
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice307.py
