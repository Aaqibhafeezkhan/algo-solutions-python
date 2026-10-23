<<<<<<< HEAD:practice_problem_solutions (2026)/practice304.py
# CodeWars - Strip Comments

def strip_comments(strng, markers):
    arr = [s for s in strng.split('\n')]
    
    for i in range(len(arr)):
        temp = []
        for mark in markers:
            ind = arr[i].find(mark)
            if ind >= 0:
                temp.append(ind)
        if temp:
            arr[i] = arr[i][:min(temp)].rstrip()
    
    return '\n'.join(arr)

print(strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])) # "apples, pears\ngrapes\nbananas")
print(strip_comments("   a #b\nc\nd $e f g", ["#", "$"]))                                 # "   a\nc\nd")
print(strip_comments("a #b\nc\nd $e f g", ["#", "$"]))                                    # "a\nc\nd")
=======
# Minimum Average of Smallest and Largest Elements

class Solution(object):
    def minimumAverage(self, nums):
        arr = []
        nums.sort()
        for i in range(len(nums) // 2):
            av = (nums[i] + nums[len(nums) - i - 1] ) / 2
            arr.append(av)

        return min(arr)

s = Solution()   
print(s.minimumAverage([7,8,3,4,15,13,4,1])) # 5.5
print(s.minimumAverage([1,9,8,3,10,5]))      # 5.5
print(s.minimumAverage([1,2,3,7,8,9]))       # 5.0
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice304.py
