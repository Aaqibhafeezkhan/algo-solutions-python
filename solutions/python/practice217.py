<<<<<<< HEAD:practice_problem_solutions (2026)/practice217.py
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
=======
# CodeWars - Good vs Evil

def good_vs_evil(good, evil):
    
    goods = {
        0: 1,
        1: 2,
        2: 3,
        3: 3,
        4: 4,
        5: 10
    }
    
    evils = {
        0: 1,
        1: 2,
        2: 2,
        3: 2,
        4: 3,
        5: 5,
        6: 10
    }
    
    g_score = 0
    for i, per in enumerate(good.split()):
        g_score += goods[i] * int(per)
    
    e_score = 0
    for i, per in enumerate(evil.split()):
        e_score += evils[i] * int(per)
    
    if g_score > e_score:
        return "Battle Result: Good triumphs over Evil"
    elif g_score < e_score:
        return "Battle Result: Evil eradicates all trace of Good"
    
    return "Battle Result: No victor on this battle field"
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice217.py
