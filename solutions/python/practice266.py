<<<<<<< HEAD:practice_problem_solutions (2026)/practice266.py
# Geeksforgeeks - Rotate Array

class Solution:
    def rotateArr(self, arr, d):
        n = d % len(arr)
        arr[:] = arr[n:] + arr[:n]
        return arr
    
s = Solution()
print(s.rotateArr([1, 2, 3, 4, 5], 2)) # [3, 4, 5, 1, 2]
print(s.rotateArr([1, 2, 3, 4, 5], 3)) # [4, 5, 1, 2, 3]
print(s.rotateArr([1, 2, 3, 4, 5], 7)) # [3, 4, 5, 1, 2]
=======
# GeeksForGeeks - Array Search

class Solution:
    def search(self, arr, x):
        return arr.index(x) if x in arr else -1

s = Solution()
print(s.search([1,2,3,5,6], 3)) # 2
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice266.py
