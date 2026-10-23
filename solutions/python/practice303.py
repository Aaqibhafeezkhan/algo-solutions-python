<<<<<<< HEAD:practice_problem_solutions (2026)/practice303.py
def correct_polish_letters(st): 
    polish = {
        "ą": "a",
        "ć": "c",
        "ę": "e",
        "ł": "l",
        "ń": "n",
        "ó": "o",
        "ś": "s",
        "ź": "z",
        "ż": "z",
    }
    res = ""
    for c in st:
        res += polish.get(c, c)
    return res

print(correct_polish_letters("Maria Skłodowska-Curie"))  # "Maria Sklodowska-Curie"
print(correct_polish_letters("Jędrzej Błądziński"))      # "Jedrzej Bladzinski"
print(correct_polish_letters("Lech Wałęsa"))             # "Lech Walesa"
=======
# Longest Increasing Subsequence

def lis(arr):
    ar = []

    for i in range(len(arr) - 1):
        temp = [arr[i]]
        for j in range(i + 1, len(arr)):
            if temp[-1] < arr[j]:
                temp.append(arr[j])
            else:
                temp[-1] = arr[j]
        ar.append(temp)

    return len(max(ar, key=len))

print(lis([3,1,8,2,5]))       # 3
print(lis([5,2,8,6,3,6,9,5])) # 4
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice303.py
