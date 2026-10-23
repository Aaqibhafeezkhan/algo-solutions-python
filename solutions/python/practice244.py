<<<<<<< HEAD:practice_problem_solutions (2026)/practice244.py
# Max Consecutive Ones

class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        counts = []

        i = 0
        while i < len(nums):
            count = 0
            j = i
            while j < len(nums) and nums[j] == 1:
                count += 1
                j += 1
            if count > 0:
                counts.append(count)
                i = j
            i += 1
        
        return max(counts) if counts else 0

s = Solution()
print(s.findMaxConsecutiveOnes([1,1,0,1,1,1])) # 3
print(s.findMaxConsecutiveOnes([1,0,1,1,0,1])) # 2
print(s.findMaxConsecutiveOnes([0,0,0,0,0,0])) # 0
print(s.findMaxConsecutiveOnes([]))            # 0
=======
# CodeWars - Human readable duration format

def format_duration(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    y, d = divmod(d, 365)

    res = ""
    if y > 0:
        res += f"{y} year{'s' if y > 1 else ''}{', ' if any([s,d,h,m]) else ''}"
    if d > 0:
        res += f"{'and ' if all([a<0 for a in [h,m,s]]) and y > 0 else ''}{d} day{'s' if d > 1 else ''}{', ' if any([s,h,m]) else ''}"
    if h > 0:
        res += f"{'and ' if all([a<0 for a in [m,s]]) and any([d, y]) else ''}{h} hour{'s' if h > 1 else ''}"
        if m > 0:
            res += ', ' if s > 0 else ' and '
        elif s > 0:
            res += ' '
    if m > 0:
        res += f"{'and ' if s < 0 and any([y,d,h]) else ''}{m} minute{'s' if m > 1 else ''}{' ' if s > 0 else ''}"
    if s > 0:
        res += f"{'and ' if any([y,d,h,m]) else ''}{s} second{'s' if s > 1 else ''}"

    return res if res else 'now'

print(format_duration(62))         # 1 minute and 2 seconds
print(format_duration(31_556_926)) # 1 year and 1 second
print(format_duration(132030240))  #"4 years, 68 days, 3 hours and 4 minutes"
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice244.py
