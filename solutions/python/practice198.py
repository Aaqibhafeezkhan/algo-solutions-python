<<<<<<< HEAD:practice_problem_solutions (2026)/practice198.py
# HackerRank - Find Digits

def findDigits(n):
    div = n
    count = 0
    while n > 0:
        cur = n % 10
        if cur != 0 and div % cur == 0:
            count += 1
        n //= 10
    
    return count

print(findDigits(12)) # 2
=======
# Valid Braces

def valid_braces(string):
    brace = {
        '}': '{',
        ']': '[',
        ')': '('
    }
    
    seen = []
    
    for c in string:
        if seen and c in brace and brace[c] == seen[-1]:
            seen.pop()
            continue
        seen.append(c)
    return not seen

# Clever Solution From CodeWars
def validBraces(s):
  while '{}' in s or '()' in s or '[]' in s:
      s=s.replace('{}','')
      s=s.replace('[]','')
      s=s.replace('()','')
  return s==''

print(valid_braces('()'))      # True
print(valid_braces('(){}[]'))  # True
print(valid_braces('([{}])'))  # True
print(valid_braces('(}'))      # False
print(valid_braces('[(])'))    # False
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice198.py
