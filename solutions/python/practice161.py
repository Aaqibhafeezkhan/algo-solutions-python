<<<<<<< HEAD:practice_problem_solutions (2026)/practice161.py
# CodeWars - String incrementer


def increment_string(string):
    if not string:
        return "1"
    
    ch = ""
    dg = ""
    for i in range(len(string) - 1, -1, -1):
        if not string[i].isdigit():
            ch = string[:i+1]
            break
        dg += string[i]
    
    dg = dg[::-1]
    
    inc = str(int(dg if dg else '0') + 1)
    lead = 0
    while dg and dg[0] == '0' and len('0' * lead + inc) != len(dg):
        lead += 1

    return ch + '0' * lead + str(inc)

print(increment_string("foobar001"))  # "foobar002"
print(increment_string("foobar00"))   # "foobar01"
print(increment_string("foobar99"))   # "foobar100"
print(increment_string("foobar099"))  # "foobar100"
print(increment_string("fo99obar99")) # "fo99obar100"
print(increment_string(""))           # "1"
print(increment_string("foo"))           # "foo1"
=======
# Insert Greatest Common Divisors in Linked List

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        
        cur = head
        import math
        while cur and cur.next:
            temp = math.gcd(cur.val, cur.next.val)
            new_node = ListNode(temp, cur.next)
            cur.next = new_node
            cur = new_node.next
        
        return head


def to_linked_list(arr):
    head = ListNode(arr[0])
    temp = head
    for i in range(1, len(arr)):
        temp.next = ListNode(arr[i])
        temp = temp.next
    return head

s = Solution()
print(s.insertGreatestCommonDivisors(to_linked_list([18, 6, 10, 3])))
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice161.py
