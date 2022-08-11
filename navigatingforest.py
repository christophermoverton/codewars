import numpy as np
from sklearn.neighbors import KDTree
from typing import NamedTuple
import math
import sys

class Point(NamedTuple):
    x: float
    y: float
    
class Circle(NamedTuple):
    ctr: Point
    r:   float

s

class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
        
    def construct_graph(self, nodes, init_graph):
        '''
        This method makes sure that the graph is symmetrical. In other words, if there's a path from node A to B with a value V, there needs to be a path from node B to node A with a value V.
        '''
        graph = {}
        for node in nodes:
            graph[node] = {}
        
        graph.update(init_graph)
        
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
                    
        return graph
    
    def get_nodes(self):
        "Returns the nodes of the graph."
        return self.nodes
    
    def get_outgoing_edges(self, node):
        "Returns the neighbors of a node."
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    
    def value(self, node1, node2):
        "Returns the value of an edge between two nodes."
        return self.graph[node1][node2]

# A class to represent a graph object
class Graph2:
 
    # Constructor
    def __init__(self, edges, n):
 
        # A list of lists to represent an adjacency list
        self.adjList = [[] for _ in range(n)]
 
        # add edges to the directed graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)

# Function to perform DFS traversal on the graph on a graph
def DFS(graph, v, visited):
 
    # mark current node as visited
    visited[v] = True
 
    # do for every edge (v, u)
    for u in graph.adjList[v]:
        # `u` is not visited
        if not visited[u]:
            DFS(graph, u, visited)
 
 
# Check if the graph is strongly connected or not
def isStronglyConnected(graph, n):
 
    # do for every vertex
    for i in range(n):
 
        # to keep track of whether a vertex is visited or not
        visited = [False] * n
 
        # start DFS from the first vertex
        DFS(graph, i, visited)
 
        # If DFS traversal doesn't visit all vertices,
        # then the graph is not strongly connected
        for b in visited:
            if not b:
                return False

def hasConnectedGraph(graph, n, strt, trgt):
    visited = [False] * n
    DFS(graph, strt, visited)
    b = visited[trgt]
    if not b:
        return [False, []]
    return [True,visited]


def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())
 
    # We'll use this dict to save the cost of visiting each node and update it as we move along the graph   
    shortest_path = {}
 
    # We'll use this dict to save the shortest known path to a node found so far
    previous_nodes = {}
 
    # We'll use max_value to initialize the "infinity" value of the unvisited nodes   
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # However, we initialize the starting node's value with 0   
    shortest_path[start_node] = 0
    
    # The algorithm executes until we visit all nodes
    while unvisited_nodes:
        # The code block below finds the node with the lowest score
        current_min_node = None
        for node in unvisited_nodes: # Iterate over the nodes
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
                
        # The code block below retrieves the current node's neighbors and updates their distances
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node
 
        # After visiting its neighbors, we mark the node as "visited"
        unvisited_nodes.remove(current_min_node)
    
    return previous_nodes, shortest_path

def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node
    
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
 
    # Add the start node manually
    path.append(start_node)
    
    print("We found the following best path with a value of {}.".format(shortest_path[target_node]))
    print(path)
    

def internal_bitangents(a: Circle, b:Circle):
    ax,ay = a.ctr
    bx, by = b.ctr
    Va = Vector(ax,ay)
    Vb = Vector(bx,by)
    Vab = Vb.sub(Va)
    Vba = Va.sub(Vb)
    d = Vab.magnitude()
    ar = a.r
    br = b.r
    theta = math.acos((ar+br)/d)
    Vabn = Vab.normalize()
    Vabncpy = Vabn.copy()
    Vabpt = Vabn.mult(ar)
    Cv = Vabpt.rotate(theta)
    C = Va.add(Cv)
    Dv = Vabpt.rotate(-theta)
    D = Va.add(Dv)
    Vban = Vba.normalize()
    Vbapt = Vban.mult(br)
    Vabncpt = Vabncpy.mult(br)
    Fv = Vbapt.rotate(theta)
    ##Fv = Vabncpt.rotate(theta)
    F = Vb.add(Fv)
    Ev = Vbapt.rotate(-theta)
    ##Ev = Vabncpt.rotate(-theta)
    E = Vb.add(Ev)
    return [C, F, D, E]

def external_bitangents(a: Circle, b:Circle):
    ax,ay = a.ctr
    bx, by = b.ctr
    Va = Vector(ax,ay)
    Vb = Vector(bx,by)
    Vab = Vb.sub(Va)
    Vba = Va.sub(Vb)
    d = Vab.magnitude()
    ar = a.r
    br = b.r
    arbr = ar-br
    print(abs(arbr)/d)
    # print(br)
    # print(d)
    theta = math.acos(abs(arbr)/d)
    Vabn = Vab.normalize()
    Vabncpy = Vabn.copy()
    Vabpt = Vabn.mult(ar)
    Cv = Vabpt.rotate(theta)
    C = Va.add(Cv)
    Dv = Vabpt.rotate(-theta)
    D = Va.add(Dv)
    ##Vban = Vba.normalize()
    ##Vbapt = Vban.mult(br)
    Vabptc = Vabncpy.mult(br)
    ##Fv = Vbapt.rotate(theta)
    Fv = Vabptc.rotate(theta)
    F = Vb.add(Fv)
    ##Ev = Vbapt.rotate(-theta)
    Ev = Vabptc.rotate(-theta)
    E = Vb.add(Ev)
    return [C, F, D, E]

