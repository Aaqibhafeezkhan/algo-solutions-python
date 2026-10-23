<<<<<<< HEAD:practice_problem_solutions (2026)/practice277.py
# Number of Islands

class Solution(object):
    def numIslands(self, grid):
        
        def flood(i, j):
            
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return

            grid[i][j] = '0'

            flood(i + 1, j)
            flood(i - 1, j)
            flood(i, j + 1)
            flood(i, j - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    flood(i, j)
        
        return count

s = Solution()
print(s.numIslands([["1","1","1","1","0"],
                      ["1","1","0","1","0"],
                      ["1","1","0","0","0"],
                      ["0","0","0","0","0"]])) # 1
print(s.numIslands([["1","1","0","0","0"],
                      ["1","1","0","0","0"],
                      ["0","0","1","0","0"],
                      ["0","0","0","1","1"]])) # 3
print(s.numIslands([["1","1","1"],
                    ["0","1","0"],
                    ["1","1","1"]]))           # 1
=======
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
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice277.py
