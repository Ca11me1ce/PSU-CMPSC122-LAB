class line():
	def __init__(self, first, second):
		self.f=first
		self.s=second
	def midpoint(self):
		mid=[]
		m1=(self.f[0]+self.s[0])/2
		m2=(self.f[1]+self.s[1])/2
		mid.append(m1)
		mid.append(m2)
		return mid

line1=line((2,5),(7,15))
print(line1.midpoint())