def line_of_sight(a: Vector, b: Vector, c:Circle):
    cvec = Vector(c.ctr.x, c.ctr.y)
    ca = cvec.sub(a)
    ba = b.sub(a)
    cadotba = ca.dot(ba)
    badotba = ba.dot(ba)
    u = cadotba/badotba
    v1 = ba.mult(np.clip(u,0,1))
    E = a.add(v1)
    ec = E.sub(cvec)
    d = ec.magnitude()
    if (d - c.r < -1e-2):
        return False
    return True

def arclength_between_nodes(a: Vector, b:Vector, c:Circle):
    ## normalize vectors
    # anorm = a.normalize()
    # bnorm = b.normalize()
    # theta = anorm.angleBetweenVectors(bnorm)
    theta = a.angleBetweenVectors_direction_signed(b)
  
    return (abs(c.r *theta),theta)

def arclength_of_circle(a: Circle):
    return 2.0*round(math.pi,7)*a.r

def point_Circle_tangents(a: Vector, b:Circle):
    bv = Vector(b.ctr.x, b.ctr.y)
    # abv = bv.sub(a)
    # abvmag = abv.magnitude()
    # theta = math.asin(b.r/abvmag)
    # tmag = math.sqrt(abvmag*abvmag -b.r*b.r)
    # abvn = abv.normalize()
    # tr1 = abvn.rotate(theta)
    # t1 = tr1.mult(tmag)
    # tr2 = abvn.rotate(-theta)
    # t2 = tr2.mult(tmag)
    #t1.add(a),t2.add(a)
    bav = a.sub(bv)
    abvmag = bav.magnitude()
    theta = math.acos(b.r/abvmag)
    bavn = bav.normalize()
    tr1 = bavn.rotate(theta)
    tr2 = bavn.rotate(-theta)
    t1 = tr1.mult(b.r)
    t2 = tr2.mult(b.r)
    return [t1.add(bv),t2.add(bv)]

def circle_in_circle(a: Circle, b: Circle):
    ax = a.ctr.x
    ay = a.ctr.y
    bx = b.ctr.x
    by = b.ctr.y
    ab = Vector(ax,ay).sub(Vector(bx,by))
    d = ab.magnitude()
    ar = a.r
    br = b.r
    r = ar
    R = br
    ind = 0
    if ar > br:
        R = ar
        r = br
        ind = 1
    if r + d < R:
        return [True,ind]
    return [False,ind]

def circle_to_circle_intersection(a: Circle, b: Circle):
    ## first test circle to circle intersection
    acv = Vector(a.ctr.x, a.ctr.y)
    ar = a.r
    bcv = Vector(b.ctr.x, b.ctr.y)
    br = b.r
    arbr = ar+br
    ar_br = ar-br
    acvbcv = acv.sub(bcv)
    d = acvbcv.magnitude()
    if d > arbr:
        return [False, [0,0],1]
    amag = (ar*ar - br*br + d*d)/(2*d)
    hmag = math.sqrt(ar*ar-amag*amag)
    p1p0 = bcv.sub(acv)
    p1p0n = p1p0.normalize()
    p1p0a = p1p0n.mult(amag)
    p2 = p1p0a.add(acv)
    p2p0 = p2.sub(acv)
    p2p1 = p2.sub(bcv)
    ##p1p0 = bcv.sub(acv)
    p0p1 = acv.sub(bcv)
    ## test arc of intersection for each circle.  
    ## arc can sweep 0 - 180 or 2pi - (shortest arc distance between intersection points)
    ## if direction of vectors p1 to p0 and p0 to p1 are similar to p1 to chord midpoint 
    ## and p0 to chord midpoint, then intersection arcs are less than 180 returns True 
    ## otherwise False per boolean idicating arc radian length 2pi - (shortest arc distance between intersection points).

    th1 = p2p0.direction()
    th2 = p2p1.direction()
    th3 = p0p1.direction()
    th4 = p1p0.direction()
    ermin, ermax = (-.01,.01)
    t1 = th1 + ermin <= th4 and th1 + ermax >= th4
    t2 = th2 + ermin <= th3 and th2 + ermax >= th3
    arc1 = True
    arc2 = True
    if not t1:
        arc1 = False
    if not t2:
        arc2 = False
    x3 = p2.x + hmag*(bcv.y - acv.y)/d
    y3 = p2.y - hmag*(bcv.x - acv.x)/d
    x4 = p2.x - hmag*(bcv.y - acv.y)/d
    y4 = p2.y + hmag*(bcv.x - acv.x)/d
    return [True,[Vector(x3,y3), Vector(x4,y4)],[arc1,arc2]]

