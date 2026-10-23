<<<<<<< HEAD:practice_problem_solutions (2026)/practice156.py
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
=======
# Unique Morse Code Words

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = []
        for word in words:
            temp = ""
            for c in word:
                temp += morse[ord(c.lower()) - 97]
            res.append(temp)
        print(res)
        return len(set(res))

s = Solution()
print(s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
print(s.uniqueMorseRepresentations(["a"]))
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice156.py
