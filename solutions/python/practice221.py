<<<<<<< HEAD:practice_problem_solutions (2026)/practice221.py
# Sum of All Odd Length Subarrays

class Solution:
    def sumOddLengthSubarrays(self, arr) -> int:
        n = len(arr)
        t = sum(arr)
        
        for i in range(n - 1):
            for j in range(i + 2, n, 2):
                temp = arr[i:j+1]
                print(temp)
                if len(temp) % 2 != 0:
                    t += sum(temp)

        return t
        
s = Solution()
print(s.sumOddLengthSubarrays([1,4,2,5,3])) # 58
print(s.sumOddLengthSubarrays([10,11,12]))  # 66
print(s.sumOddLengthSubarrays([1,2]))       # 3
=======
# CodeWars -Pyramid Array

def pyramid(n):
    res = []
    for i in range(1, n + 1):
        temp = []
        for j in range(i):
            temp.append(1)
        res.append(temp)
    return res

print(pyramid(0)) # []
print(pyramid(1)) # [[1]]
print(pyramid(3)) # [[1], [1, 1], [1, 1, 1]]
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice221.py
