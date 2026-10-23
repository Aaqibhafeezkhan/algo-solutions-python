<<<<<<< HEAD:practice_problem_solutions (2026)/practice173.py
# Count of Matches in Tournament

class Solution(object):
    def numberOfMatches(self, n):
        count = 0
        while n > 1:
            if n % 2 == 0:
                count += n // 2
                n //= 2
            else:
                count += (n - 1) // 2
                n = (n - 1) // 2 + 1
        return count
    
s = Solution()
print(s.numberOfMatches(n=7)) # 6
=======
# HackerRank - Maximize It!

k, m = map(int, input().split())

arr = []
for _ in range(k):
    temp = list(map(int, input().split()))
    x = temp[0]
    arr.append(temp[1:x+1])

result = [[]]

for lst in arr:
    new_comb = []
    for ar in result:
        for val in lst:
            new_comb.append(ar + [val])
    result = new_comb

cur_max = float('-inf')
for ar in result:
    temp = []
    for val in ar:
        temp.append(val ** 2)
    cur_max = max(cur_max, sum(temp) % m)

print(cur_max)
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice173.py
