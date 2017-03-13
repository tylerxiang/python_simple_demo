from p9base import p9base
from grade import Grade

class p9file(p9base):
	def __init__(self,loadName,saveName):
		self.loadName=loadName
		self.saveName=saveName
		self.grades=[]

	def load(self):
		pass
	def save(self):
		pass

	def listBefore(self):
		return self.grades

	def addAfter(self,g):
		self.grades.append(g)
		return 1

	def delAfter(self,g):
		self.grades.remove(g)
		return 1

	def editAfter(self,g):
		return 1

	def find(self,grade_id):		
		for g in self.grades:
			if g.id == grade_id:
				return g
		return None
