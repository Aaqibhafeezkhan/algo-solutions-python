<<<<<<< HEAD:practice_problem_solutions (2026)/practice247.py
# HackerRank - Circular Array Rotation

def circularArrayRotation(a, k, queries):
    k %= len(a)
    arr = a[-k:] + a[:-k]
    return [arr[i] for i in queries]

print(circularArrayRotation([1, 2, 3, 4], 4, [0, 1, 2, 3]))  # [1, 2, 3, 4]
print(circularArrayRotation([1, 2, 3], 2, [0, 1, 2]))        # [2, 3, 1]
print(circularArrayRotation([3, 4, 5], 2, [1, 2]))           # [5, 3]
=======
def zeros(n):
    count = 0
    while n:
        n //= 5
        count += n
    return count
    
print(zeros(6))          # 1
print(zeros(30))         # 7
print(zeros(1000000000)) # 249999998
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice247.py
