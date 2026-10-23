<<<<<<< HEAD:practice_problem_solutions (2026)/practice185.py
# CodeWars - Help the bookseller !

def stock_list(stocklist, categories):
    
    cur = dict(zip(categories, [0] * len(categories)))
    
    for stock in stocklist:
        name, count = stock.split()
        if name[0] in cur:
            cur[name[0]] += int(count)
        
    return " - ".join(f"({cat} : {val})" for cat, val in cur.items()) if stocklist else ''
=======
# Range Sum of BST

from collections import deque
class Solution(object):
    def rangeSumBST(self, root, low, high):
        queue = deque([root])
        res = []
        while queue:
            node = queue.popleft()
            res.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
        return sum(num for num in res if num >= low and num <= high)
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice185.py
