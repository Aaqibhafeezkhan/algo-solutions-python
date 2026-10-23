<<<<<<< HEAD:practice_problem_solutions (2026)/practice207.py
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
=======
# HackerRank - Compress the String!

s = input()

res = []
i = 0
while i < len(s):
    count = 0
    while i + 1 < len(s) and s[i] == s[i + 1]:
        count += 1
        i += 1
    i += 1
    res.append((count + 1, int(s[i - 1])))
print(' '.join(map(str, res)))
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice207.py
