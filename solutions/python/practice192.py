<<<<<<< HEAD:practice_problem_solutions (2026)/practice192.py
# Number of Lines To Write String

class Solution(object):
    def numberOfLines(self, widths, s):
        ar = []
        al = dict(zip([chr(i)for i in range(97, 123)], widths))

        cur = 0
        i = 0
        temp = []
        while i < len(s):
            num = al[s[i]]
            if cur + num > 100:
                ar.append([temp, cur])
                cur = num
                temp = [s[i]]
                i += 1
                continue
            else:
                temp.append(s[i])
                cur += num

            if cur == 100:
                ar.append([temp, cur])
                cur = 0
                temp = []
            i += 1
        if temp and cur > 0:
            ar.append([temp, cur])
        return [len(ar), ar[-1][1]]

s = Solution()
print(s.numberOfLines([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "abcdefghijklmnopqrstuvwxyz")) # [3,60]
print(s.numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "bbbcccdddaaa")) # [2,4]
print(s.numberOfLines([3,4,10,4,8,7,3,3,4,9,8,2,9,6,2,8,4,9,9,10,2,4,9,10,8,2], "mqblbtpvicqhbrejb")) # [1,100]
=======
# GCD of Sums of Odd and Even Integers

# Brut Force Solution
class Solution(object):
    def gcdOfOddEvenSums(self, n):
        odd = []
        even = []
        i = 1
        while len(odd) < n:
            odd.append(i)
            i += 2
        i = 0
        while len(even) < n:
            even.append(i)
            i += 2
        
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        return gcd(sum(even), sum(odd))

# Mathematical Solution
class Solution(object):
    def gcdOfOddEvenSums(self, n):
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        return gcd(n * n, n * (n + 1))
    

s = Solution()
print(s.gcdOfOddEvenSums(5)) # 5
print(s.gcdOfOddEvenSums(6)) # 3
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice192.py
