<<<<<<< HEAD:practice_problem_solutions (2026)/practice289.py
# Geeksforgeeks - Rotate Array by One

class Solution:
    def rotate(self, arr):
        if not arr:
            return arr
            
        d = 1 % len(arr)
        arr[:] = arr[-d:] + arr[:-d]
        return arr
    
s = Solution()
print(s.rotate([1, 2, 3, 4, 5, 6, 7])) # [7, 1, 2, 3, 4, 5, 6]
print(s.rotate([1, 2, 3, 4, 5, 6]))    # [6, 1, 2, 3, 4, 5]
print(s.rotate([1, 2, 3, 4, 5]))       # [5, 1, 2, 3, 4]
=======
# HackerRank - Electronics Shop

def getMoneySpent(keyboards, drives, b):
    prices = []
    for kb in sorted(keyboards)[::-1]:
        for d in sorted(drives)[::-1]:
            if kb + d <= b:
                prices.append(kb + d)
    return max(prices) if prices else -1

print(getMoneySpent([40,50,60], [5,8,12], 60)) # 58
print(getMoneySpent([3,1], [5,2,8], 10)) # 9
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice289.py
