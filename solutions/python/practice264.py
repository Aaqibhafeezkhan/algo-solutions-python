<<<<<<< HEAD:practice_problem_solutions (2026)/practice264.py
# Geeksforgeeks - Print n to 1 without loop

class Solution:
    def printNos(self, n):
        return ' '.join(map(str,range(n,0,-1)))

# Accepted Sol; Not mine
class Solution:
    def printNos(self, n):
        if n == 0:
            return
        print(n, end=" ")
        self.printNos(n-1)

s = Solution()
print(s.printNos(10)) # 10 9 8 7 6 5 4 3 2 1
print(s.printNos(5))  # 5 4 3 2 1
print(s.printNos(2))  # 2 1
=======
# GeeksForGeeks - Indexes of Subarray Sum

arr = [1, 2, 3, 7, 5]
def subarraySum(arr, target):
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                x = sum(arr[i:j+1])
                if x == target:
                    return [i+1, j+1]
                elif x > target:
                    break
        return [-1]

print(subarraySum(arr, 12))
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice264.py
