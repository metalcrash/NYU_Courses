class NNC:

	def __init__(self, w, b):
		self.w=w
		self.b=b
	#type(input)=List(List(int)), the last int for each list is the target value
	def train(self, trainset):
		for x in trainset:
			if len(x)-1!=len(self.w):
				print "trainning pattern size error"
				return
			xb=x[len(x)-1]
			self.b+=xb
			for i in xrange(len(self.w)):
				self.w[i]+=x[i]*xb

	def test(self, testset):
		res=[]
		co=0
		for x in testset:
			if len(x)-1!=len(self.w):
				print "testing pattern size error"
				return
			xres=x[len(x)-1]
			y=0
			for i in xrange(len(self.w)):
				y+=self.w[i]*x[i]
			print "y:",y
			xc=1
			if y<self.b:xc=-1
			res.append(xc)
			if xres==xc:
				co+=1
		print "result:",res

if __name__=='__main__':
	w=[0 for x in xrange(15)]
	b=0
	nnc=NNC(w,b)
	ctrain=[-1,1,1,1,-1,-1,1,-1,-1,1,-1,-1,-1,1,1,1]
	dtrain=[1,1,-1,1,-1,1,1,-1,1,1,-1,1,1,1,-1,-1]
	trainset=[ctrain,dtrain]
	print "trainning set:",trainset
	nnc.train(trainset)
	cblur=[0,0,0,0,0,0,0,-1,-1,1,-1,-1,-1,1,1,1]
	dblur=[0,0,0,0,0,0,0,-1,1,1,-1,1,1,1,-1,-1]
	x=[1,-1,1,1,-1,1,-1,1,-1,1,-1,1,1,-1,1,0]
	testset=[x]
	print "testing set:",testset
	nnc.test(testset)
	'''print "testing set:",trainset
	nnc.test(trainset)'''