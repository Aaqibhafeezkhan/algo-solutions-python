<<<<<<< HEAD:practice_problem_solutions (2026)/practice208.py
# HackerRank - The Hurdle Race

def hurdleRace(k, height):
    return max(height) - k if k < max(height) else 0

print(hurdleRace(7, [1,6,3,5,2])) # 0
print(hurdleRace(4, [1,6,3,5,2])) # 2
print(hurdleRace(2, [3,5,7,9,1])) # 7
=======
# CodeWars - Mexican Wave

def wave(people):
    arr = []
    for i in range(len(people)):
        if not people[i].isalpha():
            continue
        temp = list(people)
        temp[i] = temp[i].upper()
        arr.append(''.join(temp))
    return arr

print(wave('hello')) # ['Hello', 'hEllo', 'heLlo', 'helLo', 'hellO']
print(wave('gap')) # ['Gap', 'gAp', 'gaP']
print(wave('two words')) # ['Two words', 'tWo words', 'twO words', 'two Words', 'two wOrds', 'two woRds', 'two worDs', 'two wordS']
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice208.py
