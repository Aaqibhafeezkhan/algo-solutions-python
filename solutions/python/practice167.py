<<<<<<< HEAD:practice_problem_solutions (2026)/practice167.py
# FizzBuzz with Twist

def fizzbuzzpop(n):
    res = ""
    if n % 3 == 0:
        res += 'Fizz'
    if n % 5 == 0:
        res += 'Buzz'
    if n % 7 == 0:
        res += 'Pop'
    return res

print(fizzbuzzpop(9))
print(fizzbuzzpop(10))
print(fizzbuzzpop(15))
print(fizzbuzzpop(49))
=======
# Display the First Three Rows

import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.iloc[0:3]
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice167.py
