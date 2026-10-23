<<<<<<< HEAD:practice_problem_solutions (2026)/practice220.py
# Sorting the Sentence

class Solution:
    def sortSentence(self, s: str) -> str:
        return ' '.join(word[:-1] for word in sorted(s.split(), key=lambda x: x[-1]))
    
s = Solution()
print(s.sortSentence("is2 sentence4 This1 a3")) # "This is a sentence"
print(s.sortSentence("Myself2 Me1 I4 and3"))    # "Me Myself and I"
=======
# CodeWars - Highest Rank Number in an Array

from collections import Counter
def highest_rank(arr):
    return max(set(arr), key=lambda x: (Counter(arr)[x], x))

print(highest_rank([1, 2, 3, 2, 1, 3, 3])) # 3
print(highest_rank([1, 1, 2, 2, 3])) # 2
print(highest_rank([1, 2, 3, 4, 5])) # 5
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice220.py
