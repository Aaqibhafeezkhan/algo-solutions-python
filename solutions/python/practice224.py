<<<<<<< HEAD:practice_problem_solutions (2026)/practice224.py
# Not in place

w = "ABCDFEGH"
alp = [chr(i).upper() for i in range(97, 123)]


import sys
prev = None

for i in w:
    if prev and alp.index(i) < prev:
        print(i)
        sys.exit()
    prev = alp.index(i)
 
=======
# CodeWars - Chain me

def chain(init_val, functions):
    x = init_val
    for func in functions:
        x = func(x)
    return x
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice224.py
