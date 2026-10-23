<<<<<<< HEAD:practice_problem_solutions (2026)/practice314.py
# Integer to Roman

class Solution(object):
    def intToRoman(self, num):
        romans = [
            ['M', 1000],
            ['CM', 900], ['D', 500], ['CD', 400],
            ['C', 100], ['XC', 90], ['L', 50],
            ['XL', 40], ['X', 10], ['IX', 9],
            ['V', 5], ['IV', 4], ['I', 1]
        ]

        res = ""

        for sym, val in romans:
            if num // val:
                count, num = divmod(num, val)
                res += sym * count
        
        return res

s = Solution()
print(s.intToRoman(1390)) # "MCCCXC"
print(s.intToRoman(79))   # "LXXIX"
print(s.intToRoman(3))    # "III"
=======
# Weighted Word Mapping

class Solution:
    def mapWordWeights(self, words, weights) -> str:
        alp = dict(zip(range(25, -1, -1),[chr(i) for i in range(97, 123)]))

        res = ""
        for word in words:
            t = sum([weights[ord(w) - 97] for w in word]) % 26
            print(t)
            res += alp[t]

        return res

s = Solution()
print(s.mapWordWeights(["abcd","def","xyz"], [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]))
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice314.py
