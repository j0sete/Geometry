
class Ackerman:
    def ack(self,m,n):
        if m == 0:
            return n+1
        elif m > 0 and n == 0:
            return self.ack(m-1,1)
        elif m > 0 and n > 0:
            return self.ack(m-1,self.ack(m,n-1))

ackerman = Ackerman()
print ackerman.ack(6,8)
