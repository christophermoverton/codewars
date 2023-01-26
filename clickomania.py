#!/bin/python
# this script uses solution searches dfs with limitation on next Move recursion while varying move
# parameters.  Move parameters consist of running top to bottom, left to right
# x param determined possible moves and updating board before running nextMove sim
# Also x params is computed per depth recursion with falloff.  for instance,
#  n recursion param = recursion param (number of moves till recursion call) * y (decay or growth param),
# computed with y < 1 decays n recursion param to zero with large N nextMove recursion
# By varying recursion params for move calls, one can test for solve within range
# and more rapid convergence of solutions within desired block remainder ranges.
# This limits computational expenditure for complete dfs which on 20x10 grid
# is cumbersome with larger n colors.  Worth noting: all permutation attempts 
# at solutions for dfs attempt to minimize remaining blocks while reducing 
# computational load for possible grid configurations may not 
# easily solve say to 0 remaining blocks if a dfs solution is say 1 tree path
# relative total n tree paths and n is a very large number.
# Unfortunately with high move complexity a single move and nextMove recursion with 
# high color complexity signifcantly encumbers dfs and remaining block minimization
# for game completion return results in a timely manner (for 3 and 4th test case),
# testing bot administrator loses our bot's game.  Hence motivation for 
# rapid dfs convergence to desired remaining block ranges if any exist.
# At present this script is better to solve known puzzle where solution template
# can be applied for hackkerank test credit since it is still too slow 
# to work as a real time ai bot sim in choosing moves.  One can reduce computational
# processing time for known puzzles refining parameters search parameters, as has already 
# been done in this code example at line 243 and 244 with vals1 and vals2 parameters.

  
import sys
sys.setrecursionlimit(15000)
def grid_updater(move, x,y, grid):
    # grid copy for grid update return 
    ugrid = [[grid[i][j] for j in range(y)] for i in range(x)] 
    mx,my = move
    mcolor = grid[mx][my]
    if mcolor == '-':
        #print('invalid move.')
        return [False,ugrid] 
    #iterate color group removal from move choice
    remove = [move]
    valid_mv = False
    while remove:
        pmove = remove.pop()
        mx,my = pmove
        count = 0
        #check top left right 
        #note: move choice is always bottom or right most choice
        # in group, so check moves to top, left and right
        if mx-1 >= 0:
            if ugrid[mx-1][my]==mcolor:
                ugrid[mx-1][my]='-'
                remove.append((mx-1,my))
                count+=1
        if my-1 >= 0:
            if ugrid[mx][my-1]==mcolor:
                ugrid[mx][my-1]='-'
                remove.append((mx,my-1))
                count+=1
        if my+1 < y:
            if ugrid[mx][my+1]==mcolor:
                ugrid[mx][my+1]='-'
                remove.append((mx,my+1))
                count+=1
        if mx+1 < x:
            if ugrid[mx+1][my]==mcolor:
                ugrid[mx+1][my]='-'
                remove.append((mx+1,my))
                count+=1
        if count >=1 and move == pmove:
            ugrid[mx][my] = '-'
            valid_mv = True
    if not valid_mv: 
        return [False,grid]
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
    return [valid_mv,ugrid]
