<<<<<<< HEAD:practice_problem_solutions (2026)/practice219.py
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
=======
# CodeWars - The Vowel Code

vowels = 'aeiou'

def encode(st):
    res = ''
    for c in st:
        if c in vowels:
            res += str(vowels.index(c) + 1)
        else:
            res += c
    return res

def decode(st):
    res = ''
    for c in st:
        if c.isdigit() and 0 < int(c) <= 5:
            res += vowels[int(c) - 1]
        else:
            res += c
    return res

print(encode('hello')) # h2ll4
print(encode('h2ll4')) # h2ll4
print(encode('How are you today?')) # H4w 1r2 y45 t4d1y?

print(decode('h2ll4')) # hello
print(decode('How are you today?')) # How are you today?
print(decode('H4w 1r2 y45 t4d1y?')) # How are you today?
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice219.py
