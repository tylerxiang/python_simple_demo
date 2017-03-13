class Grade:
	def __init__(self,id,name,value=0):
		self.id=id
		self.name=name
		self.value=value

	def __str__(self):
		return "id:%s name:%s value:%d" % (self.id,self.name,self.value)

	def data(self):
		return "%s,%s,%d\n" % (self.id,self.name,self.value)
