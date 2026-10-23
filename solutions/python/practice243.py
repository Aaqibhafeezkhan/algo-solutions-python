<<<<<<< HEAD:practice_problem_solutions (2026)/practice243.py
from collections import Counter
class Solution:
    def findEvenNumbers(self, digits):
        arr = []
        
        D = Counter(map(str, digits))

        for i in range(100, 999, 2):
            temp = Counter(str(i))

            if all(temp[k] <= D[k] for k in temp):
                arr.append(i)
                
        return arr
    
s = Solution()
print(s.findEvenNumbers([2,1,3,0]))   # [102,120,130,132,210,230,302,310,312,320]
print(s.findEvenNumbers([2,2,8,8,2])) # [222,228,282,288,822,828,882]
print(s.findEvenNumbers([3,7,5]))     # []
=======
# Height Checker

class Solution(object):
    def heightChecker(self, heights):
        srt = sorted(heights)
        count = 0
        for x, y in zip(heights, srt):
            if x != y:
                count += 1
        return count

s = Solution()
print(s.heightChecker([1,1,4,2,1,3])) # 3
print(s.heightChecker([5,1,2,3,4]))   # 5
print(s.heightChecker([1,2,3,4,5]))   # 0
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice243.py