def arc_line_of_sight(p1vc:Vector, p2vc:Vector, a:Circle, b: Circle):
    res = circle_to_circle_intersection(a,b)
    rresult = []
    if res[0]:
        ## check to see if node path intersection occurs
        th1 = p1vc.direction()
        th2 = p2vc.direction()
        # direction vectors on the circle for each node
        avec = Vector(a.ctr.x, a.ctr.y)
        
        dp1vc = p1vc.sub(avec)
        dp2vc = p2vc.sub(avec) 
        inode, inode2 = res[1]
        dinode = inode.sub(avec)
        dinode2 = inode2.sub(avec)
        ## the next is a boolean parammeter indicating arc segment is min angle dist (intersect pt1, intersect pt2), or
        ## max angle dist (intersect pt1, intersect pt2) eg. 2pi - angle difference betweeen vectors.
        arc1, arc2 = res[2]  ## boolean states whether arc segment is min or maximumm angle distance between point
        print('arc1'+str(arc1))
        a1 = abs(dp1vc.angleBetweenVectors(dinode))
        a1_sign = dp1vc.angleBetweenVectors_direction_signed(dinode)
        a2 = abs(dp1vc.angleBetweenVectors(dinode2))
        a3 = abs(dp2vc.angleBetweenVectors(dinode))
        a4 = abs(dp2vc.angleBetweenVectors(dinode2))
        iangle = abs(dinode.angleBetweenVectors(dinode2))
        pangle = abs(dp1vc.angleBetweenVectors(dp2vc))
        arcsegintersect = False
        nodepath = True ## min arc distance
        nodepath1 = True
        nodepath2 = True 
        if a1 >= iangle or a2 >= iangle:
            if not arc1:
                arcsegintersect = True
            
        elif a1 <= iangle and a2 <= iangle:
            if arc1:
                print('a1 '+ str(a1))
                print('a2 '+ str(a2))
                print('iangle '+str(iangle))
                arcsegintersect = True
            
        if a3 >= iangle or a4 >= iangle:
            if not arc1:
                arcsegintersect = True

        elif a3 <= iangle and a4 <= iangle:
            if arc1:
                print('a3 '+str(a3))
                print('a4 '+str(a4))
                print('iangle '+str(iangle))
                arcsegintersect = True
        t1= a1 <= pangle and a2 <= pangle
        t2= a3 <= pangle and a4 <= pangle
        pathsign = 1
        # if a1_sign < 0:
        #     pathsign = -1
        if t1 and t2:
            nodepath=False
            if a1_sign < 0:
                pathsign = 1
            else:
                pathsign = -1
        else:
            if a1_sign < 0:
                pathsign = 1
            else:
                pathsign = -1

        return {'circleintersect': True,'arcsegintersect':arcsegintersect, 'intersection':[inode,inode2], 'minarc':arc1,
                'nodepath':nodepath,'pathsign': pathsign}
    return {'circleintersect': False, 'lineofsight': True}        
        # th3 = inode.direction()
        # th4 = inode2.direction()
        # minth1 = min(th1, th2)
        # maxth1 = max(th1, th2)
        # minth2 = min(th3, th4)
        # maxth2 = max(th3, th4)
        # t1 = minth1 <= minth2 
        # t2 = maxth1 >= minth2  ## cclockwise intersection
        # t3 = minth1 <= maxth2
        # t4 = maxth1 >= maxth2  ## clockwise intersection
        # clockw = True
        # cclockw = True 
        # if t1 and t2:
        #     cclockw = False
        # if t3 and t4:
        #     clockw = False  
        # if not t1 and not t4:
        #     clockw = False
        #     cclockw = False
        # if not t1 and t4:
        #     clockw = False
        #     cclockw = False

def arc_line_of_sight_2(p1vc:Vector, p2vc:Vector, a:Circle, b: Circle):
    def convert_negative_radians(theta):
        if theta < 0:
            return 2*math.pi - theta
        return theta

    def min_max_theta_ordering(theta1,theta2):
        return (min([theta1,theta2]), max([theta1,theta2]))

    res = circle_to_circle_intersection(a,b)
    rresult = []
    if res[0]:
        ## check to see if node path intersection occurs

        # direction vectors on the circle for each node
        avec = Vector(a.ctr.x, a.ctr.y)
        
        dp1vc = p1vc.sub(avec)
        dp2vc = p2vc.sub(avec) 
        inode, inode2 = res[1]
        dinode = inode.sub(avec)
        dinode2 = inode2.sub(avec)
        ## the next is a boolean parammeter indicating arc segment is min angle dist (intersect pt1, intersect pt2), or
        ## max angle dist (intersect pt1, intersect pt2) eg. 2pi - angle difference betweeen vectors.
        arc1, arc2 = res[2]  ## boolean states whether arc segment is min or maximumm angle distance between point
        print('arc1'+str(arc1))

        ## compute atan2 direction of d1pvc, dp2pvc, dinode, dinode2.  Atan2 converts all angles relative positive x axis
        ## normalize vectors 
        dp1vcn = dp1vc.normalize()
        dp2vcn = dp2vc.normalize()
        dinoden = dinode.normalize()
        dinode2n = dinode2.normalize()
        dp1vcn_theta = dp1vcn.direction()
        dp2vcn_theta = dp2vcn.direction()
        dinoden_theta = dinoden.direction()
        dinode2n_theta = dinode2n.direction()
        dp1vcn_theta = convert_negative_radians(dp1vcn_theta)
        dp2vcn_theta = convert_negative_radians(dp2vcn_theta)
        dinoden_theta = convert_negative_radians(dinoden_theta)
        dinode2n_theta = convert_negative_radians(dinode2n_theta)
        dn1thmin, dn2thmax = min_max_theta_ordering(dinoden_theta,dinode2n_theta)
        dpthetamin, dpthetamax = min_max_theta_ordering(dp1vcn_theta,dp2vcn_theta)
        compare_g_l = False
        if dn2thmax-dn1thmin <= math.pi:
            if arc1:
                compare_g_l = True
        else:
            if not arc1:
                compare_g_l = True
        arcsegintersect = False
        if compare_g_l:
            if dpthetamin >= dn1thmin and dpthetamin <= dn2thmax:
                arcsegintersect = True
            if dpthetamax >= dn1thmin and dpthetamax <= dn2thmax:
                arcsegintersect = True
        else:
            if dpthetamin <= dn1thmin or dpthetamin >= dn2thmax:
                arcsegintersect = True
            if dpthetamax <= dn1thmin or dpthetamax >= dn2thmax:
                arcsegintersect = True
        dp_compare_g_l = False
        if dpthetamax-dpthetamin <= math.pi:
            dp_compare_g_l = True
        a1 = abs(dp1vc.angleBetweenVectors(dinode))
        a1_sign = dp1vc.angleBetweenVectors_direction_signed(dinode)
        a2 = abs(dp1vc.angleBetweenVectors(dinode2))
        a3 = abs(dp2vc.angleBetweenVectors(dinode))
        a4 = abs(dp2vc.angleBetweenVectors(dinode2))
        iangle = abs(dinode.angleBetweenVectors(dinode2))
        pangle = abs(dp1vc.angleBetweenVectors(dp2vc))
        arcsegintersect = False
        nodepath = True ## min arc distance
        nodepath1 = True
        nodepath2 = True 
        # if a1 >= iangle or a2 >= iangle:
        #     if not arc1:
        #         arcsegintersect = True
            
        # elif a1 <= iangle and a2 <= iangle:
        #     if arc1:
        #         print('a1 '+ str(a1))
        #         print('a2 '+ str(a2))
        #         print('iangle '+str(iangle))
        #         arcsegintersect = True
            
        # if a3 >= iangle or a4 >= iangle:
        #     if not arc1:
        #         arcsegintersect = True

        # elif a3 <= iangle and a4 <= iangle:
        #     if arc1:
        #         print('a3 '+str(a3))
        #         print('a4 '+str(a4))
        #         print('iangle '+str(iangle))
        #         arcsegintersect = True
        
        t1= a1 <= pangle and a2 <= pangle
        t2= a3 <= pangle and a4 <= pangle
        pathsign = 1
        if dp_compare_g_l:
            t1 = dinoden_theta >= dpthetamin and dinode2n_theta <= dpthetamax
            t2 = dinode2n_theta >= dpthetamin and dinode2n_theta <= dpthetamax
            if t1 and t2:
                nodepath = False
            if a1_sign < 0:
                pathsign = 1
            else:
                pathsign -1
            # else:
            #     if a1_sign < 0:
            #         pathsign = 1
            #     else:
            #         pathsign = -1 
        else:
            t1 = dinoden_theta <= dpthetamin or dinoden_theta >= dpthetamax
            t2 = dinode2n_theta <= dpthetamin or dinode2n_theta >= dpthetamax 
            if t1 and t2:
                nodepath = False
                # if a1_sign < 0:
                #     pathsign = 1
                # else:
                #     pathsign -1   
            if a1_sign < 0:
                pathsign = 1
            else:
                pathsign = -1                           
        # if a1_sign < 0:
        #     pathsign = -1
        # if t1 and t2:
        #     nodepath=False
        #     if a1_sign < 0:
        #         pathsign = 1
        #     else:
        #         pathsign = -1
        # else:
        #     if a1_sign < 0:
        #         pathsign = 1
        #     else:
        #         pathsign = -1

        return {'circleintersect': True,'arcsegintersect':arcsegintersect, 'intersection':[inode,inode2], 'minarc':arc1,
                'nodepath':nodepath,'pathsign': pathsign}
    return {'circleintersect': False, 'lineofsight': True}        
    
