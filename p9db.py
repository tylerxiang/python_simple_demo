from p9base import p9base
from grade import Grade
import sqlite3

class p9db(p9base):
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
			g=Grade(line[0],line[1],line[2])
			grades.append(g)
		return grades

	def addAfter(self,g):
		cur=self.db.cursor()
		affectRow=cur.execute("insert into grade(id,name,value) values(?,?,?)",(g.id,g.name,g.value,))
		self.db.commit()
		return 1

	def delAfter(self,g):
		cur=self.db.cursor()
		affectRow=cur.execute("delete from  grade where id=?",(g.id,))
		self.db.commit()
		return 1

	def editAfter(self,g):
		cur=self.db.cursor()
		affectRow=cur.execute("update grade set name=?,value=? where id=?",(g.name,g.value,g.id,))
		self.db.commit()
		return 1

	def find(self,grade_id):		
		g=None

		cur = self.db.cursor()
		cur.execute("select id,name,value from grade where id=?",( grade_id,))
		res=cur.fetchall()
		if len(res)>0:
			g=Grade(res[0][0],res[0][1],res[0][2])
		
		return g

p=p9db('datafile/grade.db')
p.mainProc()