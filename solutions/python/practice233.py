<<<<<<< HEAD:practice_problem_solutions (2026)/practice233.py
# Furthest Point From Origin

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        return abs(moves.count('R') - moves.count('L')) + moves.count('_')
    
s = Solution()
print(s.furthestDistanceFromOrigin("L_RL__R")) # 3
print(s.furthestDistanceFromOrigin("_R__LL_")) # 5
print(s.furthestDistanceFromOrigin("_______")) # 7
=======
# Number of 1 Bits

class Solution(object):
    def hammingWeight(self, n):
        return bin(n)[2:].count('1')

s = Solution()
print(s.hammingWeight(11)) # 3
print(s.hammingWeight(128)) # 1
print(s.hammingWeight(4294967293)) # 31
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice233.py
