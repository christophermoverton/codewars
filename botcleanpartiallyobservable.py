#!/usr/bin/python3
## two main case structures.  if observable d set waypoint to d pos, otherwise,
## use waypoint routing for counter clockwise movement on the owaypoint ring of the position matrix.
## note: at each move there is a constant change in observable position states.  
# rotation on the ring of the position matrix ensures that all points 
## on the position matrix are observably covered.  
## there are added case structures for points either on or off the rotation
## owaypoint ring.  Also points on the cross of the ring but not on the ring
## are accounted for with the bot directed to the nearest owaypoint.
## the corner vertices of the owaypoint ring are given by owaypoints.


def dist(pos1, pos2):
    return abs(pos1[0]-pos2[0])+abs(pos1[1]-pos2[1])

def next_move(posx, posy, board):
    
    owaypoints = [[3,3],[1,3],[1,1],[3,1]]
    if board[posx][posy]=='d':
        print("CLEAN")
    else:
        min_d = len(board)*len(board)
        min_d_pos = None
        min_d_o = len(board)*len(board)
        min_d_o_pos = None
        #determine nearest dirty cell to move to
        for rowid in range(len(board)):
            for colid in range(len(board)):

                ## see if on way point track 
                t1 = posx == 1 or posx == 3
                t2 = posy == 1 or posy == 3
                if t1 or t2:
                    t1 = posx == 3
                    t2 = posx == 1
                    t3 = posy == 3
                    t4 = posy == 1
                    #if at way point direct to the next waypoint
                    if t1 and t3:
                        min_d_o_pos = owaypoints[1]
                        min_d_o = dist([posx,posy],min_d_o_pos)
                    elif t2 and t3:
                        min_d_o_pos = owaypoints[2]
                        min_d_o = dist([posx,posy],min_d_o_pos)
                    elif t2 and t4:
                        min_d_o_pos = owaypoints[3]
                        min_d_o = dist([posx,posy],min_d_o_pos)
                    elif t1 and t4:
                        min_d_o_pos = owaypoints[0]
                        min_d_o = dist([posx,posy],min_d_o_pos)
                    else:
                        if t1 and posy == 2:
                            min_d_o_pos = owaypoints[0]
                            min_d_o = dist([posx,posy],min_d_o_pos)
                        if t3 and posx == 2:
                            min_d_o_pos = owaypoints[1]
                            min_d_o = dist([posx,posy],min_d_o_pos)
                        if t2 and posy == 2:
                            min_d_o_pos = owaypoints[2]
                            min_d_o = dist([posx,posy],min_d_o_pos)
                        if t4 and posx == 2:
                            min_d_o_pos = owaypoints[3]
                            min_d_o = dist([posx,posy],min_d_o_pos)
                        if posx == 3 and posy == 0:
                            min_d_o_pos = owaypoints[3]
                            min_d_o = dist([posx,posy],min_d_o_pos)
                        if posx == 3 and posy == 4:
                            min_d_o_pos = owaypoints[0]
                            min_d_o = dist([posx,posy], min_d_o_pos)
                        if posx == 1 and posy == 0:
                            min_d_o_pos = owaypoints[2]
                            min_d_o = dist([posx,posy], min_d_o_pos)
                        if posx == 1 and posy == 4:
                            min_d_o_pos = owaypoints[1]
                            min_d_o = dist([posx,posy], min_d_o_pos)
                        if posy == 1 and posx == 0:
                            min_d_o_pos = owaypoints[2]
                            min_d_o = dist([posx,posy], min_d_o_pos)
                        if posy == 1 and posx == 4:
                            min_d_o_pos = owaypoints[3]
                            min_d_o = dist([posx,posy], min_d_o_pos)
                        if posy == 3 and posx == 0:
                            min_d_o_pos = owaypoints[1]
                            min_d_o = dist([posx,posy], min_d_o_pos)
                        if posy == 3 and posx == 4:
                            min_d_o_pos = owaypoints[0]
                            min_d_o = dist([posx,posy], min_d_o_pos)
                        
                else:
                    for opoint in owaypoints:
                        posdiff = dist([posx,posy],opoint)
                        if posdiff < min_d_o:
                            min_d_o = posdiff
                            min_d_o_pos = opoint
                if board[rowid][colid] == 'd':
                    posdiff = dist([posx,posy],[rowid,colid])
                    if posdiff<=min_d:
                        min_d = posdiff
                        min_d_pos = [rowid,colid]

        #minimize move distance to chosen 'd'
        if min_d_pos:
            min_dt = min_d
            move = "None"
            d1 = dist([posx,posy+1],min_d_pos)
            d2 = dist([posx,posy-1],min_d_pos)
            d3 = dist([posx+1,posy],min_d_pos)
            d4 = dist([posx-1,posy],min_d_pos)
            if d1 < min_dt:
                min_dt = d1
                print('RIGHT')
            elif d2 < min_dt:
                print('LEFT')
            elif d3 < min_dt:
                print('DOWN')
            elif d4 < min_dt:
                print('UP')
        else:
            min_dt = min_d_o
            d1 = dist([posx,posy+1],min_d_o_pos)
            d2 = dist([posx,posy-1],min_d_o_pos)
            d3 = dist([posx+1,posy],min_d_o_pos)
            d4 = dist([posx-1,posy],min_d_o_pos)
            if d1 < min_dt:
                min_dt = d1
                print('RIGHT')
            elif d2 < min_dt:
                print('LEFT')
            elif d3 < min_dt:
                print('DOWN')
            elif d4 < min_dt:
                print('UP')

if __name__ == "__main__": 
    pos = [int(i) for i in input().strip().split()] 
    board = [[j for j in input().strip()] for i in range(5)]
    
    next_move(pos[0], pos[1], board)