<<<<<<< HEAD:practice_problem_solutions (2026)/practice249.py
# HackerRank - Bigger is Greater

# Not my Sol;
def biggerIsGreater(w):
    arr = list(w)

    pivot = -1
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] > arr[i - 1]:
            pivot = i - 1
            break

    if pivot == -1:
        return 'no answer'

    for i in range(len(arr) - 1, pivot, -1):
        if arr[i] > arr[pivot]:
            arr[i], arr[pivot] = arr[pivot], arr[i]
            break

    arr[pivot + 1:] = sorted(arr[pivot + 1:])

    return ''.join(arr)


print(biggerIsGreater("ab"))  # "ba"
print(biggerIsGreater("bb"))  # "no answer"
print(biggerIsGreater("hefg"))  # "hegf"
print(biggerIsGreater("dkhc"))  # "hcdk"
=======
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
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice249.py
