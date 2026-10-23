<<<<<<< HEAD:practice_problem_solutions (2026)/practice160.py
# CodeWars - Product of consecutive Fib numbers

def product_fib(_prod):
    a, b = 0, 1
    while a * b != _prod and a * b < _prod:
        a, b = b, a + b
    return [a, b, a * b == _prod]

print(product_fib(4895)) # [55, 89,  True]
print(product_fib(5895)) # [89, 144, False]
=======
# Shuffle String

class Solution(object):
    def restoreString(self, s, indices):
        arr = [""] * len(s)
        for i, num in enumerate(indices):
            arr[num] = s[i]
        return "".join(arr)

s = Solution()
print(s.restoreString("codeleet", [4,5,6,7,0,2,1,3])) # "leetcode"
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice160.py
