<<<<<<< HEAD:practice_problem_solutions (2026)/practice308.py
# CodeWars - Convert PascalCase string into snake_case

def to_underscore(strng: str) -> str:
    words = []
    temp = ""
    for c in str(strng):
        if c.isupper() and temp:
            words.append(temp)
            temp = c
        else:
            temp += c
    if temp:
        words.append(temp)
    
    return '_'.join(w.lower() for w in words)

print(to_underscore('MoviesAndBooks')) # 'movies_and_books'
print(to_underscore('TestController')) # 'test_controller'
print(to_underscore('App7Test'))       # 'app7_test'
=======
# HackerRank - Drawing Book

def pageCount(n, p):
    pages = [[i, i+1] for i in range(0, n+1, 2)]
    
    cur_min = 0
    for i in range(len(pages)):
        if p in pages[i]:
            cur_min = i
    
    for i, page in enumerate(pages[::-1]):
        if p in page:
            cur_min = min(cur_min, i)
    
    return(cur_min)

print(pageCount(5, 3)) # 1
print(pageCount(6, 2)) # 1
print(pageCount(5, 4)) # 0
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice308.py