def line_of_sight_Tracking(p1vc: Vector, p2vc: Vector, current_tracking, results):
    ## this tracks the open and closed line of sight segments for hugging paths of circle nodes
    ## per neighboring circle to circle intersection
    openseg = current_tracking['open'] ## is 0,1,2.  2 designates min max paths hugging paths open.  1 inicates min path, 0 is max path
    inode, inode2 = results['intersection']
    if openseg == 2:
        
        closed_path = results['minarc']  ## encoded closed path.  True min path between ipts, False max path between ipts.
        open_path = results['nodepath']
        current_tracking['open'] = open_path
        current_tracking['pathsign'] = results['pathsign']
    else:
        open_path = results['nodepath']
        path_sign = results['pathsign']
        tpath_sign = current_tracking['pathsign']
        print('open_path '+ str(open_path))
        print('open seg' + str(openseg))
        print('path_sign '+ str(path_sign))
        print('tpath_sign' + str(tpath_sign))
        if openseg != open_path:
            return False
        # if path_sign != tpath_sign:
        #     return False
    return True

def checkArcLineofSight(p1vc:Vector,p2vc:Vector, ucircs, cid, c:Circle):
    current_tracking = {'open': 2}
    lineofsight = True
    minarcpath = True
    for cid2, circ2 in enumerate(ucircs):
        if cid == cid2:
            continue
        res = arc_line_of_sight_2(p1vc, p2vc, c, circ2)
        if res['circleintersect']:
            print('circle intersection!')
            if res['arcsegintersect']:
                v1,v2 =res['intersection']
                print('intersections:')
                v1.print_vec()
                v2.print_vec()
                return {'arclineofsight':False, 'minarcpath':res['nodepath']}  
            else:
                res2 = line_of_sight_Tracking(p1vc,p2vc,current_tracking,res)
                minarcpath = res['nodepath']
                if not res2:
                    print('aclineofsight:False')
                    return {'arclineofsight':False, 'minarcpath':res['nodepath']}
              
    return {'arclineofsight':True, 'minarcpath':minarcpath}  

a, b = Point(0, 1), Point(0, -1)
c = [Circle(Point(0,0), 0.8), Circle(Point(3.8,0), 3.2), Circle(Point(-3.5,0), 3), Circle(Point(-7,0), 1)]

# a, b = Point(-3, 1), Point(4.25, 0)
# c = [Circle(Point(0,0), 2.5), Circle(Point(1.5,2), 0.5), Circle(Point(3.5,1), 1), Circle(Point(3.5,-1.7), 1.2)]

# a, b = Point(-3.5,0.1), Point(3.5,0.0)
# r = 2.01
# c = [Circle(Point(0,0), 1), Circle(Point(r,0), 1), Circle(Point(r*0.5, r*math.sqrt(3)/2), 1), Circle(Point(-r*0.5, r*math.sqrt(3)/2), 1),
#         Circle(Point(-r, 0), 1), Circle(Point(r*0.5, -r*math.sqrt(3)/2), 1), Circle(Point(-r*0.5, -r*math.sqrt(3)/2), 1)]

