<<<<<<< HEAD:practice_problem_solutions (2026)/practice273.py
# HackerRank - Fair Rations

def fairRations(B):
    count = 0
    for i in range(len(B)):
        if B[i] % 2 != 0:
            if i + 1 < len(B):
                print(B)
                B[i] += 1
                B[i + 1] += 1
                count += 2
            else:
                print(B)
                break
            print('=' * 20)
    print(B)
    if all(c % 2 == 0 for c in B):
        return count
    return 'NO'

print(fairRations([2, 3, 4, 5, 6])) # 2
print(fairRations([1, 2]))    # NO
=======
# Distribute Candies

class Solution(object):
    def distributeCandies(self, candyType):
        cd = len(set(candyType))
        ce = len(candyType) // 2
        return min(ce, cd)

s = Solution()
print(s.distributeCandies([1,1,2,2,3,3])) # 3
print(s.distributeCandies([1,1,2,3]))     # 2
print(s.distributeCandies([6,6,6,6]))     # 1
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice273.py
