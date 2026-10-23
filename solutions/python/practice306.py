<<<<<<< HEAD:practice_problem_solutions (2026)/practice306.py
# CodeWars - Count IP Addresses

def ips_between(start, end):
    return sum([int(num) * (256 ** (3 - i)) for i, num in enumerate(end.split('.'))]) - sum([int(num) * (256 ** (3-i)) for i, num in enumerate(start.split('.'))])

print(ips_between("10.11.12.13", "10.11.13.0")) # 243
print(ips_between("20.0.0.10", "20.0.1.0"))     # 246
print(ips_between("10.0.0.0", "10.0.0.50"))     # 50
=======
# Sum of All Odd Length Subarrays

class Solution:
    def sumOddLengthSubarrays(self, arr) -> int:
        n = len(arr)
        t = sum(arr)
        
        for i in range(n - 1):
            for j in range(i + 2, n, 2):
                temp = arr[i:j+1]
                print(temp)
                if len(temp) % 2 != 0:
                    t += sum(temp)

        return t
        
s = Solution()
print(s.sumOddLengthSubarrays([1,4,2,5,3])) # 58
print(s.sumOddLengthSubarrays([10,11,12]))  # 66
print(s.sumOddLengthSubarrays([1,2]))       # 3
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice306.py