## build circle exclusion list where circle is interior to circle
## using kdtrees for fast nearest neighbor search
## build key index of circles
circs = []
for cir in c:
    circs.append([cir.ctr.x, cir.ctr.y])

a1 = np.array(circs)
tree = KDTree(a1)
nearest_dist, nearest_ind = tree.query(a1, k=2)  # k=2 nearest neighbors where k1 = identity
print(a1)
print(nearest_dist[:, 1])    # drop id; assumes sorted -> see args!
nninds = nearest_ind[:, 1]     # drop id 
## list check nearest neighbors to check circle circle overlap 
dropIndicies = []
for idx, x in enumerate(nninds):
    res = circle_in_circle(c[idx],c[x])
    if res[0]:
        if res[1]:
            dropIndicies.append(x)
        else:
            dropIndicies.append(idx)
ucircs = []
for id, cir in enumerate(c):
    if not id in dropIndicies:
        ucircs.append(cir)
print(ucircs)
## compute graph of tangent nodes
graph ={}  ## keyed parent circle id node to neighbor circle node graph
graph2 = {}  ## key node_id pairs to circle and start and end objects for graph2
graph3 = {} ## is node position graph 
graph4 = {}  ## circle intra node graph (all nodes contained on the circle) for computing hugging graph.
## initialize graph
for id, cir in enumerate(ucircs):
    graph[id] = {'nodes': {}, 'circle':cir}
    graph4[id] = {'nodes':{}, 'circle':cir}
graph['start'] = {'nodes':{}, 'circle':0}
graph['end'] = {'nodes':{}, 'circle': 0}
edges = 0
node_id = 2
strt = 0
trgt = 1
for id, cir in enumerate(ucircs):
    for id2, cir2 in enumerate(ucircs):
        if id == id2:
            continue
        if id2 in graph[id]['nodes']:
            continue
        ##compute graph tangents
        C=0; F=0; D=0; E=0; internalBitang = True
        try:
            C,F,D,E = internal_bitangents(cir,graph[id2]['circle'])
        except Exception as e:
            print('no internal bitangents')
            print(e)
            internalBitang = False
        if internalBitang:
            print(C)
            print(F)
            cf = C.sub(F)
            distcf = round(cf.magnitude(),8)
            ## check line of sight
            sightline = True
            for id3, cir3 in enumerate(ucircs):
                if id3 == id or id3 ==id2:
                    continue
                resls = line_of_sight(C,F, cir3)
                if not resls:
                    print('hit')
                    sightline = False
                    break
            if sightline:
                graph[id]['nodes'][id2] = {'nodepairs': {str(node_id)+' '+str(node_id+1):{'positions': [C,F],'distance':distcf}}}
                graph[id2]['nodes'][id] = {'nodepairs': {str(node_id+1)+' '+str(node_id):{'positions': [F,C],'distance':distcf}}}
                graph2[(node_id,node_id+1)]={'parentids':[id, id2], 'distance':distcf}
                graph2[(node_id+1,node_id)]={'parentids':[id2, id], 'distance':distcf}
                graph3[str(node_id)] = {'position':C, 'parentid':id,'position':C}
                graph3[str(node_id+1)] = {'position':F, 'parentid': id2,'position':F} 
                graph4[id]['nodes'][str(node_id)]=C
                graph4[id2]['nodes'][str(node_id+1)]=F
                edges+=1 
                node_id+=2
            de = D.sub(E)
            distde = round(de.magnitude(),8)
            ## check line of sight
            sightline = True; initNode = True
            if id2 in graph[id]['nodes']:
                initNode = False
            for id3, cir3 in enumerate(ucircs):
                if id3 == id or id3 ==id2:
                    continue
                if not line_of_sight(D,E, cir3):
                    sightline = False
                    break
            if sightline:
                if initNode:
                    graph[id]['nodes'][id2] = {'nodepairs': {str(node_id)+' '+str(node_id+1): {'positions': [D,E],'distance':distde}}} 
                    graph[id2]['nodes'][id] = {'nodepairs': {str(node_id+1)+' '+str(node_id): {'positions': [E,D],'distance':distde}}}
                else:   
                    graph[id]['nodes'][id2]['nodepairs'][str(node_id)+' '+str(node_id+1)]= {'positions': [D,E],'distance':distde}
                    graph[id2]['nodes'][id]['nodepairs'][str(node_id+1)+' '+str(node_id)]= {'positions': [E,D],'distance':distde}
                graph2[(node_id,node_id+1)]={'parentids':[id, id2], 'distance':distde}
                graph2[(node_id+1,node_id)]={'parentids':[id2, id], 'distance':distde}
                graph3[str(node_id)] = {'position':D, 'parentid':id,'position':D}
                graph3[str(node_id+1)] = {'position':E, 'parentid':id2,'position':E}
                graph4[id]['nodes'][str(node_id)]=D
                graph4[id2]['nodes'][str(node_id+1)]=E
                edges+=1 
                node_id+=2
        try:
            cir2 = graph[id2]['circle']
            A = cir
            B = cir2
            swapAB = False 
            ## note A B circle pair has implicit A radius >= B radius for external bitangents
            ## this is important for direction vector from B to A in external bitangents computation.
            ## just have to remember to swap function return values after external_bitangents 
            ## computation.  Note this direction vector for theta rotation always points away 
            ## from A and towards B, and determines the theta rotation axis.
            if A.r < B.r:
                A = B
                B = cir
                swapAB = True
            C,F,D,E = external_bitangents(A,B)
            if swapAB:
                ##copyC = C.copy()
                copyF = F.copy()
                F = C.copy()
                C = copyF
                copyE = E.copy()
                E = D.copy()
                D = copyE
        except Exception as e:
            print('no external bitangents')
            print(e)
            continue
        initNode = True
        if id2 in graph[id]['nodes']:
            initNode = False
        cf = C.sub(F)
        distcf = round(cf.magnitude(),8)
        ## check line of sight
        sightline = True
        for id3, cir3 in enumerate(ucircs):
            if id3 == id or id3 ==id2:
                continue
            resls = line_of_sight(C,F, cir3)
            if not resls:
                 print('hit line of sight external bitangent')
                 print('id '+str(id))
                 print('id2 '+str(id2))
                 sightline = False
                 break
        if sightline:
            if initNode:
                graph[id]['nodes'][id2] = {'nodepairs': {str(node_id)+' '+str(node_id+1):{'positions': [C,F],'distance':distcf}}}
                graph[id2]['nodes'][id] = {'nodepairs': {str(node_id+1)+' '+str(node_id):{'positions': [F,C],'distance':distcf}}}
                
            else:
                graph[id]['nodes'][id2]['nodepairs'][str(node_id)+' '+str(node_id+1)] = {'positions': [C,F],'distance':distcf}
                graph[id2]['nodes'][id]['nodepairs'][str(node_id+1)+' '+str(node_id)]= {'positions': [F,C],'distance':distcf}
            graph2[(node_id,node_id+1)]={'parentids':[id, id2], 'distance':distcf}
            graph2[(node_id+1,node_id)]={'parentids':[id2, id], 'distance':distcf}
            graph3[str(node_id)] = {'position':C, 'parentid':id,'position':C}
            graph3[str(node_id+1)] = {'position':F, 'parentid':id2,'position':F}
            graph4[id]['nodes'][str(node_id)]=C
            graph4[id2]['nodes'][str(node_id+1)]=F
            edges+=1
            node_id+=2   
        de = D.sub(E)
        distde = round(de.magnitude(),8)
        ## check line of sight
        sightline = True
        for id3, cir3 in enumerate(ucircs):
            if id3 == id or id3 ==id2:
                continue
            if not line_of_sight(D,E, cir3):
                 sightline = False
                 break
        if sightline:
            initNode = True
            if id2 in graph[id]['nodes']:
                initNode = False
            if initNode:
                graph[id]['nodes'][id2]={'nodepairs':{str(node_id)+' '+str(node_id+1): {'positions': [D,E],'distance':distde}}}
                graph[id2]['nodes'][id]={'nodepairs':{str(node_id+1)+' '+str(node_id): {'positions': [E,D],'distance':distde}}}
            else:
                graph[id]['nodes'][id2]['nodepairs'][str(node_id)+' '+str(node_id+1)]= {'positions': [D,E],'distance':distde}
                graph[id2]['nodes'][id]['nodepairs'][str(node_id+1)+' '+str(node_id)]= {'positions': [E,D],'distance':distde}
            graph2[(node_id,node_id+1)]={'parentids':[id, id2], 'distance':distde}
            graph2[(node_id+1,node_id)]={'parentids':[id2, id], 'distance':distde}
            graph3[str(node_id)] = {'position':D, 'parentid':id,'position':D}
            graph3[str(node_id+1)] = {'position':E, 'parentid':id2,'position':E}
            graph4[id]['nodes'][str(node_id)]=D
            graph4[id2]['nodes'][str(node_id+1)]=E
            edges+=1
            node_id+=2     

