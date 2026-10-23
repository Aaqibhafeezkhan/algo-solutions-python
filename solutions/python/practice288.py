<<<<<<< HEAD:practice_problem_solutions (2026)/practice288.py
# Geeksforgeeks -Square Root

class Solution:
    def floorSqrt(self, n): 
        from math import floor
        num = n ** 0.5
        if num == int(num):
            return int(num)
        return floor(num)

s = Solution()
print(s.floorSqrt(4))  # 2
print(s.floorSqrt(11)) # 3
print(s.floorSqrt(25)) # 5
=======
# HackerRank - Counting Valleys

def countingValleys(steps, path):
    
    cur = 0
    val = 0
    for c in path:
        if cur < 0 and c == 'U':
            if cur + 1 == 0:
                val += 1
                cur += 1
                continue
        if c == 'U': cur += 1
        else: cur -= 1
    return val

print(countingValleys(8, "UDDDUDUU")) # 1
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice288.py
