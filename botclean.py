#!/usr/bin/python

# Head ends here
def dist(pos1, pos2):
    return abs(pos1[0]-pos2[0])+abs(pos1[1]-pos2[1])

def next_move(posr, posc, board):
    #check current cell is clean or dirty
    if board[posr][posc]=='d':
        print("CLEAN")
    else:
        min_d = len(board)*len(board)
        min_d_pos = None
        #determine nearest dirty cell to move to
        for rowid in range(len(board)):
            for colid in range(len(board)):
                if board[rowid][colid] == 'd':
                    posdiff = dist([posr,posc],[rowid,colid])
                    if posdiff<min_d:
                        min_d = posdiff
                        min_d_pos = [rowid,colid]
                    
        #minimize move distance to chosen 'd'
        min_dt = min_d
        move = "None"
        d1 = dist([posr,posc+1],min_d_pos)
        d2 = dist([posr,posc-1],min_d_pos)
        d3 = dist([posr+1,posc],min_d_pos)
        d4 = dist([posr-1,posc],min_d_pos)
        if d1 < min_dt:
            min_dt = d1
            print('RIGHT')
        elif d2 < min_dt:
            print('LEFT')
        elif d3 < min_dt:
            print('DOWN')
        elif d4 < min_dt:
            print('UP')
                
    

# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)