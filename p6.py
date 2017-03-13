import grade

class p6:
	def __init__(self,loadName,saveName):
		self.loadName=loadName
		self.saveName=saveName
		self.grades=[]

	def load(self):
		f=file(self.loadName)

		for line in f.readlines():
			sa=line.split(',')
			g=grade.Grade(sa[0],sa[1],int(sa[2]))
			self.grades.append(g)
		print 'load data ok'

	def save(self):
		f=file(self.saveName,'w')
		for g in self.grades:
			f.writelines(g.data())
		f.close()
		print 'save data ok'

	def gradeList(self):
		for g in self.grades:
			print g

	def gradeAdd(self):
		print '--add--'
		grade_id=raw_input('id:')
		g=self.find(grade_id)
		if g:
			print grade_id,' exists!'
		else:
			g=grade.Grade(grade_id,'',0)
			self.input(g)
			self.grades.append(g)
			print '--add ok--'

	def gradeDel(self):
		print '--del--'

		grade_id=raw_input('id:')

		g=self.find(grade_id)
		if g==None:
			print 'not fount ',grade_id
		else:
			self.grades.remove(g)
			print '--del ok--'

	def gradeEdit(self):
		print '--edit--'

		grade_id=raw_input('id:')

		g=self.find(grade_id)
		if  g == None :
			print 'not fount ',grade_id
		else:
			self.input(g)
			print '--edit ok--'

	def find(self,grade_id):
		for g in self.grades:
			if(g.id == grade_id):
				return g

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


if __name__ == '__main__':
	p=p6('datafile/d1.txt','datafile/d11.txt')
	p.mainProc()
