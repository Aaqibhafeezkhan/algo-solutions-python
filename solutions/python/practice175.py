<<<<<<< HEAD:practice_problem_solutions (2026)/practice175.py
# Count Items Matching a Rule

class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        matches = 0
        rules = {
            'type': 0,
            'color': 1,
            'name': 2
        }
        for item in items:
            if item[rules[ruleKey]] == ruleValue:
                matches += 1
        return matches
    
s = Solution()
print(s.countMatches([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], "color", "silver")) # 1
print(s.countMatches([["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], "type", "phone")) # 2
=======
# HackerRank - Decorators 2 - Name Directory

def person_lister(f):
    def inner(people):
        people.sort(key=lambda x: int(x[2]))
        return [f(p) for p in people]
    return inner
    
@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice175.py
