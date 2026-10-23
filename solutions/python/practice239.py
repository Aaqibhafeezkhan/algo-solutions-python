<<<<<<< HEAD:practice_problem_solutions (2026)/practice239.py
# Maximum 69 Number

class Solution:
    def maximum69Number (self, num: int) -> int:
        cur = list(str(num))
        maxs = num
        for i in range(len(cur)):
            if cur[i] == '6':
                cur[i] = '9'
                maxs = max(maxs, int(''.join(cur)))
                cur[i] = '6'
        return maxs

s = Solution()
print(s.maximum69Number(9999)) # 9999
print(s.maximum69Number(9996)) # 9999
print(s.maximum69Number(9669)) # 9969
=======
# py.checkio - Monkey Typing

def count_words(text: str, words: set) -> int:
    w = dict(zip([w.lower()for w in words], [0] * len(words)))
    print(w)
    for txt in text.lower().split():
        for word in words:
            if word.lower() in txt:
                w[word.lower()] += 1
    count = 0
    for k,v in w.items():
        if v > 0: count += 1
    return count

print(count_words("Bananas, give me bananas!!!", {"banana", "bananas"})) # 2
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice239.py
