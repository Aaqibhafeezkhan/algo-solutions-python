<<<<<<< HEAD:practice_problem_solutions (2026)/practice195.py
# HackerRank - Write a function

def is_leap(year):
    leap = False
    
    if year % 4 == 0 and (year % 100 != 0 or year % 400  == 0):
        leap = True
    
    return leap
=======
# Sort by binary ones

def sort_by_binary_ones (numList): 
    bins = [bin(ch)[2:] for ch in numList]
    return list(map(lambda x: int(x, 2), sorted(bins, key=lambda x: (-(x.count('1')), len(x), int(x, 2)))))

print(sort_by_binary_ones( [1,15,5,7,3])) # [15, 7, 5, 3, 1]
print(sort_by_binary_ones([5, 2049, 3]))  # [3, 5, 2049]
print(sort_by_binary_ones([99, 51, 21, 7, 44, 50, 49, 25, 5, 80, 33, 1])) # [51, 99, 7, 21, 25, 44, 49, 50, 5, 33, 80, 1]
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice195.py
