<<<<<<< HEAD:practice_problem_solutions (2026)/practice205.py
# HackerRank - Angry Professor

def angryProfessor(k, a):
    return ['NO', 'YES'][len([st for st in a if st <= 0])<k]

print(angryProfessor(3, [-1,-3,4,2])) # YES
print(angryProfessor(2, [0,-1,2,1]))  # NO
=======
# HackerRank - Word Order

from collections import Counter
arr = [input() for _ in range(int(input()))]

counts = {}
for word in arr:
    counts[word] = counts.get(word, 0) + 1

print(len(counts))
print(' '.join(str(count) for count in counts.values()))
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice205.py
