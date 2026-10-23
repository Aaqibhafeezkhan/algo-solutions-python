<<<<<<< HEAD:practice_problem_solutions (2026)/practice298.py
# HackerRank - CamelCase

def camelcase(s):
    return sum(1 for c in s if c.isupper()) + 1 if s else 0

print(camelcase("oneTwoThreeFourFiveSixSevenEightNineTen"))  # 10
print(camelcase("saveChangesInTheEditor"))                   # 5
print(camelcase(""))                                         # 0
=======
# HackerRank - Picking Numbers

def pickingNumbers(a):
    subs = []
    i = 0

    a.sort()

    while i < len(a) - 1:
        temp = [a[i]]
        
        for j in range(i + 1, len(a)):
            add = True
            for num in temp:
                if abs(num - a[j]) > 1:
                    add = False
            if add:
                temp.append(a[j])

        subs.append(temp)

        i += 1
                
    return len(max(subs, key=len))

print(pickingNumbers([1,1,2,2,4,4,5,5,5])) # 5
print(pickingNumbers([4,6,5,3,3,1]))       # 3
print(pickingNumbers([1,2,2,3,1,2]))       # 5
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice298.py
