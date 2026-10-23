<<<<<<< HEAD:practice_problem_solutions (2026)/practice145.py
# CodeWars - N-th Fibonacci

def nth_fib(n):
    a, b = 0, 1
    count = 2
    if n < 2:
        return [a, b][n - 1]
    while count < n:
        a, b = b, a + b
        count += 1
    return b

print(nth_fib(1)) # 0
print(nth_fib(2)) # 1
print(nth_fib(100)) # 218922995834555169026
=======
# Array Partition

class Solution(object):
    def arrayPairSum(self, nums):
        return sum(num for i, num in enumerate(sorted(nums)) if i % 2 == 0)

s = Solution()
print(s.arrayPairSum([1, 4, 3, 2]))       # 4
print(s.arrayPairSum([6, 2, 6, 5, 1, 2])) # 9
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice145.py