#compute start end node point circle tangents
for id, cir in enumerate(ucircs):
    t1 = 0; t2= 0; pcirtangentfound = True
    try:
        t1, t2 = point_Circle_tangents(Vector(a.x,a.y),cir)
    except Exception as e:
        print('no point circle tangents')
        print(e)
        pcirtangentfound = False
    if pcirtangentfound:
        lineofsight = True
        for id2, cir2 in enumerate(ucircs):
            # if id == id2:
            #     continue
            if not line_of_sight(Vector(a.x, a.y), t1, cir2):
                lineofsight = False
                break
        if lineofsight:
      
            va = Vector(a.x,a.y)
            vat1 = va.sub(t1)
            vat1mag = round(vat1.magnitude(),8)
            graph[id]['nodes']['start'] = {'nodepairs': {str(node_id)+' start':{'positions': [t1,va],'distance':vat1mag}}}
            graph['start']['nodes'][id] = {'nodepairs': {'start '+str(node_id):{'positions': [va,t1],'distance':vat1mag}}} 
            graph2[(node_id,strt)]={'parentids':[id, 'start'], 'distance':vat1mag}
            graph2[(strt,node_id)]={'parentids':['start', id], 'distance':vat1mag}
            graph3[str(node_id)]={'position':D, 'parentid':id,'position':t1}
            graph4[id]['nodes'][str(node_id)]=t1
            edges+=1
            node_id+=1
        lineofsight = True
        for id2, cir2 in enumerate(ucircs):
            # if id == id2:
            #     continue
            if not line_of_sight(Vector(a.x, a.y), t2, cir2):
                lineofsight = False
                break
        if lineofsight:
            va = Vector(a.x,a.y)
            vat2 = va.sub(t2)
            vat2mag = vat2.magnitude()
            if 'start' in graph[id]['nodes']:
                graph[id]['nodes']['start']['nodepairs'][str(node_id)+' start']={'positions': [t2,va],'distance':vat2mag}
                graph['start']['nodes'][id]['nodepairs']['start ' + str(node_id)]={'positions': [va,t2],'distance':vat2mag}
            else:    
                graph[id]['nodes']['start'] = {'nodepairs': {str(node_id)+' start':{'positions': [t2,va],'distance':vat2mag}}}
                graph['start']['nodes'][id] = {'nodepairs': {'start '+str(node_id):{'positions': [va,t2],'distance':vat2mag}}}
            graph2[(node_id,strt)]={'parentids':[id, 'start'], 'distance':vat2mag}
            graph3[str(node_id)]={'position':D, 'parentid':id,'position':t2}
            graph2[(strt,node_id)]={'parentids':['start', id], 'distance':vat2mag}
            graph4[id]['nodes'][str(node_id)]=t2
            edges+=1
            node_id+=1
