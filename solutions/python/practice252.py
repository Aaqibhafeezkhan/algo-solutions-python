<<<<<<< HEAD:practice_problem_solutions (2026)/practice252.py
# Happy Number

class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()

        while n != 1:
            sums = 0
            temp = n
            while temp > 0:
                sums += (temp % 10) ** 2
                temp //= 10
            if sums in seen:
                return False

            seen.add(sums)
            n = sums
        
        return True

s = Solution()
print(s.isHappy(19)) # True
print(s.isHappy(2)) # False
print(s.isHappy(7)) # True
=======
# FizzBuzz with Twist

def fizzbuzzpop(n):
    res = ""
    if n % 3 == 0:
        res += 'Fizz'
    if n % 5 == 0:
        res += 'Buzz'
    if n % 7 == 0:
        res += 'Pop'
    return res

print(fizzbuzzpop(9))
print(fizzbuzzpop(10))
print(fizzbuzzpop(15))
print(fizzbuzzpop(49))
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice252.py
