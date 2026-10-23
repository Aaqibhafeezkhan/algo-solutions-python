<<<<<<< HEAD:practice_problem_solutions (2026)/practice251.py
# Sort an array of 0s, 1s and 2s without using any sorting algorithm.

class Solution:
    def sort012(self, arr):
        from collections import Counter
        d = Counter(arr)
        
        return [i for i in range(3) for _ in range(d[i])]

s = Solution()
print(s.sort012([0, 1, 2, 0, 1, 2])) # [0, 0, 1, 1, 2, 2]
print(s.sort012([1, 0, 1, 2, 0, 1])) # [0, 0, 1, 1, 1, 2]
print(s.sort012([2, 2, 0, 1, 0, 1])) # [0, 0, 1, 1, 2, 2]
=======
# Maximum Subarray Sum

def maxSub(arr):
    cur_sum = []
    seen = []
    for i in range(len(arr)):
        if seen and seen[-1] > arr[i]:
            cur_sum.append(seen)
            seen = [arr[i]]
            continue
        seen.append(arr[i])
    if seen:
        cur_sum.append(seen)
    return max(cur_sum, key=lambda x: sum(x)) if cur_sum else []

print(maxSub([1,2,3,4,5,6,7,8,9]))
print(maxSub([1,2,3,4,1,7,8,9]))
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice251.py
