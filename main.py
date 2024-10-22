import math
board =[]
for i in range(9):
    row=[]
    for i in range(9):
        row.append(0)
    board.append(row)

def check(x, y, num):
    if num in board[y]:
        return False
    
    for i in board:
        if num == i[x]:
            return False
    
    xsquare = 3*((x//3)+1)
    ysquare = 3*((y//3)+1)

    for k in range(y-3, y):
        for l in range(x-3, x):
            if board[k][l] == num:
                return False
    return True
def solve():
    for a in range(9):
        for b in range(9):
            if board[a][b] == 0:
                for t in range(1, 10):
                     if check(a,b,t):
                        board[a][b] = t

for w in board:
    print(w)