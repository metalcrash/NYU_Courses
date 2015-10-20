class Delta:

    def __init__(self, w, b, a, theta):
        self.w=w
        self.b=b
        self.a=a
        self.theta=theta

    def train(self, trainset, descR, MBU):
        print "a=",self.a," descR=",descR," MBU=",MBU
        step=0
        c=0
        q=0
        print ("step").rjust(8),
        print ("train case").rjust(30),
        print ("delta").rjust(8),
        print ("weight").rjust(40),
        print ("bias").rjust(10)
        wbatch=[0 for x in self.w]
        bbatch=0
        while c<len(trainset) and step<=100:
            for x in trainset:
                print str(step).rjust(8),
                print str(x).rjust(30),
                step+=1
                if len(x)-1!=len(self.w):
                    print "error"
                    return
                xt=x[len(x)-1]
                y=0
                for i in xrange(len(self.w)):
                    y+=self.w[i]*x[i]
                y+=self.b
                delta=y-xt
                print ("%0.4f"%delta).rjust(8),
                if abs(delta)<=theta:c+=1
                else:c=0
                bbatch-=delta*2*self.a
                for i in xrange(len(self.w)):
                    wbatch[i]-=x[i]*delta*2*self.a
                q+=1
                if q>=MBU:
                    q=0
                    self.b+=bbatch
                    for i in xrange(len(self.w)):
                        self.w[i]+=wbatch[i]
                    bbatch=0
                    wbatch=[0 for x in self.w]
                wlist=""
                wlist+='['
                for wx in self.w:
                    wlist+=" %0.2f" % wx
                    wlist+=","
                wlist=wlist[:-1]+']'
                print wlist.rjust(40),
                print ("%0.5f"%self.b).rjust(14)
                if c>=4:break
            self.a*=descR
        print "***",step," steps in total"
        print "*** weight:",self.w
        print "*** bias:",self.b

    def test(self, testset):
        res=[]
        for x in testset:
            xres=x[len(x)-1]
            y=0
            for i in xrange(len(self.w)):
                y+=self.w[i]*x[i]
            y+=self.b
            if y>=0:yout=1
            else:yout=-1
            res.append(yout)
        print "result:",res

if __name__=='__main__':
    w=[0,0,0,0]
    b=0
    a=0.12
    theta=0.2
    descR=1
    MBU=0
    p=Delta(w,b,a,theta)
    trainset=[[1,1,1,1,1],[-1,1,-1,-1,1],[1,1,1,-1,-1],[1,-1,-1,1,-1]]
    p.train(trainset,descR,MBU)
    p.test(trainset)
