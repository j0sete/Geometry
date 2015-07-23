from math import sqrt

class Poligon:
    side = {
        'three' : 3, '3' : 3, 'three sides' : 3, 'three side' : 3, 'threesides' : 3, 'threeside' : 3,
        'four'  : 4, '4' : 4, 'four sides'  : 4, 'four side'  : 4, 'foursides'  : 4, 'fourside'  : 4
    }

class Triangle(Poligon):

    sides = Poligon.side['three']

    def __init__(self,sticks=None,stick1=None,stick2=None,stick3=None):

        if sticks != None and len(sticks) == 3 and ( isinstance(sticks,tuple) or isinstance(sticks,list) ):
            self.sticks = []
            for stick in sticks:
                self.sticks.append(stick)

        elif not (isinstance(sticks,tuple) or isinstance(sticks,list)) or len(sticks) != 3:
            print 'Type error on Triangle at initialization:\n\tYou must use \'tuple\' type\n\tor \'list\' type with length 3.\n'

        elif stick1 != None and stick2 != None and stick3 != None and ( isinstance(stick1,float) or isinstance(stick2,float) or isinstance(stick3,float) or isinstance(stick1,int) or isinstance(stick2,int) or isinstance(stick3,int)):
            self.sticks = [stick1,stick2,stick3]

        elif not (isinstance(stick1,float) or isinstance(stick2,float) or isinstance(stick3,float) or isinstance(stick1,int) or isinstance(stick2,int) or isinstance(stick3,int)):
            print 'Type error on Triangle at initialization:\n\tYou must use \'int\' type or \'float\' type\n\tat stickX initialization.'

    def is_triangle(self):
        if sticks != None:
            pass
        elif sticks != None and not isinstance(sticks,list):
            print 'Pon una lista compae'
        elif sticks == None:
            print 'Initialize sticks'


class Pitagoras:
    def __init__(self,cat1=None,cat2=None):
        self.cat1 = cat1
        self.cat2 = cat2

    def get_hipotenusa(self,cat1=None,cat2=None):
        if self.cat1 != None and self.cat2 != None:
            return sqrt(self.cat1*self.cat1 + self.cat2*self.cat2)
        elif ( cat1 != None and cat != None ) and ( isinstance(cat1,int) or isinstance(cat1,float) ):
            return sqrt(cat1*cat1 + cat2*cat2)
        else:
            print 'Pitagoras method bad use:\n\tType must be \'int\' or \'float\' \n\tor initialize the class pit = Pitagoras(cat1,cat2).\n'

class Point(object):
    '''
    Represent a 2D values

    Atributes: x and y coordinates
    '''

    zero = (0,0)

    def __init__(self,x=None,y=None):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%.2f, %.2f)' % (self.x, self.y)

    def __add__(self,point2):
        if isinstance(point2,tuple) and len(point2) == 2:
            self.x += point2[0]
            self.y += point2[1]
            return Point(self.x,self.y)
        elif isinstance(point2,Point):
            self.x += point2.x
            self.y += point2.y
            return Point(self.x,self.y)
        else:
            print 'Invalid argument to add for a point\n\tTry with Point() + (x,y) or Point() + Point()'
            print 'Method error: Not good use'

    def __radd__(self,other):
        return self.__add__(other)

    def __dict__(self):
        return {'x' : self.x, 'y' : self.y}

    def __cmp__(self,other):

        if self.distance_to(Point.zero) > other.distance_to(Point.zero):
            return 1
        elif self.distance_to(Point.zero) < other.distance_to(Point.zero):
            return -1
        else:
            return 0

    def print_point(self):
        print '(%d, %d)' % (self.x, self.y)

    def distance_to(self,point2):
        if isinstance(point2,Point):
            dx = abs(point2.x - self.x)
            dy = abs(point2.y - self.y)
            result = dx + dy
            return sqrt(result)
        elif isinstance(point2,tuple) and len(point2) == 2:
            dx = abs(point2[0] - self.x)
            dy = abs(point2[1] - self.y)
            result = dx + dy
            return sqrt(result)
        else:
            print 'Invalid argument to calculate distance between points\n\tTry with a Point() or tuple of 2'

    def move_to(self,x,y):
        self.x = x
        self.y = y

    def abs(self,num):
        if num >= 0:
            return num
        else:
            return (-1 * num)

class Vector:

    i = 'i'
    j = 'j'
    k = 'k'

    base2_keys = (i,j)
    base2 = {
        i : [1,0],
        j : [0,1]
    }

    base3_keys = (i,j,k)
    base3 = {
        i : [1,0,0],
        j : [0,1,0],
        k : [0,0,1]
    }

    bases = [base2,base3]
    bases_keys = [base2_keys,base3_keys]

    base_names = {
        'base2' : 2, 'base 2' : 2, '2' : 2,
        'base3' : 3, 'base 3' : 3, '3' : 3
    }

    def __init__(self,base=2,components=None):

        self.base = Vector.bases[self.getBase(base)-2]

        self.direction = {}
        for component in Vector.bases_keys[len(self.base)-2]:
            self.direction[component] = None

        if components != None and len(components) == len(self.base):
            self.components(components)
        elif len(components) != len(self.base):
            print 'Bad initialization:\n\tComponent dimension not the same as vector dimension'

    def __str__(self):
        if len(self.base) == 2:
            return '({},{})'.format(self.direction[Vector.i],self.direction[Vector.j])
        elif len(self.base) == 3:
            return '({},{},{})'.format(self.direction[Vector.i],self.direction[Vector.j],self.direction[Vector.k])

    def __add__(self,other):

        instance = isinstance(other,Vector) or isinstance(other,list) or isinstance(other,tuple)

        if instance and len(other.base) == len(self.base):
            new_vector = []
            for component in Vector.bases_keys[len(self.base)-2]:
                new_vector.append(self.direction[component] + other.direction[component])

            return Vector(len(self.base),new_vector)

        elif not instance:
            print 'Bad vector aditive use:\n\tMust be a Vector, list or tuple type.'
            return None

        elif len(other.base) != len(self.base):
            print 'Bad dimension of vectors:\n\tVectors must be same dimension.'
            return None

    def __radd__(self,other):
        return self.__add__(other)

    def __abs__(self):
        return self.calc_module()

    def getBase(self,base):
        if str(base) in Vector.base_names:
            for name in Vector.base_names:
                if str(base) in name:
                    return Vector.base_names[name]

    def calc_module(self):
        components = []
        for direction in self.direction:
            if self.direction[direction] == None:
                print 'Fail using calc_module() method:\n\tNot component in vector\nDid you succsesfully initialize them?'
                return None
            else:
                components.append(self.direction[direction] ** 2)
        return sqrt(sum(components))

    def components(self,components):

        if isinstance(components,dict) and len(components) == len(base):
            for component in components:
                self.direction[component] = components[component]

        elif isinstance(components,list):
            i = 0
            for component in Vector.bases_keys[len(self.base)-2]:
                self.direction[component] = components[i]
                i += 1
        else:
            print 'Bad use of method components\n\tWe accept list or dict types'


v = Vector(2,[1,1])
w = Vector(2,[3,4])
print (v+w)
print abs(w)
