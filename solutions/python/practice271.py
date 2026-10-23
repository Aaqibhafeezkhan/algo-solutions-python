<<<<<<< HEAD:practice_problem_solutions (2026)/practice271.py
# Vowel and Consonant

n = int(input()) # "àç_èç_è_(-'(çè_-çàà)ç_è(_-v çè- çàè_-ponctuation"
v, c = 0, 0
for i in range(n):
    text = input().lower()
    v += len([c for c in text if c in 'aeiou' and c.isalpha()])
    c += len([c for c in text if c not in 'aeiou' and 97 <= ord(c) < 123])
    print(v)
    print(c)
print(v * c)
=======
# CodeWars - Meeting

def meeting(s):
    names = []
    for name in s.split(';'):
        first, last = name.upper().split(':')
        names.append([last, first])
    
    return ''.join(f"({last}, {name})" for last, name in sorted(names, key=lambda x: (x[0], x[1])))
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice271.py
