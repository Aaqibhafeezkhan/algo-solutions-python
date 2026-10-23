<<<<<<< HEAD:practice_problem_solutions (2026)/practice193.py
# Check if the Sentence Is Pangram

class Solution(object):
    def checkIfPangram(self, sentence):
        alp = [chr(i) for i in range(97, 123)]
        for c in alp:
            if c not in sentence:
                return False
        return True

s = Solution()
print(s.checkIfPangram("thequickbrownfoxjumpsoverthelazydog")) # True
print(s.checkIfPangram("leetcode"))                            # False
=======
# Ho Ho Ho with Functions!

def ho(x = None):
    if not x:
        return "Ho!"
    return "Ho " + x

print(ho())             # Ho!
print(ho(ho(ho())))     # Ho Ho Ho!
print(ho(ho(ho(ho())))) # Ho Ho Ho Ho!
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice193.py
