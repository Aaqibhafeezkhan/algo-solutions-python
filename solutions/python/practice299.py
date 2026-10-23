<<<<<<< HEAD:practice_problem_solutions (2026)/practice299.py
# HackerRank - Running Time of Algorithms

def runningTime(arr):
    count = 0
    
    for i in range(1, len(arr)):
        key = arr[i]
        
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            count += 1
            j -= 1
        arr[j + 1] = key
    
    return count

print(runningTime([ 8, 6, 6, 42, 8, 1, 1, 13, 4, 6, 2, 1, 1, 39 ])) # 51
print(runningTime([2, 1, 3, 1, 2]))                                 # 4
print(runningTime([1, 1, 1, 2, 2]))                                 # 0
=======
# HackerRank - Between Two Sets

def getTotalX(a, b):
    ar = []
    for i in range(a[-1], b[0] + 1):
        div = True
        
        for num in a:
            if i % num != 0:
                div = False
                break
        if div:
            ar.append(i)

    inc = []
    for num in ar:
        div = True
        for n in b:
            if n % num != 0:
                div = False
                break
        if div:
            inc.append(num)
    
    return len(inc)

print(getTotalX([2,4], [16,32,96]))
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice299.py
