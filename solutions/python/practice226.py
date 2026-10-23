<<<<<<< HEAD:practice_problem_solutions (2026)/practice226.py
# HackerRank - Non-Divisible Subset

# Other Sol
def nonDivisibleSubset(k, s):
    freq = [0] * k
    for num in s:
        freq[num % k] += 1
    
    count = 0

    if freq[0] > 0:
        count += 1

    for i in range(1, k // 2 + 1):
        if i == k - i:
            if freq[i] > 0:
                count += 1
        else:
            count += max(freq[i], freq[k - i])
    
    return count


print(nonDivisibleSubset(7, list(map(int, "278 576 496 727 410 124 338 149 209 702 282 718 771 575 436".split())))) # 11
=======
# Convert an Array Into a 2D Array With Conditions

class Solution(object):
    def findMatrix(self, nums):
        res = []

        while nums:
            cur = []
            for num in nums:
                if cur and num in cur:
                    continue
                cur.append(num)
            res.append(cur)
            for val in cur:
                nums.remove(val)
        return res
    
s = Solution()
print(s.findMatrix([1, 3, 4, 1, 2, 3, 1])) # [[1, 3, 4, 2], [1, 3], [1]]
print(s.findMatrix([1, 1, 1, 1, 1])) # [[1], [1], [1], [1], [1]]
print(s.findMatrix([1, 2, 3, 4])) # [[1, 2, 3, 4]]
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice226.py
