<<<<<<< HEAD:practice_problem_solutions (2026)/practice157.py
# Count Digit Appearances

class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        count = 0
        for num in map(str, nums):
            count += num.count(str(digit))
        return count

s = Solution()
print(s.countDigitOccurrences([12,54,32,22], 2)) # 4
print(s.countDigitOccurrences([3], 1))           # 0
=======
# Split a String in Balanced Strings

class Solution(object):
    def balancedStringSplit(self, s):
        
        count = 0

        r_count = 0
        l_count = 0

        for c in s:
            if c == 'R':
                r_count += 1
            elif c == 'L':
                l_count += 1
            
            if r_count == l_count:
                count += 1
                r_count = 0
                l_count = 0
        return count

s = Solution()
print(s.balancedStringSplit("RLRRLLRLRL"))
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice157.py
