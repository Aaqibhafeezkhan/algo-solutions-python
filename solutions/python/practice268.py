<<<<<<< HEAD:practice_problem_solutions (2026)/practice268.py
# GeeksforGeeks - Row with max 1s

class Solution:
    def rowWithMax1s(self, arr):
        max_ones = 0
        ind = -1
        
        for i, row in enumerate(arr):
            counts = row.count(1)
            if counts > max_ones:
                max_ones = counts
                ind = i
        
        return ind

s = Solution()
print(s.rowWithMax1s([[0, 1, 1], [0, 0, 1], [1, 1, 1]]))  # 2
print(s.rowWithMax1s([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))  # -1
print(s.rowWithMax1s([[1, 1, 1], [0, 0, 0], [0, 0, 0]]))  # 0
=======
# Number Complement

class Solution(object):
    def findComplement(self, num):
        bina = list(bin(num)[2:])
        for i, c in enumerate(bina):
            bina[i] = '1' if c == '0' else '0'
        return int(''.join(bina), 2)

s = Solution()
print(s.findComplement(5))  # 2
print(s.findComplement(1))  # 0
print(s.findComplement(12)) # 3
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice268.py
