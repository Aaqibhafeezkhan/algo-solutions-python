<<<<<<< HEAD:practice_problem_solutions (2026)/practice302.py
# CodeWars - Currying functions: multiply all elements in an array

def multiply_all(arr):
    return lambda n: [x * n for x in arr]

print(multiply_all([1, 2, 3])(4))  # [4, 8, 12] 
print(multiply_all([1, 2, 3])(3))  # [3, 6, 9]
print(multiply_all([1, 2, 3])(2))  # [2, 4, 6]
=======
import math

def viralAdvertising(n):
    shared = 5
    likes = 0

    for _ in range(n):
        like = shared // 2
        likes += like
        shared = like * 3
    
    return likes

print(viralAdvertising(3)) # 9
print(viralAdvertising(4)) # 15
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice302.py