global MAX_ITERATIONS 
MAX_ITERATIONS = 2000
def nextMove_test(x, y, color, grid, nested, recurs_param, dgparam, max_iterations):
    grid_dict = {}
    nrecurs_param = recurs_param*dgparam
    max_count = 0
    max_pos = None
    moves = {}
    group_id_iter = 0
    colors = {}
    # search for all present board moves that is where moves remove 2 or more blocks
    # these board moves are keyed by group id, ideally to remove duplicate moves 
    # that remove the same set of blocks  (hashing accomplishes this)
    #grid_dict[(0,0)]={'color':grid[0][0],count:1}
    for i in range(x):
        for j in range(y):
            lcount = 0
            group_id = group_id_iter
            if not grid[i][j] in colors:
                colors[grid[i][j]] = 1
            else:
                colors[grid[i][j]] +=1
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
    minbcount = 9e9
    minmove = None 
    movelist = []
    minmovelist = []
    movelist_e = []
    # if not nested:
    #     print(colors)
    if not len(moves) == 0:
        highcountmoves = 0
        ugrid = [[grid[i][j] for j in range(y)] for i in range(x)] 
        recurs_after_moves = 0
        for group_id in moves:
            # if not nested:
            #     print('move:'+str(group_id))
            move = moves[group_id]
            mv_valid,ugrid  = grid_updater(move,x,y,ugrid)
            if mv_valid:
                movelist.append(move)
            if recurs_after_moves > recurs_param:
                rbcount,movelist_e = nextMove_test(x,y,color,ugrid,True, nrecurs_param,dgparam,max_iterations)
                if rbcount >= 0:
                    max_iterations[0] +=1
                if rbcount < minbcount:
                    minbcount = rbcount
                    minmove = move
                    movelistc = movelist[0:]
                    movelistc.extend(movelist_e)
                    minmovelist = movelistc[0:]
                movelist = []
                ugrid = [[grid[i][j] for j in range(y)] for i in range(x)] 
                recurs_after_moves = 0
                # if rbcount <= 14:
                #     print(rbcount)
            recurs_after_moves+=1
            if max_iterations[0] >= MAX_ITERATIONS:
                break
                # if minbcount <= 10:
                #     print(minbcount)
                # if (rbcount == 0 and nested) or (rbcount >=1 and nested and highcountmoves > 0):
                #     #print(rbcount)
                #     break
                # elif (rbcount == 0 and not nested) or (rbcount >=1 and not nested and highcountmoves > 41):
                #     print(rbcount)
                #     break
        rbcount = 9e9
        if max_iterations[0] < MAX_ITERATIONS:
            rbcount,movelist_e = nextMove_test(x,y,color,ugrid,True,nrecurs_param,dgparam,max_iterations)
        if rbcount >= 0:
            highcountmoves +=1
            max_iterations[0]+=1
        if rbcount < minbcount:
            minbcount = rbcount
            minmove = move
            movelistc = movelist[0:]
            movelistc.extend(movelist_e)
            minmovelist = movelistc[0:]
        # if rbcount <= 14:
        #     print(rbcount)
    else:
        #return number of blocks left
        bcount = 0
        for i in range(x):
            for j in range(y):
                if not grid[i][j] == '-':
                    bcount +=1
        return [bcount,[]]
    
    if not nested:
        return [minbcount,minmovelist,minmove]
        #print(minbcount)
        #print(minmovelist)
        #print(sstr(minmove[0])+" "+str(minmove[1]))
    else:
        #print(minbcount)
        #print(str(minmove[0])+" "+str(minmove[1]))
        #movelist.append(minmove)
        return [minbcount,minmovelist[0:]]   
    #print(str(max_pos[0])+" "+str(max_pos[1]))
    #print ""

def nextMove(x, y, color, grid):
    minb = 9e9
    minbmoves = []
    minbmove = None
    minrankval1 = []
    vals1 = [20]  #number of attempted moves before recursing nextMove simulation
    vals2 = [-1]
    val2inc = .005
    refined = 0 
    global MAX_ITERATIONS
    MAX_ITERATIONS = 400
    while refined < 1:
        for i,val1 in enumerate(vals1):
            if vals2[i] < 0:
                #decay parameter setting
                val2 = 1.0
                for j in range(100):
                    res = nextMove_test(x, y, color, grid, nested=False, recurs_param=val1, dgparam= val2,max_iterations=[0])
                    bcount, movlist, mov = res
                    if bcount <= minb:
                        pminb = minb
                        minb = bcount
                        
                        print(minb)
                        if bcount < pminb:
                            minbmoves = [movlist[0:]]
                            minrankval1 = [val1]
                        else:
                            if not val1 in minrankval1:
                                minbmoves.append(movlist[0:])
                                minrankval1.append(val1)
                        minbmove = mov
                        #minrankval1 = val1
                    val2 -= val2inc
                    if j % 10 == 0:
                        print(str(j/10*10)+"percent complete for" +str(val1))
            if vals2[i] > 0:
                #growth parameter setting
                val2 = 1.0
                for j in range(100):
                    res = nextMove_test(x, y, color, grid, nested=False, recurs_param=val1, dgparam= val2,max_iterations=[0])
                    bcount, movlist, mov = res
                    if bcount <= minb:
                        pminb = minb
                        minb = bcount
                        print(minb)
                        if bcount < pminb:
                            minbmoves = [movlist[0:]]
                            minrankval1 = [val1]
                        else:
                            
                            if not val1 in minrankval1:
                                minbmoves.append(movlist[0:])
                                minrankval1.append(val1)
                        minbmove = mov
                        
                        #minrankval1 = val1
                    val2 += val2inc
                    if j % 10 == 0:
                        print(str(j/10*10)+"percent complete for" +str(val1))
        # refine search
        # set search to radius about minrankval1
        vals1 = []; radius = 1; vals2 = [-1]*(radius*2+1)*(len(minrankval1))
        
        for val1 in minrankval1:
            for i in range(val1-radius,val1+radius+1):
                vals1.append(i)
        # minrankval1 = []
        # minbmoves = []
        MAX_ITERATIONS = 750
        refined +=1
    print(minb)
    print(minbmoves)
    print(minbmove)
    ugrid = [[grid[i][j] for j in range(y)] for i in range(x)] 
    minmoves = minbmoves[0]
    for move in minmoves:
        vmov,ugrid = grid_updater(move,x,y,ugrid)
        print(vmov)
        print(ugrid)

#if name == 'main':
import testcase_clickomania
x,y,k = [ int(i) for i in input().strip().split() ] 
grid = [[i for i in str(input().strip())] for _ in range(x)] 
nextMove(x, y, k, grid)