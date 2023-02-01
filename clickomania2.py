#!/bin/python
def grid_updater(move, x,y, grid):
    # grid copy for grid update return 
    ugrid = [[grid[i][j] for j in range(y)] for i in range(x)] 
    mx,my = move
    mcolor = grid[mx][my]
    #iterate color group removal from move choice
    remove = [move]
    while remove:
        mx,my = remove.pop()
        #check top left right 
        #note: move choice is always bottom or right most choice
        # in group, so check moves to top, left and right
        if mx-1 >= 0:
            if ugrid[mx-1][my]==mcolor:
                ugrid[mx-1][my]='-'
                remove.append((mx-1,my))
        if my-1 >= 0:
            if ugrid[mx][my-1]==mcolor:
                ugrid[mx][my-1]='-'
                remove.append((mx,my-1))
        if my+1 < y:
            if ugrid[mx][my+1]==mcolor:
                ugrid[mx][my+1]='-'
                remove.append((mx,my+1))
        if mx+1 < x:
            if ugrid[mx+1][my]==mcolor:
                ugrid[mx+1][my]='-'
                remove.append((mx+1,my))
    #iterate move of all upper tiles
    # find down tile empty 
    update = []
    for i in range(x):
        for j in range(y):
            if i + 1 < x:
                if not ugrid[i][j] == '-' and ugrid[i+1][j] == '-':
                    update.append((i,j))
    while update:
        move = update.pop()
        mx,my = move
        if mx+1 < x:
            if ugrid[mx+1][my] == '-':
                ugrid[mx+1][my] = ugrid[mx][my]
                ugrid[mx][my] = '-'
                if mx -1 >= 0 and not ugrid[mx-1][my] == '-':
                    update.append((mx-1,my))
                if mx + 2 < x and ugrid[mx+2][my] == '-':
                    update.append((mx+1,my))
    # check no open columns otherwise update ugrid
    for j in range(y):
        if ugrid[x-1][j] == '-' and j +1 < y and not ugrid[x-1][j+1] == '-':
            update.append((x-1,j+1))
    update.reverse()
    while update:
        move_column = update.pop()
        mov_x,mov_y = move_column
        for mx in range(x):
            ugrid[mx][mov_y-1] = ugrid[mx][mov_y]
            ugrid[mx][mov_y] = '-'
        if mov_y+1 < y and not ugrid[x-1][mov_y+1] == '-':
            update.append((x-1,mov_y+1)) 
    return ugrid

def nextMove(x, y, color, grid, nested,minbcount):
    grid_dict = {}
    max_count = 0
    max_pos = None
    moves = {}
    group_id_iter = 0
    #grid_dict[(0,0)]={'color':grid[0][0],count:1}
    for i in range(x):
        for j in range(y):
            lcount = 0
            group_id = group_id_iter
            if not grid[i][j] == '-':
                prevgid = False
                if i-1 >= 0:
                    if (i-1,j) in grid_dict and grid_dict[(i-1,j)]['color']==grid[i][j]:
                        lcount = grid_dict[(i-1,j)]['count']
                        group_id = grid_dict[(i-1,j)]['group_id']
                        prevgid = True
                if j-1 >= 0:
                    #check left
                    if (i,j-1) in grid_dict and grid_dict[(i,j-1)]['color']==grid[i][j]:
                        if prevgid:
                            if not group_id == grid_dict[(i,j-1)]['group_id']:
                                pgid = grid_dict[(i,j-1)]['group_id']
                                #update j-1 gid 
                                grid_dict[(i,j-1)]['group_id'] = group_id
                                lcount += grid_dict[(i,j-1)]['count'] 
                                if pgid in moves:
                                    del moves[pgid]
                        else:
                            lcount = grid_dict[(i,j-1)]['count']
                            group_id = grid_dict[(i,j-1)]['group_id']
                lcount+=1
                grid_dict[(i,j)] = {'color':grid[i][j],'count':lcount,'group_id':group_id}
                if lcount > max_count:
                    max_count = lcount
                    max_pos = (i,j)
                if lcount > 1:
                    moves[group_id] = (i,j)
                if group_id == group_id_iter:
                    group_id_iter+=1
    # check optimal move in moves using recursion
    #minbcount_e = minbcount[0]
    rbcount = 9e9
    minmove = None 
    if not len(moves) == 0:
        for group_id in moves:
            move = moves[group_id]
            ugrid = grid_updater(move,x,y,grid)
            rbcount = nextMove(x,y,color,ugrid,True,minbcount)
            if rbcount < minbcount[0]:
                minbcount[0] = rbcount
                minmove = move
                print(minbcount[0])
            if rbcount == 0 and nested:
                return rbcount
            elif rbcount == 0 and not nested:
                break
    else:
        #return number of blocks left
        bcount = 0
        for i in range(x):
            for j in range(y):
                if not grid[i][j] == '-':
                    bcount +=1
        return bcount
    
    if not nested:
        #print(minbcount)
        print(str(minmove[0])+" "+str(minmove[1]))
    else:
        return minbcount[0]    
    #print(str(max_pos[0])+" "+str(max_pos[1]))
    #print ""

#if name == 'main':
import testcase_clickomania2
x,y,k = [ int(i) for i in input().strip().split() ] 
grid = [[i for i in str(input().strip())] for _ in range(x)] 
nextMove(x, y, k, grid,False,[9e9])