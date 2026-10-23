<<<<<<< HEAD:practice_problem_solutions (2026)/practice209.py
# Minimum Distance to the Target Element

class Solution(object):
    def getMinDistance(self, nums, target, start):
        closest = float('inf')
        for i in range(start, len(nums)):
            if nums[i] == target:
                closest = min(closest, abs(start - i))
        
        for i in range(start, -1, -1):
            if nums[i] == target:
                closest = min(closest, abs(start - i))
        
        return closest
=======
# CodeWars - The Supermarket Queue

def queue_time(customers, n):
    
    queus = [0] * n
    
    for t in customers:
        i = queus.index(min(queus))
        queus[i] += t
    
    return max(queus)

print(queue_time([5,3,4], 1)) # 12
print(queue_time([10,2,3,3], 2)) # 10
print(queue_time([2,3,10], 2)) # 12
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice209.py
