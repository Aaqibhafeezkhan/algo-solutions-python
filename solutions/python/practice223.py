<<<<<<< HEAD:practice_problem_solutions (2026)/practice223.py
# HackerRank - Drawing Book

def pageCount(n, p):
    pages = [[i, i+1] for i in range(0, n+1, 2)]
    
    cur_min = 0
    for i in range(len(pages)):
        if p in pages[i]:
            cur_min = i
    
    for i, page in enumerate(pages[::-1]):
        if p in page:
            cur_min = min(cur_min, i)
    
    return(cur_min)

print(pageCount(5, 3)) # 1
print(pageCount(6, 2)) # 1
print(pageCount(5, 4)) # 0
=======
# CodeWars - Sum of Odd Cubed Numbers

def cube_odd(arr):
    res = 0
    
    for num in arr:
        if type(num) == int:
            if (num ** 3) % 2 != 0:
                res += num ** 3
        else:
            return None
    return res


print(cube_odd([1, 2, 3, 4, 5])) # 153
print(cube_odd([0, 1, False, 3, True, 5])) # None
print(cube_odd([1, 2, 3, 4, 5, '7'])) # None
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice223.py
