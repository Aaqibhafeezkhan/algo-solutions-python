<<<<<<< HEAD:practice_problem_solutions (2026)/practice290.py
# CodeWars - Add Fractions

from fractions import Fraction
def add_fracs(*args):
    return str(Fraction(sum(eval(c) for c in args)).limit_denominator()) if args else ''

print(add_fracs())                    # ''
print(add_fracs('1/2', '3/4'))        # '5/4'
print(add_fracs('1/2', '1/3', '1/4')) # '13/12'
=======
# HackerRank - Angry Professor

def angryProfessor(k, a):
    return ['NO', 'YES'][len([st for st in a if st <= 0])<k]

print(angryProfessor(3, [-1,-3,4,2])) # YES
print(angryProfessor(2, [0,-1,2,1]))  # NO
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice290.py
