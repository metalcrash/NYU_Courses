class Perceptron:

    def __init__(self, w, b, a, theta):
        self.w=w
        self.b=b
        self.a=a
        self.theta=theta

    def train(self, trainset):
        step=0
        while True:
            immute=True
            for x in trainset:
                print ("step "+str(step)+":").rjust(8),
                print ("  train case:"+str(x)).rjust(30),
                step+=1
                if len(x)-1!=len(self.w):
                    print "error"
                    return
                xt=x[len(x)-1]
                y=0
                for i in xrange(len(self.w)):
                    y+=self.w[i]*x[i]
                y+=self.b
                yout=self.ftheta(y)
                #print "  yout:",yout
                if yout==xt:
                    print "  correctly classified".rjust(28)
                    continue
                print "  misclassified".rjust(28),
                immute=False
                self.b+=xt*self.a
                for i in xrange(len(self.w)):
                    self.w[i]+=x[i]*xt*self.a
                print ("  weight:"+str(self.w)).rjust(24),
                print ("  bias:"+str(self.b)).rjust(10)
            if immute or step>50:break
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
            yout=self.ftheta(y)
            res.append(yout)
        print "result:",res

    def ftheta(self,yin):
        if yin>self.theta:return 1
        if yin>=-self.theta and yin<=self.theta:return 0
        if yin<-self.theta:return -1

if __name__=='__main__':
    w=[0,0,0]
    b=0
    a=1
    theta=0.2
    p=Perceptron(w,b,a,theta)
    trainset=[[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[-1,1,1,-1]]
    p.train(trainset)
    p.test(trainset)
