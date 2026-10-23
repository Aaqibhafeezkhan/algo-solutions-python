<<<<<<< HEAD:practice_problem_solutions (2026)/practice213.py
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
=======
# CodeWars - Take a Number And Sum Its Digits Raised To The Consecutive Powers And ....¡Eureka!!

def sum_dig_pow(a, b):
    res = []
    for i in range(a, b + 1):
        temp = sum(int(num) ** (j + 1) for j, num in enumerate(str(i)))
        if temp == i:
            res.append(i)
    return res

print(sum_dig_pow(1, 10))
print(sum_dig_pow(1, 100))
print(sum_dig_pow(90, 100))
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice213.py
