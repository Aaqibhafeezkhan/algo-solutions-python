<<<<<<< HEAD:practice_problem_solutions (2026)/practice174.py
# Decompress Run-Length Encoded List

class Solution(object):
    def decompressRLElist(self, nums):
        arr = []

        for i in range(0, len(nums) - 1, 2):
            arr.extend([nums[i + 1]] * nums[i])
        
        return arr
    
s = Solution()
print(s.decompressRLElist([1,2,3,4])) # [2,4,4,4]
print(s.decompressRLElist([1,1,2,3])) # [1,3,3]
=======
# HackerRank - Merge the Tools!

def merge_the_tools(string, k):
    pairs = []
    
    i = 0
    while i < len(string):
        temp = ''
        if (i + k) >= len(string):
            temp = string[i:]
        else:
            temp = string[i:i+k]
        
        seen = []
        for c in temp:
            if seen and c in seen:
                continue
            seen.append(c)
        pairs.append(''.join(seen))
        
        i += k
        
    return '\n'.join(pairs)

print(merge_the_tools('AABCAAADA', 3)) # AB\nCA\nAD
print(merge_the_tools('AAABBBCCC', 3)) # AB\nBC\nC
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice174.py