## check end node for circle tangents
    t1 = 0; t2= 0; pcirtangentfound = True
    try:
        t1, t2 = point_Circle_tangents(Vector(b.x,b.y),cir)
    except Exception as e:
        print('no point circle tangents')
        print(e)
        pcirtangentfound = False
    if id == 1:
        print ('1 pcirtangentfound: '+ str(pcirtangentfound))
    if pcirtangentfound:
        lineofsight = True
        for id2, cir2 in enumerate(ucircs):
            # if id == id2:
            #     continue
            if not line_of_sight(Vector(b.x, b.y), t1, cir2):
                lineofsight = False
                break
        if id == 1:
            print('id 1 line of sight: '+str(lineofsight))
        if lineofsight:
            vb = Vector(b.x,b.y)
            vbt1 = vb.sub(t1)
            vbt1mag = round(vbt1.magnitude(),8)
            graph[id]['nodes']['end'] = {'nodepairs': {str(node_id)+' end':{'positions': [t1,vb],'distance':vbt1mag}}}
            graph['end']['nodes'][id] = {'nodepairs': {'end '+str(node_id):{'positions': [vb,t1],'distance':vbt1mag}}}
            graph2[(node_id,trgt)]={'parentids':[id, 'end'], 'distance':vbt1mag}
            graph2[(trgt,node_id)]={'parentids':['end', id], 'distance':vbt1mag}
            graph3[str(node_id)]={'position':D, 'parentid':id,'position':t1}
            graph4[id]['nodes'][str(node_id)]=t1
            edges+=1 
            node_id+=1
        lineofsight = True
        for id2, cir2 in enumerate(ucircs):
            # if id == id2:
            #     continue
            if not line_of_sight(Vector(b.x, b.y), t2, cir2):
                lineofsight = False
                break
        if lineofsight:
            vb = Vector(b.x,b.y)
            vbt2 = vb.sub(t2)
            vbt2mag = round(vbt2.magnitude(),8)
            initNode = True
            if 'end' in graph[id]['nodes']:
                initNode = False
            if initNode:
                graph[id]['nodes']['end'] = {'nodepairs': {str(node_id)+' end':{'positions': [t2,vb],'distance':vbt2mag}}}
                graph['end']['nodes'][id] = {'nodepairs': {'end '+str(node_id):{'positions': [vb,t2],'distance':vbt2mag}}}
            else:
                graph[id]['nodes']['end']['nodepairs'][str(node_id)+' end']= {'positions': [t2,vb],'distance':vbt2mag}
                graph['end']['nodes'][id]['nodepairs']['end '+str(node_id)]={'positions': [vb,t2],'distance':vbt2mag}
            graph2[(node_id,trgt)]={'parentids':[id, 'end'], 'distance':vbt2mag}
            graph2[(trgt,node_id)]={'parentids':['end',id], 'distance':vbt2mag}
            graph3[str(node_id)]={'position':D, 'parentid':id,'position':t2}
            graph4[id]['nodes'][str(node_id)]=t2
            edges+=1
            node_id+=1
## check line of sight between 'start' and 'end' nodes 
lineofsight = True
va = Vector(a.x, a.y)
vb = Vector(b.x, b.y)
for id2, cir2 in enumerate(ucircs):
    if not line_of_sight(va, vb, cir2):
        lineofsight = False
        break
if lineofsight:
    
    vavb = va.sub(vb)
    vavbmag = round(vavb.magnitude(),8)
    graph['end']['nodes']['start'] = {'nodepairs': {'end'+' start':{'positions': [vb,va],'distance':vavbmag}}}
    graph['start']['nodes']['end'] = {'nodepairs': {'start '+'end':{'positions': [va,vb],'distance':vavbmag}}}
    graph2[(strt,trgt)] = {'parentids':['start', 'end'], 'distance':vavbmag}
    graph2[(trgt,strt)] = {'parentids':['end', 'start'], 'distance':vavbmag}
    edges+=1       

