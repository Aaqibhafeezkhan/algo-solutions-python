<<<<<<< HEAD:practice_problem_solutions (2026)/practice285.py
class Solution:
    def twoSum(self, arr, target):
        arr.sort()
        left = 0
        right = len(arr) - 1
        
        while left < right:
            res = arr[left] + arr[right]
            if res == target:
                return True
            
            if res > target:
                right -= 1
            else:
                left += 1
        
        return False

s = Solution()
print(s.twoSum([1, 2, 3, 4, 5], 9))  # True
print(s.twoSum([1, 2, 3, 4, 5], 10)) # False
print(s.twoSum([1, 2, 3, 4, 5], 5))  # True
=======

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
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice285.py
