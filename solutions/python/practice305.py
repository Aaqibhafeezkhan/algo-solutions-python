<<<<<<< HEAD:practice_problem_solutions (2026)/practice305.py
# CodeWars - Next bigger number with the same digits

def next_bigger(n):
    digits = list(str(n))
    
    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i+1]:
        i -= 1
    
    if i == -1:
        return -1
    
    j = len(digits) - 1
    while j >= 0 and digits[j] <= digits[i]:
        j -= 1
    
    digits[i], digits[j] = digits[j], digits[i]
    
    digits[i+1:] = sorted(digits[i+1:])
    
    return int(''.join(digits))

print(next_bigger(2017))    # 2071
print(next_bigger(144))     # 414
print(next_bigger(12))      # 21
=======
# Sorting the Sentence

class Solution:
    def sortSentence(self, s: str) -> str:
        return ' '.join(word[:-1] for word in sorted(s.split(), key=lambda x: x[-1]))
    
s = Solution()
print(s.sortSentence("is2 sentence4 This1 a3")) # "This is a sentence"
print(s.sortSentence("Myself2 Me1 I4 and3"))    # "Me Myself and I"
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice305.py
