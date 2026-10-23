<<<<<<< HEAD:practice_problem_solutions (2026)/practice199.py
# Repeated String

def repeatedString(s, n):
    l = len(s)
    
    total = n // l
    other = n % l
    
    return (s.count('a') * total) + s[:other].count('a')

print(repeatedString('a', 1000000000000)) # 1000000000000
print(repeatedString('aba', 10))          # 7
print(repeatedString('abcac', 10))        # 4
=======
# Find the Number of Good Pairs I

class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        count = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] % (nums2[j] * k) == 0:
                    count += 1
        return count

s = Solution()
print(s.numberOfPairs([1,2,3,4], [1,2,3,4], 1))  # 8
print(s.numberOfPairs([1,2,3,4], [1,2,3,4], 2))  # 3
print(s.numberOfPairs([1,2,3,4], [1,2,3,4], 3))  # 1
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice199.py
