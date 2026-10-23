<<<<<<< HEAD:practice_problem_solutions (2026)/practice241.py
# Counting Words With a Given Prefix

class Solution:
    def prefixCount(self, words, pref: str) -> int:
        count = 0
        for word in words:
            if word.startswith(pref):
                count += 1
        return count

s = Solution()
print(s.prefixCount(["leetcode","win","loops","success"], 'code'))  # 0
print(s.prefixCount(["pay","attention","practice","attend"], 'at')) # 2
=======
# Design Parking System

class ParkingSystem(object):

    def __init__(self, big, medium, small):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType):
        if carType == 1 and self.big > 0:
            self.big -= 1
            return True
        elif carType == 2 and self.medium > 0:
            self.medium -= 1
            return True
        elif carType == 3 and self.small > 0:
            self.small -= 1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice241.py
