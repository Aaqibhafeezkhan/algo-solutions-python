<<<<<<< HEAD:practice_problem_solutions (2026)/practice179.py
# GeeksForGeeks - Indexes of Subarray Sum

arr = [1, 2, 3, 7, 5]
def subarraySum(arr, target):
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                x = sum(arr[i:j+1])
                if x == target:
                    return [i+1, j+1]
                elif x > target:
                    break
        return [-1]

print(subarraySum(arr, 12))
=======
# First Matching Character From Both Ends

class Solution(object):
    def firstMatchingIndex(self, s):
        n = len(s)
        for i in range(n):
            if s[i] == s[n - i - 1]:
                return i
        return -1
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice179.py
