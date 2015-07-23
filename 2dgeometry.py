
from math import sqrt, cos, acos, pi, sin as sen # Why sen instead of sin?? Because i'm spanish and I prefer to call it sen

def to_rad(angle):
    '''
     180  (grad) -> pi (rad)
    angle (grad) -> x (rad)
    '''
    return (angle*pi)/180

def to_grad(angle):
    '''
      pi    (rad) -> 180 (grad)
     angle  (rad) ->  x  (grad)
    '''
    return (angle*180)/pi

class Poligon:
    '''
    Abstract class to defined posibles sides of a Poligon
    '''
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
    '''
    2D or 3D vectos geometry
    '''

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
        elif components != None and len(components) != len(self.base):
            print 'Bad initialization:\n\tComponent dimension not the same as vector dimension'

    def __str__(self):
        if len(self.base) == 2:
            return '({},{})'.format(self.direction[Vector.i],self.direction[Vector.j])
        elif len(self.base) == 3:
            return '({},{},{})'.format(self.direction[Vector.i],self.direction[Vector.j],self.direction[Vector.k])

    def __len__(self):
        return len(self.base)

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

    def __neg__(self):
        new_vector = []
        for component in Vector.bases_keys[len(self.base)-2]:
            new_vector.append( -self.direction[component] )
        return Vector(len(self.base),new_vector)

    def __mul__(self,other):

        if isinstance(other,int) or isinstance(other,float):
            for component in self.direction:
                direction[component] *= other

        elif isinstance(other,Vector) and len(other) == len(self):

            result = []
            for component in self.direction:
                result.append(self.direction[component] * other.direction[component])

            return sum(result)

        elif not (isinstance(other,int) or isinstance(other,float) or isinstance(other,Vector)):
            print 'Type error on Vector:\n\tMust use type float, int or Vector on:\n\tMultiplicate vectors.'

        elif len(other) == len(self):
            print 'Vectors bad dimension:\n\tVectors scalar product must be same dimension'

    def __rmul__(self,other):
        if isinstance(other,int) or isinstance(other,float):
            return self.__mul__(other)

    def __div__(self,other):
        instance = isinstance(other,int) or isinstance(other,float)
        if not instance:
            print 'Error type:\n\tType on division must be an escalar.\n int or float type ??'
        else:
            result = []
            for component in Vector.bases_keys[len(self.base)-2]:
                result.append( float(self.direction[component]) / float(other))
            return Vector(len(self),result)

    def __rdiv__(self,other):
        return self.__div__(other)

    def __getitem__(self,key):
        count = 0
        if key < len(self):
            for component in Vector.bases_keys[len(self.base)-2]:
                if count == key:
                    return self.direction[component]
                count += 1
        else:
            print '***Out of range!!:\n\tVector have %d dimension\n\tYou\'re trying to acces on %dth component' % (len(self),key+1)
            return None
        return None

    def __setitem__(self,key,value):
        count = 0
        if key < len(self):
            for component in Vector.bases_keys[len(self.base)-2]:
                if count == key:
                    self.direction[component] = value
                count += 1
        else:
            print '***Out of range!!:\n\tVector have %d dimension\n\tYou\'re trying to acces on %dth component' % (len(self),key+1)

    def __xor__(self,other):
        'Calculate the vectorial product (v1^v2) of the vector'
        if len(self) == len(other) and isinstance(other,Vector):
            if len(self) == 3:
                # This could export to ndimension vector
                new_vector = Vector('base 3')
                new_vector[0] = (self[1] * other[2]) - (self[2] * other[1])
                print new_vector[0]
                new_vector[1] = - ( (self[0] * other[2]) - (self[2] * other[0]) )
                print new_vector[1]
                new_vector[2] = (self[0] * other[1]) - (self[1] * other[0])
                print new_vector[2]
                return new_vector
            else:
                print 'Dimension error:\n\tFor calculate vectorial product must be 3 dimension vector.'

        elif not isinstance(other,Vector):
            print 'Fail in vectorial calculate:\n\tBoth element must be Vector type.'

        else:
            print 'Dimenstion error:\n\tVectors must have same dimension'

    def __rxor__(self,other):
        'Calculate the vectorial product (v1^v2) of the vector'
        return self.__xor__(other)

    def getBase(self,base):
        if str(base) in Vector.base_names:
            for name in Vector.base_names:
                if str(base) in name:
                    return Vector.base_names[name]

    def calc_module(self):
        'Calculate the module of the vector'
        components = []
        for direction in self.direction:
            if self.direction[direction] == None:
                print 'Fail using calc_module() method:\n\tNot component in vector\nDid you succsesfully initialize them?'
                return None
            else:
                components.append(self.direction[direction] ** 2)
        return float(sqrt(sum(components)))

    def components(self,components):
        'Components of the vector a i + b j + c k'
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

    def _get_angle(self,other):
        return ( (self * other)/(abs(self)*abs(other)) )

def dot(v1,v2):
    cos_alpha = (v1*v2)/(abs(v1)*abs(v2))
    return abs(v1)*abs(v2)*cos_alpha

def normalize(v):
    new_vector = []
    for i in xrange(len(v)):
        new_vector.append( float(v[i]) / float(abs(v)))
    return Vector(len(v),new_vector)
