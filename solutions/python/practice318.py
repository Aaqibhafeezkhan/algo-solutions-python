<<<<<<< HEAD:practice_problem_solutions (2026)/practice318.py
# CodeWars - So Many Permutations!

from itertools import permutations as p
def permutations(s):
    return list(set(''.join(list(e)) for e in p(s)))

print(permutations('abcd')) # ['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca', 'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba']
print(permutations('aabb')) # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
print(permutations('a'))    # ['a']
=======
# Furthest Point From Origin

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        return abs(moves.count('R') - moves.count('L')) + moves.count('_')
    
s = Solution()
print(s.furthestDistanceFromOrigin("L_RL__R")) # 3
print(s.furthestDistanceFromOrigin("_R__LL_")) # 5
print(s.furthestDistanceFromOrigin("_______")) # 7
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice318.py
