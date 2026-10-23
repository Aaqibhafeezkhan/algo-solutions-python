<<<<<<< HEAD:practice_problem_solutions (2026)/practice169.py
# Number of Islands

def islands(arr):
    island = 0

    for ar in arr:
        for num in ar:
            if num == '1':
                island += 1
    
    return island


print(islands([['1','0','1'], ['1','1','1'], ['1','0','1']]))
=======
# Vowel Recognition

def vowel_recognition(s):
    vowels = set("aeiouAEIOU")
    count = 0
    n = len(s)
    for i, c in enumerate(s):
        if c in vowels:
            count += (i + 1) * (n - i)
    return count

print(vowel_recognition("aba")) # 6
print(vowel_recognition("abc")) # 3
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice169.py
