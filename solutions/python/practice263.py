<<<<<<< HEAD:practice_problem_solutions (2026)/practice263.py
# Geeksfor Geeks - Bits Counting

from typing import List

class Solution:
    def countBits(self, n : int) -> List[int]:
        arr = []
        
        for i in range(n + 1):
            arr.append(bin(i)[2:].count('1'))
        
        return arr
        
s = Solution()
print(s.countBits(10)) # [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]
print(s.countBits(5))  # [0, 1, 1, 2, 1, 2]
print(s.countBits(2))  # [0, 1, 1]
=======
class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        arr = [0, 0]
        for num in nums1:
            if num in nums2:
                arr[0] += 1
        
        for num in nums2:
            if num in nums1:
                arr[1] += 1

        return arr

s = Solution()
print(s.findIntersectionValues([4,3,2,3,1], [2,2,5,2,3,6])) # [3,4]
print(s.findIntersectionValues([3,4,2,3], [1,5])) # [0,0]
print(s.findIntersectionValues([2,3,2], [1,2])) # [2,1]
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice263.py
