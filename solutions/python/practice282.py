<<<<<<< HEAD:practice_problem_solutions (2026)/practice282.py
class Solution(object):
    def reverseBits(self, n):
        return int(f"{n:032b}"[::-1], 2)

s = Solution()
print(s.reverseBits(43261596))   # 964176192
print(s.reverseBits(2147483644)) # 1073741822
=======
# HackerRank - Number Line Jumps

def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        return 'YES' if x1 == x2 else 'NO'

    diff_pos = x2 - x1
    diff_vel = v1 - v2

    if diff_vel == 0:
        return 'NO'

    if diff_pos % diff_vel == 0 and diff_pos / diff_vel >= 0:
        return 'YES'

    return 'NO'
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice282.py
