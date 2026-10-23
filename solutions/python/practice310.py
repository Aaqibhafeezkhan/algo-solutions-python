<<<<<<< HEAD:practice_problem_solutions (2026)/practice310.py
# py.checkio - The Highest Building

def highest_building(buildings: list[list[int]]) -> list[int]:
    
    cur_max = float('-inf')
    ind = -1

    n = len(buildings) - 1
    for col in range(len(buildings[0])):
        row = n
        
        while row >= 0 and buildings[row][col] == 1:
            row -= 1
        
        new_height = n - row
        if new_height > cur_max:
            ind = col
            cur_max = new_height

    return [ind + 1, cur_max]


print(highest_building([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]])) # [4, 1]
print(highest_building([[0, 0, 1, 0], [1, 0, 1, 0], [1, 1, 1, 0], [1, 1, 1, 1]])) # [3, 4]
print(highest_building([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]])) # [3, 2]
=======
# HackerRank - Cut the sticks

def cutTheSticks(arr):
    count = [len(arr)]
    
    while arr:
        temp = []
        mn = min(arr)
        for i in range(len(arr)):
            if arr[i] - mn > 0:
                temp.append(arr[i] - mn)
        arr = temp
        if arr:
            count.append(len(arr))
    
    return count

print(cutTheSticks([5,4,4,2,2,8]))     # [6,4,2,1]
print(cutTheSticks([1,2,3,4,3,3,2,1])) # [8,6,4,1]
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice310.py
