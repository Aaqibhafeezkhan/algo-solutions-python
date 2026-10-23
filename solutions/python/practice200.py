<<<<<<< HEAD:practice_problem_solutions (2026)/practice200.py

def punctuation_score(msg):
    punc = {
        '.': 2,
        '!': 5,
        '?': 10
    }

    t = 0
    i = 0

    while i < len(msg):
        if msg[i] in punc:
            cur = i

            while cur < len(msg) and msg[cur] in punc:
                cur += 1

            group_score = sum(punc[c] for c in msg[i:cur])

            t += group_score * (i + 1)

            i = cur
        else:
            i += 1

    return t

print(punctuation_score("I like to write multiple sentences. Don't you? Come on!")) # 805
print(punctuation_score("Hello world!"))                                            # 60
=======
# Create Target Array in the Given Order

class Solution(object):
    def createTargetArray(self, nums, index):
        target = []
        for i, num in zip(index, nums):
            target.insert(i, num)
        return target

s = Solution()
print(s.createTargetArray([0,1,2,3,4], [0,1,2,2,1]))  # [0,4,1,3,2]
print(s.createTargetArray([1,2,3,4,0], [0,1,2,3,0]))  # [0,1,2,3,4]
print(s.createTargetArray([1], [0]))  # [1]
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice200.py
