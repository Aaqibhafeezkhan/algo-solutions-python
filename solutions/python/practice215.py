<<<<<<< HEAD:practice_problem_solutions (2026)/practice215.py
# HackerRank - Sequence Equation

def permutationEquation(p):
    res = []
    for i in range(1, len(p) + 1):
        inner = p.index(i) + 1
        outer = p.index(inner) + 1
        res.append(outer)
    return res

print(permutationEquation([5,2,1,3,4])) # [4,2,5,1,3]
print(permutationEquation([4,3,5,1,2])) # [1,3,5,4,2]
print(permutationEquation([2,3,1]))     # [2,3,1]
=======
# CodeWars - Roman Numerals Decoder

def solution(roman : str) -> int:
    
    romans = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0
    i = 0
    while i < len(roman):
        if i + 1 < len(roman):
            if romans[roman[i]] < romans[roman[i + 1]]:
                result += romans[roman[i + 1]] - romans[roman[i]]
                i += 2
                continue
        result += romans[roman[i]]
        i += 1
    return result

print(solution('XXI'))      # 21
print(solution('I'))        # 1
print(solution('IV'))       # 4
print(solution('MMVIII'))   # 2008
print(solution('MDCLIXIV')) # 1663
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice215.py
