<<<<<<< HEAD:practice_problem_solutions (2026)/practice163.py
# CodeWars - Return the Missing Element

# My solution
def get_missing_element(seq): 
    for num, i in zip(sorted(seq), range(len(seq))):
        if num != i:
            return i
    return 9

# Other clever solution
def get_missing_element(seq): 
    return 45 - sum(seq)

print(get_missing_element([0,5,1,3,2,9,7,6,4])) # 8
print(get_missing_element([9,2,4,5,7,0,8,6,1])) # 3
print(get_missing_element([9,2,4,5,3,0,8,6,1])) # 7
=======
# Mirror Distance of an Integer

class Solution(object):
    def mirrorDistance(self, n):
        return abs(n - int(str(n)[::-1]))
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice163.py
