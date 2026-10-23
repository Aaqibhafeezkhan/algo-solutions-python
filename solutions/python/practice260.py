<<<<<<< HEAD:practice_problem_solutions (2026)/practice260.py
# Geeksforgeeks - Kth Largest in a Stream

import heapq
class Solution:
    def kthLargest(self, arr, k):
        heap = []
        res = []
        
        for num in arr:
            heapq.heappush(heap, num)
            
            if len(heap) > k:
                heapq.heappop(heap)
            
            if len(heap) < k:
                res.append(-1)
            else:
                res.append(heap[0])
        
        return res

s = Solution()
print(s.kthLargest([1, 2, 3, 4, 5], 2)) # [-1, 1, 2, 3, 4]
print(s.kthLargest([1, 2, 3, 4, 5], 3)) # [-1, -1, 1, 2, 3]
print(s.kthLargest([1, 2, 3, 4, 5], 4)) # [-1, -1, -1, 1, 2]
=======
# Count Items Matching a Rule

class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        matches = 0
        rules = {
            'type': 0,
            'color': 1,
            'name': 2
        }
        for item in items:
            if item[rules[ruleKey]] == ruleValue:
                matches += 1
        return matches
    
s = Solution()
print(s.countMatches([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], "color", "silver")) # 1
print(s.countMatches([["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], "type", "phone")) # 2
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice260.py
