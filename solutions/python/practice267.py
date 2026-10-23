<<<<<<< HEAD:practice_problem_solutions (2026)/practice267.py
# Geeksforgeeks - Smallest Positive Missing

class Solution:
    def missingNumber(self, arr):
        arr[:] = sorted([num for num in arr if num > 0])
        if arr:
            for i in range(1, max(arr)):
                if i not in arr:
                    return i
        return max(arr) + 1 if arr else 1

s = Solution()
print(s.missingNumber([7, 8, 9, 11, 12])) # 1
print(s.missingNumber([3, 4, -1, 1]))     # 2
print(s.missingNumber([1, 2, 0]))         # 3
print(s.missingNumber([-12, 0]))          # 1
=======
# Next Greater Element I

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        arr = []

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    if j < len(nums2) - 1:
                        k = j + 1
                        while k < len(nums2) and nums2[k] < nums2[j]:
                            k += 1
                        if k < len(nums2) and nums2[k] > nums2[j]:
                            arr.append(nums2[k])
                            break
                    arr.append(-1)
                
        return arr
    
s = Solution()
print(s.nextGreaterElement([2,4], [1,2,3,4]))             # [3,-1]
print(s.nextGreaterElement([4,1,2], [1,3,4,2]))           # [-1,3,-1]
print(s.nextGreaterElement([1,3,5,2,4], [6,5,4,3,2,1,7])) # [7,7,7,7,7]
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice267.py
