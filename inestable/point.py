
class Point:
    'Represent a 2D or 3D point'

    MAX_DIM = 3
    zero = [0]*MAX_DIM

    def __init__(self,coord=None,x=None,y=None,z=None):

        short_instance = (isinstance(x,int) and isinstance(y,int)) or (isinstance(x,float) and isinstance(y,float))
        full_instance  = short_instance and (isinstance(z,int) or isinstance(z,float))


        if coord and isinstance(coord,list) and len(coord) <= Point.MAX_DIM:
            self.coord = coord

        elif x and y and not z and short_instance:
            self.coord = [x,y]

        elif x and y and z and full_instance:
            self.coord = [x,y,z]

        elif coord or x or y or z:
            print 'Class point bad initialization:\n\tValue must be a list or int/float types\n\tDid you assign x,y or x,y,z correctly?'
            exit(1)

    def __setitem__(self,key,value):
        if key in [c for c in xrange(Point.MAX_DIM)]:
            self.coord[key] = value
        else:
            print 'Not valid index'
            exit(1)

    def __getitem__(self,key):
        if key in [c for c in xrange(Point.MAX_DIM)]:
            return self.coord[key]
        else:
            print 'Not valid index'
            return None

    def __len__(self):
        return len(self.coord)

    def __neg__(self):
        for coor in xrange(len(self)):
            self[coor] = -self[coor]
            print self[coor]

    def __str__(self):
        if len(self) == 2:
            return '({},{})'.format(self[0],self[1])
        elif len(self) == 3:
            return '({},{},{})'.format(self[0],self[1],self[2])

p = Point([1,2])
print p
p = -p
print p
