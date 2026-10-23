<<<<<<< HEAD:practice_problem_solutions (2026)/practice248.py
# HackerRank - Jumping on the Clouds

def jumpingOnClouds(c):
    jumps = 0
    
    i = 0
    while i < len(c):
        
        if i + 2 < len(c) and c[i + 2] == 0:
            jumps += 1
            i += 2
            continue
        if i + 1 < len(c) and c[i + 1] == 0:
            jumps += 1
            i += 1
            continue
        
        jumps += 1
        i += 2
        
    return jumps - 1

print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]))  # 4
print(jumpingOnClouds([0, 0, 0, 1, 0, 0]))     # 3
print(jumpingOnClouds([0, 0, 0, 0, 1, 0]))     # 3
=======
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
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice248.py
