<<<<<<< HEAD:practice_problem_solutions (2026)/practice170.py
# Coin Change (Minimum Coins)

def change(n):
    coins = [50, 20, 10, 5, 1]
    change = []
    while n > 0:
        for coin in coins:
            if coin <= n:
                n -= coin
                change.append(coin)
                break
    return change


print(change(25))
print(change(15))
print(change(45))
=======
# How Broke Are You?

def broke_count(exp):
    n = len(exp)
    i = 0
    count = 0
    while i < n:
        temp = 0
        if (n - i) >= 7:
            if all(j <= 10 for j in exp[i:i+7]):
                count += 1
                i += 7
                continue
        if (n - i) >=  3:
            if all(j <= 7 for j in exp[i:i+3]):
                count += 1
                i += 3
                continue
        if exp[i] <= 3:
            count += 1
        i += 1
    return count
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice170.py
