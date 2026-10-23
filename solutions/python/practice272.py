<<<<<<< HEAD:practice_problem_solutions (2026)/practice272.py
# HackerRank - Minimum Distances

def minimumDistances(a):
    if len(set(a)) == len(a):
        return -1
        
    d = {}
    
    for i in range(len(a)):
        if a[i] in d:
            d[a[i]].append(i)
        else:
            d[a[i]] = [i]
    minN = float('inf')
    for pairs in d.values():
        if len(pairs) > 1:
            minN = min(minN, abs(pairs[0] - pairs[1]))
    
    return minN

print(minimumDistances([7, 1, 3, 4, 1, 7])) # 3
print(minimumDistances([1, 2, 3, 4, 5]))    # -1
print(minimumDistances([1, 1]))             # 1
=======
# Backspaces in string

def clean_string(s):
    seen = []
    
    for c in s:
        if seen and c == '#':
            seen.pop()
        elif c != '#':
            seen.append(c)
    
    return ''.join(seen)
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice272.py
