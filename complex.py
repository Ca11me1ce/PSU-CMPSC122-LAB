class Complex():
	def __init__(self, real, imag):
		self.r=real
		self.i=imag
	def __repr__(self):
		return '({}, {}i)'.format(self.r, self.i)

	def __add__(self, other):
		self.r=self.r*other
		#self.r=self.i[0]+self.i[1]
		return self

a=Complex(1,2)
b=Complex(-2,5)
print(a)
print(b)
a+b

