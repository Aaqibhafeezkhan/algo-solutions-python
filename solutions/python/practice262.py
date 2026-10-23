<<<<<<< HEAD:practice_problem_solutions (2026)/practice262.py
# Geeksforgeeks - Binary to Decimal

class Solution:
    def binary_to_decimal(self, B):
        return int(B, 2)

s = Solution()
print(s.binary_to_decimal("101"))  # 5
print(s.binary_to_decimal("1001")) # 9
print(s.binary_to_decimal("1111")) # 15
=======
# Matrix Diagonal Sum

class Solution(object):
    def diagonalSum(self, mat):
        tot = 0

        for i in range(len(mat)):
            tot += mat[i][i]
            tot += mat[i][len(mat)-1-i]
        
        if len(mat) % 2 != 0:
            tot -= mat[len(mat)//2][len(mat)//2]
        
        return tot

s = Solution()
print(s.diagonalSum([[7,3,1,9],[3,4,6,9],[6,9,6,6],[9,5,8,5]])) # 55
print(s.diagonalSum([[1,2,3],[4,5,6],[7,8,9]])) # 25
print(s.diagonalSum([[5]])) # 5
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice262.py
