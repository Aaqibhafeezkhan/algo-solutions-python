<<<<<<< HEAD:practice_problem_solutions (2026)/practice210.py
# HackerRank - Day of the Programmer

def dayOfProgrammer(year):
    if year < 1919:
        days = 243 if year % 4 != 0 else 244
    else:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            days = 244
        else:
            days = 243
    
    if year == 1918:
        days -= 13
=======
def to_weird_case(words):
    res = []
    for word in words.split():
        temp = []
        for i in range(len(word)):
            if i % 2 == 0:
                temp.append(word[i].upper())
            else:
                temp.append(word[i].lower())
        res.append(''.join(temp))
    return ' '.join(res)

print(to_weird_case('This'))           # 'ThIs'
print(to_weird_case('THIs iS a TEST')) # 'ThIs Is A TeSt'
print(to_weird_case('Weird string case')) # 'WeIrD StRiNg CaSe'
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice210.py
