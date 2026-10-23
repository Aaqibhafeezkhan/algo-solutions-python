<<<<<<< HEAD:practice_problem_solutions (2026)/practice292.py
# CodeWars - Sort arrays - 1

def sortme(names):
    return sorted(names, key=lambda x: (ord(x[0]), ord(x[1])))

print(sortme(["one", "two", "three"])) # ['one', 'three', 'two']
=======
# HackerRank - Append and Delete

def appendAndDelete(s, t, k):
    i = 0
    while i < min(len(s), len(t)) and s[i] == t[i]:
        i += 1

    ops = (len(s) - i) + (len(t) - i)

    if k >= len(s) + len(t):
        return "Yes"

    if k >= ops and (k - ops) % 2 == 0:
        return "Yes"

    return "No"

print(appendAndDelete("hackerhappy", "hackerrank", 9)) # Yes
print(appendAndDelete("ashley", "ash", 2))             # No
print(appendAndDelete("ash", "ashley", 1))             # No
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice292.py
