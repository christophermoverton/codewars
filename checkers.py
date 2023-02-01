#One can update this algorithm, so that board and rank states are saved with 
#several bot versus opponents are moved then ranked.  That is to simulate
#where board state and rank are tied amongst multiple move 
# choices in capture or non capture situations.  You may consider
# also implementing a skill level on the opponent if simulating any number
# of moves in advance for move optimization.  For instance,
# a skill level could be a mattter of having the AI bot not always choosing
# the best ranked board state (per opponent perspective) move, but instead
# alternate lesser ranked moves.  This bot alogrithm is a much simpler
# not as 'smart' implementation since this only optimizes by first serve
# highest rank board state choice for current board state.  Does not optimize
# per simulating multiple moves in advance (outcomes).   
def get_capture_pos(pos,move):
    cap_x = pos[0]+(move[0]-pos[0])/2
    cap_y = pos[1]+(move[1]-pos[1])/2
    return [int(cap_x),int(cap_y)]

def update_board(move_num, pos, moves, board):
    #assumed move validation
    board_c = [[board[i][j] for j in range(8)] for i in range(8)]
    if move_num == 1:
        #get pos color
        pcolor = board[pos[0]][pos[1]]
        npos = moves[0]
        board_c[pos[0]][pos[1]] = '_'
        board_c[npos[0]][npos[1]] = pcolor
    else:
        #capture moves
        pcolor = board[pos[0]][pos[1]]
        board_c[pos[0]][pos[1]] = '_'
        nmov = pos
        for move in moves:
            cap_pos = get_capture_pos(nmov,move)
            nmov = move
            board_c[cap_pos[0]][cap_pos[1]] = '_'
            if pcolor == 'w':
                #check for king move
                if move[0] == 0:
                    #king position
                    pcolor = 'W'
            elif pcolor == 'b':
                if move[0] == 7:
                    pcolor = 'B'
        board_c[moves[-1][0]][moves[-1][1]] = pcolor
    return board_c

def rank_board_state(bot_color,board):
    ocolor = 'w'
    ocolor_king = 'W'
    bot_color_king = 'B'
    if bot_color == 'w':
        ocolor = 'b'
        ocolor_king = 'B'
        bot_color_king = 'W'
    score = 0
    tot_o_color = 0
    tot_b_color = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == ocolor or board[i][j]==ocolor_king:
                tot_o_color +=1 
            elif board[i][j] == bot_color or board[i][j]==bot_color_king:
                tot_b_color +=1

    return tot_b_color-tot_o_color

def get_capture_moves(bot_color,pos, board):
    past_move = []
    next_move = [[pos[0:]]]
    res_moves = []
    pos_color = board[pos[0]][pos[1]]
    if pos_color == 'B':
        bot_color = 'B'
    elif pos_color == 'W':
        bot_color = 'W'
    while next_move:
        x_check = [-1,1]
        y_check = [-1,1]
        if bot_color.isupper():
            # check forwards and backwards diagonally
            
            x_check = [-1,1]
        else:
            # check directionality per bot color
            if bot_color == 'w':
                x_check = [-1]
                y_check = [-1,1]
            elif bot_color == 'b':
                x_check = [1]
                y_check = [-1,1]
        cpos_list = next_move.pop()
        cpos = cpos_list[-1]
        next_move_add = False
        for x_chk in x_check:
            for y_chk in y_check:
                ncpos = [cpos[0]+x_chk,cpos[1]+y_chk]
                if ncpos[0]>7 or ncpos[0] < 0:
                    continue
                if ncpos[1]>7 or ncpos[1]<0:
                    continue                
                ccolor = board[ncpos[0]][ncpos[1]]
                ncpos2 = [cpos[0]+2*x_chk, cpos[1]+2*y_chk]
                if ncpos2[0]>7 or ncpos2[0] < 0:
                    continue
                if ncpos2[1]>7 or ncpos2[1] < 0:
                    continue
                t1 = board[ncpos2[0]][ncpos2[1]] == '_'
                t2 = ncpos2[0] >= 0 and ncpos2[0] <= 7
                t3 = ncpos2[1] >= 0 and ncpos2[1] <= 7
                same_color_capture = False
                if bot_color == 'b' or bot_color == 'B':
                    if ccolor == 'b' or ccolor == 'B':
                        same_color_capture = True
                if bot_color == 'w' or bot_color == 'W':
                    if ccolor == 'w' or ccolor == 'W':
                        same_color_capture = True
                if ccolor == '_':
                    same_color_capture = True
                if t2 and t3 and ncpos2 not in past_move and not same_color_capture and t1:
                    #capture move valid
                    past_move.append(cpos)
                    cpos_listc = cpos_list[0:]
                    cpos_listc.append(ncpos2)
                    next_move.append(cpos_listc)
                    # check valid next move isn't a valid king position
                    t1 = ncpos2[0] == 0 and bot_color == 'w'
                    t2 = ncpos2[0] == 7 and bot_color == 'b'
                    t3 = not bot_color.isupper()
                    if (t3 and t1) or (t3 and t2): 
                        if bot_color == 'w':
                            bot_color = 'W'
                        else:
                            bot_color = 'B'
                    next_move_add = True
        if not next_move_add and len(cpos_list)>1:
            #exhausted all valid move choices for this test position
            #add moves list to return results move list
            res_moves.append(cpos_list)
                    #ress_moves.append(ncpos2)
    return res_moves

