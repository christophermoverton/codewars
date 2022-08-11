import math
from typing import NamedTuple
class Point(NamedTuple):
    x: float
    y: float

class Vector:
    def dot(self, a):
        return self.x*a.x + self.y*a.y
    def magnitude(self):
        return math.sqrt(self.x*self.x+self.y*self.y)
    def normalize(self):
        d = self.magnitude()
        xp = self.x/d  
        if abs(xp) < 1e-4:
            xp = math.modf(xp)[1]
        return Vector(xp, self.y/d)
    def angleBetweenVectors(self, b):
        dotab = self.dot(b)
        maga = self.magnitude()
        magb = b.magnitude()
        cos_theta = dotab/(maga*magb)
        abs_cos_theta = math.fabs(cos_theta)
        if abs_cos_theta > 1.0:
            if abs_cos_theta - 1.0 < 1e-5:
                cos_theta = math.modf(cos_theta)[1]
            else:
                raise ValueError('Invalid arguments (vectors not normalized?)')
        return math.acos(cos_theta)
    def angleBetweenVectors_direction_signed(self, b):
        ## east counter clockwise signed
        return math.atan2(self.x*b.y - self.y*b.x, self.x*b.x+self.y*b.y)
    def rotate(self, theta):
        xp = self.x*math.cos(theta)- self.y*math.sin(theta)
        yp = self.x*math.sin(theta)+ self.y*math.cos(theta)
        return Vector(xp,yp)
    def add(self, b):
        return Vector(self.x+b.x, self.y+b.y)
    def sub(self, b):
        return Vector(self.x-b.x, self.y-b.y)
    def mult(self, c):
        ##scalar mult
        return Vector(self.x*c, self.y*c)
    def direction(self):
        ## returns angle in radians
        xp = self.x 
        yp = self.y 
        
        theta = 0
        if xp > 0 and yp >= 0:
            theta = abs(math.atan(yp/xp))
        if xp == 0:
            if yp > 0:
                return math.pi/2
            else:
                return math.pi+math.pi/2
        if xp < 0 and yp >= 0:
            theta = math.pi - abs(math.atan(yp/xp))
        if xp < 0 and yp <= 0:
            theta = math.pi + abs(math.atan(yp/xp))
        if xp > 0 and yp <= 0:
            theta = 2*math.pi - abs(math.atan(yp/xp))
        return theta
        
    def direction_atan2(self):
        cos_theta = self.y/self.x
        abs_cos_theta = math.fabs(cos_theta)
        if abs_cos_theta > 1.0:
            if abs_cos_theta - 1.0 < 1e-5:
                cos_theta = math.modf(cos_theta)[1]
            else:
                raise ValueError('Invalid arguments (vectors not normalized?)')
        return math.acos(cos_theta)        
            

    def projection_onto_self(self, u):
        ## self is v
        v = self.normalize()
        udotv = self.dot(v)
        return v.mult(udotv)

    def copy(self):
        return Vector(self.x, self.y)

    def print_vec(self):
        print(str(self.x)+','+str(self.y))
    def __init__(self, x,y):
        self.x = x
        self.y = y
    
AB = 1
BC = 100

AC = math.sqrt(AB**2+BC**2)
M = AC/2## mag length
## vector to M
A = (0,AB)
A = Point(0,AB)
C = Point(BC,0)
A = Vector(A.x,A.y)
C = Vector(C.x,C.y)
CA = A.sub(C)
CAn = CA.normalize()
CAnM = CAn.mult(M)
M = CAnM.add(C)
MBC=round((180/math.pi)*math.atan(M.y/M.x))
#BCM = (180/math.pi)*math.acos(M/BC) ## radians 
#MBC = round(180-(90+BCM))
print(str(int(MBC))+'\u00B0')