from math import sqrt

class cal:
    def __init__(self, para):
        self.para=para
        self.mod=sqrt(para[0]**2+para[1]**2+para[2]**2)

    def go(self, point):
        tmp=abs(para[0]*point[0]+para[1]*point[1]+para[2]*point[2]+para[3])
        return float(tmp)/self.mod

if __name__=='__main__':
    para=[2,2,2,-4]
    pointset=[[1,1,1],[1,1,-1],[1,-1,1],[-1,1,1]]
    c=cal(para)
    print c.mod
    for point in pointset:
        print point
        print c.go(point)
