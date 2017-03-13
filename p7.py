import sqlite3
import grade

class p7:
	def __init__(self,dbName):
		self.dbName=dbName
		self.db=None

	def load(self):
		self.db=sqlite3.connect(self.dbName) 
		print 'database open ok'

	def save(self):
		self.db.close()
		print 'database close ok'

	def listBefore(self):
		cur = self.db.cursor()
		cur.execute("select id,name,value from grade")
		res=cur.fetchall()
		grades=[]
		for line in res:
			g=grade.Grade(line[0],line[1],line[2])
			grades.append(g)
		return grades

	def gradeList(self):
		grades=self.listBefore()
		for g in grades:
			print g

	def addAfter(self,g):
		cur=self.db.cursor()
		affectRow=cur.execute("insert into grade(id,name,value) values(?,?,?)",(g.id,g.name,g.value,))
		self.db.commit()
		return 1

	def gradeAdd(self):
		print '--add--'
		grade_id=raw_input('id:')
		g=self.find(grade_id)
		if g:
			print grade_id,' exists!'
		else:
			g=grade.Grade(grade_id,'',0)
			self.input(g)
			affRow=self.addAfter(g)
			if affRow==1:
				print '--add ok--'
			else:
				print '--add err--'

	def delAfter(self,g):
		cur=self.db.cursor()
		affectRow=cur.execute("delete from  grade where id=?",(g.id,))
		self.db.commit()
		return 1

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

	def editAfter(self,g):
		cur=self.db.cursor()
		affectRow=cur.execute("update grade set name=?,value=? where id=?",(g.name,g.value,g.id,))
		self.db.commit()
		return 1

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

	def find(self,grade_id):
		g=None

		cur = self.db.cursor()
		cur.execute("select id,name,value from grade where id=?",( grade_id,))
		res=cur.fetchall()
		if len(res)>0:
			g=grade.Grade(res[0][0],res[0][1],res[0][2])
		
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
	p=p7('datafile/grade.db')
	p.mainProc()
