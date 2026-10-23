<<<<<<< HEAD:practice_problem_solutions (2026)/practice154.py
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
=======
# How Many Numbers Are Smaller Than the Current Number

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        res = [0] * len(nums)
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] > nums[j]:
                    res[i] += 1
        return res

s = Solution()
print(s.smallerNumbersThanCurrent([8, 1, 2, 2, 3])) # [4, 0, 1, 1, 3]
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice154.py
