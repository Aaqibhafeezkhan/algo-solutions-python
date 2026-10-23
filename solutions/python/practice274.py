<<<<<<< HEAD:practice_problem_solutions (2026)/practice274.py
# HackerRank - ACM ICPC Team

def acmTeam(topic):
    n = len(topic)
    max_t = 0
    counts = 0
    
    for i in range(n):
        for j in range(i+1, n):
            
            known = sum(1 for a, b in zip(topic[i], topic[j]) if a == '1' or b == '1')
            
            if known > max_t:
                max_t = known
                counts = 1
            elif known == max_t:
                counts += 1
    return [max_t, counts]

print(acmTeam(['11101', '10101', '11001', '10111', '10000', '11010', '00010', '01010'])) # [5, 9]
print(acmTeam(['10101', '11100', '11010', '00101'])) # [5, 2]
print(acmTeam(['10101', '11110', '00010'])) # [5, 1]
  
=======
# Keyboard Row

class Solution(object):
    def findWords(self, words):
        row1="qwertyuiop"
        row2="asdfghjkl"
        row3="zxcvbnm"
        arr = []
        for word in words:
            cur = None
            for c in word.lower():
                if not cur:
                    if c in row1:
                        cur = 1
                    elif c in row2:
                        cur = 2
                    elif c in row3:
                        cur = 3
                if cur == 1 and c not in row1:
                    cur = None
                    break
                if cur == 2 and c not in row2:
                    cur = None
                    break
                if cur == 3 and c not in row3:
                    cur = None
                    break
            if cur:
                arr.append(word)
        return arr

s = Solution()
print(s.findWords(["Aasdfghjkl","Qwertyuiop","zZxcvbnm"])) # ["Aasdfghjkl","Qwertyuiop","zZxcvbnm"]
print(s.findWords(["Hello","Alaska","Dad","Peace"]))       # ["Alaska","Dad"]
print(s.findWords(["adsdf","sfd"]))                        # ["adsdf","sfd"]
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice274.py
