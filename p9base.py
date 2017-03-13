import socket
from grade import Grade

class p9base:
	#virtual method,child class must override
	def __init__(self):
		pass
	def load(self):
		pass
	def save(self):
		pass
	def listBefore(self):
		pass
	def addAfter(self,g):
		pass
	def delAfter(self,g):
		pass
	def editAfter(self,g):
		pass
	def find(self,grade_id):
		pass


	def gradeList(self):
		grades=self.listBefore()
		for g in grades:
			print g

	def gradeAdd(self):
		print '--add--'
		grade_id=raw_input('id:')
		g=self.find(grade_id)
		if g:
			print grade_id,' exists!'
		else:
			g=Grade(grade_id,'',0)
			self.input(g)
			affRow=self.addAfter(g)
			if affRow==1:
				print '--add ok--'
			else:
				print '--add err--'


	def gradeDel(self):
		print '--del--'

		grade_id=raw_input('id:')

		g=self.find(grade_id)
		if g==None:
			print 'not fount ',grade_id
		else:
			affRow=self.delAfter(g)
			print 'affRow:',affRow
			if affRow==1:
				print '--del ok--'
			else:
				print '--del err--'

	def gradeEdit(self):
		print '--edit--'

		grade_id=raw_input('id:')

		g=self.find(grade_id)
		if  g == None :
			print 'not fount ',grade_id
		else:
			self.input(g)
			affRow=self.editAfter(g)
			if affRow==1:
				print '--edit ok--'
			else:
				print '--edit err--'

	def input(self,g):
		grade_name=raw_input('name:')
		grade_value=raw_input('value:')
		g.name=grade_name
		g.value=int(grade_value)

	def mainProc(self):
		self.load()

		isRun=True
		while isRun:
			print '===grade manager==='
			print 'List'
			print 'Add'
			print 'Del'
			print 'Edit'
			print 'Quit'
			choi=raw_input("===Choice:")
			choi=choi.upper()

			if choi=='Q':
				isRun=False
			elif choi=='L':
				self.gradeList()
			elif choi=='A':
				self.gradeAdd()
			elif choi=='D':
				self.gradeDel()
			elif choi=='E':
				self.gradeEdit()
			else:
				print 'choice error'

		self.save()

