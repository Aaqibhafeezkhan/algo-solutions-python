<<<<<<< HEAD:practice_problem_solutions (2026)/practice218.py
# Longest Increasing Subsequence

def lis(arr):
    ar = []

    for i in range(len(arr) - 1):
        temp = [arr[i]]
        for j in range(i + 1, len(arr)):
            if temp[-1] < arr[j]:
                temp.append(arr[j])
            else:
                temp[-1] = arr[j]
        ar.append(temp)

    return len(max(ar, key=len))

print(lis([3,1,8,2,5]))       # 3
print(lis([5,2,8,6,3,6,9,5])) # 4
=======
# CodeWars - Data Reverse

def data_reverse(data):
    n = 8
    res = []
    
    i = 0
    for _ in range(len(data) // n):
        cur = []
        while i < len(data) and len(cur) < n:
            cur.append(data[i])
            i += 1
        res.append(cur)
    return [num for sublist in res[::-1] for num in sublist]

print(data_reverse([1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0])) # [1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0]
print(data_reverse([0,0,1,0,1,1,1,0,1,1,0,0,1,1,1,0])) # [1,1,1,0,1,1,0,0,1,0,0,0,1,0,0,0]
print(data_reverse([1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0])) # [1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0]
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice218.py
