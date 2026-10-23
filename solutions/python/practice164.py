<<<<<<< HEAD:practice_problem_solutions (2026)/practice164.py
# Two Sum Variant

# Simple Solution 0(n2)
def sums(arr, targ):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == targ:
                return [i, j]
    return -1


# Accepted solution
def sums(arr, targ):
    seen = {}

    for i in range(len(arr)):
        need = targ - arr[i]
        if need in seen:
            return seen[need], i
        seen[arr[i]] = i
        
    return -1

print(sums([1,2,3,4], 7))
print(sums([1,2,3], 7))
=======
# Matrix Script

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

res = ""

for i in range(m):
    for j in range(n):
        res += matrix[j][i]

final = ""
prev = ""
i = 0
while i < len(res):
    if res[i].isalpha():
        final += res[i]
        prev = res[i]
    elif prev.isalpha():
        j = i + 1
        while j < len(res) and not res[j].isalpha():
            j += 1
        if j < len(res) and res[j].isalpha():
            final += " "
            i = j - 1
        else:
            final += res[i]
    else:
        final += res[i]
    i += 1
print(final.strip())

assert final.strip() == "This is Matrix#  %!"
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice164.py
