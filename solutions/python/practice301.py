<<<<<<< HEAD:practice_problem_solutions (2026)/practice301.py
# HackerRank - Pair of gloves

from collections import Counter
def number_of_pairs(gloves):
    count = Counter(gloves)
    
    tot = []
    
    for c, v in count.items():
        pairs = v // 2
        if pairs > 0:
            tot.append([c, pairs])

    return sum(pair for _, pair in tot) if tot else 0

print(number_of_pairs(["red", "red", "red", "red", "red", "red"]))  # 3
print(number_of_pairs(["red", "green", "red", "blue", "blue"]))     # 2
print(number_of_pairs(["red", "green", "blue"]))                    # 0
=======
# HackerRank - Equalize the Array

def equalizeArray(arr):
    return len(arr) - arr.count(max(arr, key=lambda x: arr.count(x)))

print(equalizeArray([3,3,2,1,3]))       # 2
print(equalizeArray([1,2,3,1,2,3,3,3])) # 4
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice301.py
