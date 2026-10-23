<<<<<<< HEAD:practice_problem_solutions (2026)/practice184.py
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
=======
# Minimum Bit Flips to Convert Number

class Solution(object):
    def minBitFlips(self, start, goal):
        start_b = format(start, 'b')
        goal_b = format(goal, 'b')

        max_len = len(max([start_b, goal_b], key=len))

        start_b = start_b.zfill(max_len)
        goal_b = goal_b.zfill(max_len)

        print(start_b, goal_b)

        i = 0
        flip_count = 0
        while i < max_len:
            if start_b[i] != goal_b[i]:
                flip_count += 1
            i += 1
        return flip_count
    
s = Solution()
print(s.minBitFlips(10, 7)) # 3
print(s.minBitFlips(3, 4)) # 3
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice184.py
