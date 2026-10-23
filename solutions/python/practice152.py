<<<<<<< HEAD:practice_problem_solutions (2026)/practice152.py
# Clear Digits

class Solution(object):
    def clearDigits(self, s):

        seen = []
        for letter in s:
            if not seen and letter.isalpha():
                seen.append(letter)
            elif letter.isalpha():
                seen.append(letter)
            else:
                if seen:
                    seen.pop()
                
        return ''.join(seen)

s = Solution()
print(s.clearDigits("abc")) # "abc"
print(s.clearDigits("cb34")) # ""
print(s.clearDigits("1234")) # ""
=======
# Largest Local Values in a Matrix

class Solution(object):
    def largestLocal(self, grid):
        n = len(grid)
        res = [[0] * (n - 2) for _ in range(n - 2)]

        for i in range(n - 2):
            for j in range(n - 2):
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        res[i][j] = max(res[i][j], grid[r][c])

        return res
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice152.py
