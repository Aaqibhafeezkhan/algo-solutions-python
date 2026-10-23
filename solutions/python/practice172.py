<<<<<<< HEAD:practice_problem_solutions (2026)/practice172.py
# Word Ladder
# TODO


def word_ladder(word):
    pass

dictionary = {"hot", "dot", "dog", "lot", "log", "cog"}
print(word_ladder("hit", "cog", dictionary))  # 5
=======
# HackerRank - Company Logo

from collections import Counter
if __name__ == '__main__':
    s = input()
    
    arr = Counter(s)
    srt = sorted(arr, key=lambda x: (-arr[x], x))[:3]
    
    for ch in srt:
        print(ch, arr[ch])

>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice172.py
