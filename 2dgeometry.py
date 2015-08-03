
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

class Point:
    '''
    Represent a 2D or 3D values
    '''

    zero = (0,0,0)

    def __init__(self,point=None,x=None,y=None,z=None):
        if not point:
            if x and y and z:
                self.coor = (x,y,z)
            elif x and y and not z:
                self.coor = (x,y)
            else:
                self.coor = None
        elif point and isinstance(point,tuple):
            self.coor = point
        else:
            self.coor = None

    def _isInitialize(self):
        return self.coor

    def __len__(self):
        return len(self.coor)

    def __str__(self):
        if len(self) == 2:
            return '(%.2f, %.2f)' % (self.coor[0], self.coor[1])
        elif len(self) == 3:
            return '(%.2f, %.2f, %.2f)' % (self.coor[0], self.coor[1], self.coor[2])
        else:
            print 'Method __str__ fail in Point():\n\tDo you initialize the point??'

    def setCoordinates(self,x=None,y=None,z=None):
        instance   = ( isinstance(x,int) or isinstance(x,float) ) and ( isinstance(y,int) or isinstance(y,float) )
        instance_z = instance and ( isinstance(z,int) or isinstance(z,float) )

        if x and y and z and instance_z:
            self.coor = (x,y,z)
        elif x and y and not z and instance:
            self.coor = (x,y)
        elif not instance or not instance_z:
            print 'Method setCoordinates fail:\n\tBad type arguments, x,y,z must be integer or float type'
        else:
            print 'Method setCoordinates fail:\n\tMiss to put some argument??'

    def __cmp__(self,other):

        if self.distance_to(Point.zero) > other.distance_to(Point.zero):
            return 1
        elif self.distance_to(Point.zero) < other.distance_to(Point.zero):
            return -1
        else:
            return 0

    def __getitem__(self,item):
        if isinstance(item,int) or isinstance(item,float):
            if item == 0:
                return self.x
            elif item == 1 or item == -1:
                return self.y
            else:
                print 'Exceed index:\n\t2 dimensions only'
                return None

        elif isinstance(item,str):
            if item == 'x':
                return self.x
            elif item == 'y':
                return self.y
            else:
                print 'Index Error:\n\tNot valid index'
                return None
        else:
            print 'Type Error:\n\tNot valid type, use int, float or \'x\' and \'y\' strs.'

    def __setitem__(self,index,value):
        if item == 0:
            self.x = value
        elif item == 1 or item == -1:
            self.y = value
        else:
            print 'Exceed index:\n\t2 dimensions only'

    def print_point(self):
        print '(%d, %d)' % (self.x, self.y)

    def distance_to(self,other):
        if self._isInitialize():
            if isinstance(other,Point) and len(other) == len(self):

        else:
            print 'Error on class Point\n\tDid you initialize the class???'
        '''
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
        '''

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

    # Cartesian directors
    i = 'i'
    j = 'j'
    k = 'k'

    # Base 2 directors
    base2_keys = (i,j)
    base2 = {
        i : [1,0],
        j : [0,1]
    }

    # Base 3 directors
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
        'Initialize the Vector with some components or/and a base'

        self.base = Vector.bases[self.getBase(base)-2]

        self.direction = {}
        for component in Vector.bases_keys[len(self.base)-2]:
            self.direction[component] = None

        if components != None and len(components) == len(self.base):
            self.components(components)
        elif components != None and len(components) != len(self.base):
            print 'Bad initialization:\n\tComponent dimension not the same as vector dimension'

    def __str__(self):
        'Show this vector'
        if len(self.base) == 2:
            return '({},{})'.format(self.direction[Vector.i],self.direction[Vector.j])
        elif len(self.base) == 3:
            return '({},{},{})'.format(self.direction[Vector.i],self.direction[Vector.j],self.direction[Vector.k])

    def __len__(self):
        'Return base of vector'
        return len(self.base)

    def __add__(self,other):
        'Sum two vectors'

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
        'Sum two vectors'
        return self.__add__(other)

    def __abs__(self):
        'Return the module of the vector'
        return self.calc_module()

    def __neg__(self):
        new_vector = []
        for component in Vector.bases_keys[len(self.base)-2]:
            new_vector.append( -self.direction[component] )
        return Vector(len(self.base),new_vector)

    def __mul__(self,other):
        'Multiplicate two vectors or a vector with a scalar'
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
        'Multiplicate two vectors or a vector with a scalar'
        if isinstance(other,int) or isinstance(other,float):
            return self.__mul__(other)

    def __div__(self,other):
        'Division between scalar and vector'
        instance = isinstance(other,int) or isinstance(other,float)
        if not instance:
            print 'Error type:\n\tType on division must be an escalar.\n int or float type ??'
        else:
            result = []
            for component in Vector.bases_keys[len(self.base)-2]:
                result.append( float(self.direction[component]) / float(other))
            return Vector(len(self),result)

    def __rdiv__(self,other):
        'Division between scalar and vector'
        return self.__div__(other)

    def __getitem__(self,key):
        'Get the component'
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
        'Set the component'
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
        'Get the vector base'
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

    def hasSameComponentsAs(self,v):
        'Return true if the vectors have the same components'

        paralels = False

        if isinstance(v,Vector) and len(self) == len(v):
            for i in xrange(len(self)):
                paralels = ( self[i] == v[i] )
                if not paralels: break

            return paralels
        else:
            print 'Bad use of same_components:\n\tBoth arguments must be Vector type'
            return paralels

    def _get_angle(self,other):
        'Get the angle formed between two vectors'
        return ( (self * other)/(abs(self)*abs(other)) )

def dot(v1,v2):
    'Dot operation'
    cos_alpha = (v1*v2)/(abs(v1)*abs(v2))
    return abs(v1)*abs(v2)*cos_alpha

def normalize(v):
    'Return a normalize vector of \'v\''
    new_vector = []
    for i in xrange(len(v)):
        new_vector.append( float(v[i]) / float(abs(v)))
    return Vector(len(v),new_vector)

class Line:
    def __init__(self,point=None,vector=None):
        if not point and not vector:
            self.p = point
            self.v = vector
        else:
            if isinstance(point,Point) and isinstance(vector,Vector):
                self.p = point
                self.v = vector
            else:
                print 'Bad initialization:\n\tArguments must be Point and Vector Line(Point p, Vector v)'
