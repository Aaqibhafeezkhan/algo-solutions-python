<<<<<<< HEAD:practice_problem_solutions (2026)/practice246.py
# Find the Difference of Two Arrays

class Solution:
    def findDifference(self, nums1, nums2):
        return [[num for num in set(nums1) if num not in nums2], [num for num in set(nums2) if num not in nums1]]
    
s = Solution()
print(s.findDifference([1,2,3], [2,4,6])) # [[1,3], [4,6]]
print(s.findDifference([1,2,3,3], [1,1,2,2])) # [[3], []]
print(s.findDifference([1,2,3], [1,2,3])) # [[], []]
=======
# CodeWars - String incrementer


def increment_string(string):
    if not string:
        return "1"
    
    ch = ""
    dg = ""
    for i in range(len(string) - 1, -1, -1):
        if not string[i].isdigit():
            ch = string[:i+1]
            break
        dg += string[i]
    
    dg = dg[::-1]
    
    inc = str(int(dg if dg else '0') + 1)
    lead = 0
    while dg and dg[0] == '0' and len('0' * lead + inc) != len(dg):
        lead += 1

    return ch + '0' * lead + str(inc)

print(increment_string("foobar001"))  # "foobar002"
print(increment_string("foobar00"))   # "foobar01"
print(increment_string("foobar99"))   # "foobar100"
print(increment_string("foobar099"))  # "foobar100"
print(increment_string("fo99obar99")) # "fo99obar100"
print(increment_string(""))           # "1"
print(increment_string("foo"))           # "foo1"
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice246.py
