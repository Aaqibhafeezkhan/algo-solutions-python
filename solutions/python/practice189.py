<<<<<<< HEAD:practice_problem_solutions (2026)/practice189.py
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
=======
# Count Good Triplets

class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        n = len(arr)
        count = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if abs(arr[i] - arr[j]) > a:
                    continue
                for k in range(j + 1, n):
                    if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        count += 1
        return count

s = Solution()
print(s.countGoodTriplets([3, 0, 1, 1, 9, 7], 7, 2, 3)) # 4
print(s.countGoodTriplets([1, 1, 2, 2, 3], 0, 0, 1)) # 0
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice189.py
