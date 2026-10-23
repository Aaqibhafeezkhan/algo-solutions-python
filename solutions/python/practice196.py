<<<<<<< HEAD:practice_problem_solutions (2026)/practice196.py
# HackerRank - The Minion Game

def minion_game(string):
    st = 0
    ke = 0
    
    for i in range(len(string)):
        score = len(string) - i
        
        if string[i] in 'AEIOU':
            ke += score
        else:
            st += score
        
    if st > ke:
        print('Stuart', st)
    elif st < ke:
        print('Kevin', ke)
    else:
        print('Draw')
=======
# Bouncing Balls

def bouncing_ball(h, bounce, window):
    if h <= 0 or (bounce <= 0 or bounce >= 1) or window >= h:
        return -1
    
    seen = 1
    while h > 0:
        bounce_height = h * bounce
        if bounce_height > window:
            seen += 2
            h = bounce_height
        else:
            break
    return seen

print(bouncing_ball(3, 0.66, 1.5))  # 3
print(bouncing_ball(2, 0.5, 1))     # 1
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice196.py
