<<<<<<< HEAD:practice_problem_solutions (2026)/practice177.py
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
=======
# HackerRank - Validating Credit Card Numbers

import re

pattern = re.compile(r"^(?:[456]\d{15}|[456]\d{3}(-\d{4}){3})$")

n = int(input())
for _ in range(n):
    temp = input()
    
    is_seq = False
    arr = [num for num in temp if num.isdigit()]
    for i in range(len(arr) - 4):
        if len(set(arr[i+1:i+5])) == 1:
            is_seq = True
            break
            
    if is_seq:
        print('Invalid')
    else:
        print(('Invalid', 'Valid')[bool(pattern.match(temp))])
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice177.py