## check all nodes for start and end line of sight add to node pairs and compute distance
for key in graph3:
    vpos = graph3[key]['position']
    vparent = graph3[key]['parentid']
    lineofsight = True
    for id2, cir2 in enumerate(ucircs):
      
        if not line_of_sight(va, vpos, cir2):
            lineofsight = False
            break
    if key == str(16):
        print('line of sight node 16 '+str(lineofsight))
    if lineofsight:
        vavpos = va.sub(vpos)
        vavposmag = round(vavpos.magnitude(),8)
        initNode = True
        if 'start' in graph[vparent]['nodes']:
            initNode = False
        if initNode:
            graph[vparent]['nodes']['start'] = {'nodepairs':{key+' start':{'positions': [vpos, va],'distance':vavposmag}}}
        else:
            graph[vparent]['nodes']['start']['nodepairs'][key+' start'] = {'positions': [vpos,va], 'distance': vavposmag}
        if vparent in graph['start']['nodes']:
            graph['start']['nodes'][vparent]['nodepairs']['start '+key] = {'positions': [va,vpos], 'distance': vavposmag}
        else:
            graph['start']['nodes'][vparent] = {'nodepairs':{'start '+key:{'positions': [va, vpos],'distance':vavposmag}}}
        graph2[(strt,int(key))]={'parentids':[vparent, 'start'], 'distance':vavposmag}
        edges+=1
    ## check end node
    lineofsight = True
    for id2, cir2 in enumerate(ucircs):
        if not line_of_sight(vb, vpos, cir2):
            lineofsight = False
            break
    if key == str(16):
        print('line of sight node 16 '+str(lineofsight))
    if lineofsight:
        vbvpos = vb.sub(vpos)
        vbvposmag = round(vbvpos.magnitude(),8)
        initNode = True
        if 'end' in graph[vparent]['nodes']:
            initNode = False
        if initNode:
            graph[vparent]['nodes']['end'] = {'nodepairs':{key+' end':{'positions': [vpos, vb],'distance':vbvposmag}}}
        else:
            graph[vparent]['nodes']['end']['nodepairs'][key+' end'] = {'positions': [vpos,vb], 'distance': vbvposmag}
        if vparent in graph['end']['nodes']:
            graph['end']['nodes'][vparent]['nodepairs']['end '+key] = {'positions': [vb,vpos], 'distance': vbvposmag}
        else:
            graph['end']['nodes'][vparent] = {'nodepairs':{'end '+key:{'positions': [vb, vpos],'distance':vbvposmag}}}
        graph2[(trgt,int(key))] = {'parentids':[vparent, 'end'], 'distance':vbvposmag}
        edges+=1
## compute arc length on nodes on circle, build hugging path graphs
for id in graph4:
    cir = graph4[id]['circle']
    cirp = Vector(cir.ctr.x, cir.ctr.y)
    for nid1 in graph4[id]['nodes']:
        for nid2 in graph4[id]['nodes']:
            if nid1 == nid2:
                continue
            t1 = nid1+' '+nid2 in graph2
            t2 = nid2+' '+nid1 in graph2
            if t1 or t2:
                continue
            p1v = graph4[id]['nodes'][nid1]
            p2v = graph4[id]['nodes'][nid2]
            print('arcnode id1: '+nid1)
            print('arcnode id2: '+nid2)
            p1vc = p1v.sub(cirp)
            p2vc = p2v.sub(cirp)
            res = checkArcLineofSight(p1vc,p2vc,ucircs, id, cir)
            if res['arclineofsight']:
                p1vp2vdist,theta = arclength_between_nodes(p1vc,p2vc,cir)
                arcdist = p1vp2vdist
                # if int(nid1) ==  10 and int(nid2) == 26:
                #     print('minarcpath ' + str(res['minarcpath']))
                if not res['minarcpath']:
                    arcdist = arclength_of_circle(cir)-arcdist
                graph2[(int(nid1),int(nid2))] = {'parentids': [id,id], 'distance': round(arcdist,8), 'minarcpath':res['minarcpath'],'theta':theta}
                edges+=1
#print(graph)
print(graph2)
print(graph3)
print(graph4)
print(edges)
print(len(graph2))
edgs = list(graph2.keys())
print(edgs)
print(node_id)
g2 = Graph2(edgs,node_id)
res = hasConnectedGraph(g2,node_id,0,1)
## build start end connected set of graph nodes
print(res)
if res[0]:
    nds = []
    for index, nd in enumerate(res[1]):
        if nd:
            nds.append(index)
    init_graph = {}
    for nd in nds:
        init_graph[nd] = {}
    
    for npair in graph2:
        p1,p2 = npair
        t1 = p1 in nds
        t2 = p2 in nds
        if t1 and t2:
            init_graph[p1][p2] = graph2[npair]['distance']
        
    print(init_graph)
    grph = Graph(nds,init_graph)
    previous_nodes, shortest_path = dijkstra_algorithm(graph=grph, start_node=0)
    print_result(previous_nodes, shortest_path, start_node=0, target_node=1)

# nodekeys = [0,26,2,3,16,17,27,1]
# nodekeys2 = [0,26,2,3,18,19,28,1]
# nodekeys3 = [0,64,45,44,13,12,6,7,29,28,30,1]
nodekeys = [0,5,3,1]
def cdists(nodekeys):
    tdist = 0
    dists = []
    for i,nkey in enumerate(nodekeys):
        if i == len(nodekeys)-1:
            break
        keyval = (nkey, nodekeys[i+1])
        if not keyval in graph2:
            keyval = (nodekeys[i+1],nkey)
        dists.append(graph2[keyval]['distance'])
        tdist += graph2[keyval]['distance']
    print('total distance: '+ str(tdist))
    print('distances: '+ str(dists))
# cdists(nodekeys)
# cdists(nodekeys2)
cdists(nodekeys)
pathstring = 'C:\\Users\\chris\\Documents\\'
file = open(pathstring+'read.txt', 'w')
file.write(str(graph2))
file.write(str(graph4))
file.close()

import matplotlib.pyplot as plt
 
figure, axes = plt.subplots()
for id in graph4: 
   ncirc = graph4[id]['circle']
   Drawing_uncolored_circle = plt.Circle( (ncirc.ctr.x, ncirc.ctr.y ),
                                      ncirc.r ,
                                      fill = False )
   axes.add_artist( Drawing_uncolored_circle )
for id in graph3:
    npt = graph3[id]['position']
    plt.plot(npt.x,npt.y,marker="o", markersize=3, markeredgecolor="red", markerfacecolor="green")
    plt.annotate(id,(npt.x,npt.y))
 
plt.axis([-20, 20, -20, 20])
##axes.add_artist( Drawing_uncolored_circle )
plt.title( 'Circle' )
plt.show()