def get_non_capture_move(pos, board):
    bot_color = board[pos[0]][pos[1]]
    res_moves = []
    if not bot_color.isupper():
        if bot_color == 'w':
            t1 = pos[1]+1 <= 7
            t2 = pos[1]-1 >= 0
            t3 = pos[0]-1 >= 0
            npos = [pos[0]-1, pos[1]+1]
            npos2 = [pos[0]-1, pos[1]-1]
            if t1 and t3 and board[npos[0]][npos[1]]=='_':
                res_moves.append([pos, npos])
            if t2 and board[npos2[0]][npos2[1]]=='_':
                res_moves.append([pos,npos2])
        elif bot_color == 'b':
            t1 = pos[1]+1 <= 7
            t2 = pos[1]-1 >= 0
            t3 = pos[0]+1 <= 7
            npos = [pos[0]+1, pos[1]+1]
            npos2 = [pos[0]+1, pos[1]-1]
            if t1 and t3 and board[npos[0]][npos[1]]=='_':
                res_moves.append([pos, npos])
            if t2 and t3 and board[npos2[0]][npos2[1]]=='_':
                res_moves.append([pos,npos2])
    else:
        #king position
         xincs = [-1,1]
         yincs = [-1,1]
         for xinc in xincs:
            for yinc in yincs:
                t1 = pos[0]+xinc >= 0 and pos[0]+xinc <= 7
                t2 = pos[1]+yinc >= 0 and pos[1]+yinc <= 7
                npos = [pos[0]+xinc, pos[1]+yinc] 
                if t1 and t2 and board[npos[0]][npos[1]] == '_':
                    res_moves.append([pos,npos])   
    return res_moves      

def get_moves(move_color, board):
    next_moves = []
    ## iterate all color position
    maxboardrank = -9e9
    max_board_move = None
    
    for i in range(0,8):
        for j in range(0,8):
            pos_color = board[i][j]
            if pos_color == 'W':
                pos_color = 'w'
            elif pos_color == 'B':
                pos_color = 'b'
            if pos_color == move_color:
                nc_mvs = get_non_capture_move([i,j],board)
                cap_mvs = get_capture_moves(move_color,[i,j],board)
                if nc_mvs:
                    for nc_mv in nc_mvs:
                        pos,nmv = nc_mv
                        uboard = update_board(1,pos,[nmv],board)
                        rank = rank_board_state(move_color,uboard)
                        if rank > maxboardrank:
                            max_board_move = nc_mv
                            maxboardrank = rank
                            
                if cap_mvs:
                    for cap_mv in cap_mvs:
                        captype = len(cap_mv)-1
                        if captype == 1:
                            captype = 2
                        uboard = update_board(captype,cap_mv[0],cap_mv[1:],board)
                        rank = rank_board_state(move_color,uboard)
                        if rank > maxboardrank:
                            max_board_move = cap_mv
                            maxboardrank = rank
    return max_board_move

import sys 
from io import StringIO
data = u"""b
8
_b_b_b_b
__b_b_b_
_b_b_b_b
__b_w___
________
w_w___w_
_w_w_w_w
w_w_w_w_"""
sys.stdin = StringIO(data)
bot_color = input()
boardsize = int(input())
board = []
board = [[i for i in str(input().strip())] for _ in range(boardsize)] 
board_move = get_moves(bot_color,board)
print(len(board_move)-1)
print(str(board_move[0][0])+' '+str(board_move[0][1]))
for move in board_move[1:]:
    print(str(move[0])+' '+str(move[1]))
                        