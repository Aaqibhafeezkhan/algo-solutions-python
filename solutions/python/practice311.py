<<<<<<< HEAD:practice_problem_solutions (2026)/practice311.py
# py.checkio - Cookies

def get_cookie(cookie, name):
    cont = [word.strip() for word in cookie.split(';')]
    
    for prt in cont:
        key, val = prt.split('=', 1)
        if key == name:
            return val

print(get_cookie("theme=light; sessionToken=abc123", "sessionToken")) # "abc123"
print(get_cookie("theme=light; sessionToken=abc123", "userId"))       # None
print(get_cookie("theme=light; sessionToken=abc123", "theme"))        # "light"
=======
# HackerRank - Non-Divisible Subset

# Other Sol
def nonDivisibleSubset(k, s):
    freq = [0] * k
    for num in s:
        freq[num % k] += 1
    
    count = 0

    if freq[0] > 0:
        count += 1

    for i in range(1, k // 2 + 1):
        if i == k - i:
            if freq[i] > 0:
                count += 1
        else:
            count += max(freq[i], freq[k - i])
    
    return count


print(nonDivisibleSubset(7, list(map(int, "278 576 496 727 410 124 338 149 209 702 282 718 771 575 436".split())))) # 11
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice311.py
