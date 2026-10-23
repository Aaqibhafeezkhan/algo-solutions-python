<<<<<<< HEAD:practice_problem_solutions (2026)/practice216.py
# HackerRank - Equalize the Array

def equalizeArray(arr):
    return len(arr) - arr.count(max(arr, key=lambda x: arr.count(x)))

print(equalizeArray([3,3,2,1,3]))       # 2
print(equalizeArray([1,2,3,1,2,3,3,3])) # 4
=======
# CodeWars - Title Case

def title_case(title, minor_words=''):
    result = []
    minors = [word.lower() for word in minor_words.split()]
    for i, word in enumerate(title.lower().split()):
        if word in minors and i > 0:
            result.append(word.lower())
        else:
            result.append(word.title())
            
    return ' '.join(result)

print(title_case("a clash of KINGS", "a an the of")) # "A Clash of Kings"
print(title_case("THE WIND IN THE WILLOWS", "The In")) # "The Wind in the Willows"
print(title_case("the quick brown fox")) # "The Quick Brown Fox"
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice216.py
