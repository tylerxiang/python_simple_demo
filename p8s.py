import sqlite3
import socket
import grade

class p8s:
	def __init__(self,dbName,port):
		self.dbName=dbName
		self.db=None
		self.port=port
		self.servsock=None
		self.sock=None

	def load(self):
		self.db=sqlite3.connect(self.dbName) 
		print 'database open ok'
		self.servsock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.servsock.bind(('localhost',self.port))
		self.servsock.listen(1)
		print 'socket server listen...'

	def save(self):
		self.db.close()
		print 'database close ok'
		self.servsock.close()
		print 'socket server stop'

	def gradeList(self):
		cur = self.db.cursor()
		cur.execute("select id,name,value from grade")
		res=cur.fetchall()
		grades=''
		for line in res:
			g='%s,%s,%d;' % (line[0],line[1],line[2]) 
			grades+=g
		self.sock.send(grades)

	def gradeAdd(self,id,name,value):
		try:
			cur=self.db.cursor()
			cur.execute("insert into grade(id,name,value) values(?,?,?)",(id,name,value,))
			self.db.commit()
			self.sock.send('ok')
		except:
			self.sock.send('err')

	def gradeDel(self,id):
		try:
			cur=self.db.cursor()
			cur.execute("delete from  grade where id=?",(id,))
			self.db.commit()
			self.sock.send('ok')
		except:
			self.sock.send('err')

	def gradeEdit(self,id,name,value):
		try:
			cur=self.db.cursor()
			cur.execute("update grade set name=?,value=? where id=?",(name,value,id,))
			self.db.commit()
			self.sock.send('ok')
		except:
			self.sock.send('err')

	def find(self,grade_id):
		g=None

		cur = self.db.cursor()
		cur.execute("select id,name,value from grade where id=?",( grade_id,))
		res=cur.fetchall()
		if len(res)>0:
			cmd='ok,%s,%s,%s' % (res[0][0],res[0][1],res[0][2])
			self.sock.send(cmd)
		else:
			self.sock.send('err')

	def mainProc(self):
		self.load()

		try:
			(self.sock,client_addr)=self.servsock.accept()
			isRun=True
			while isRun:
				data=self.sock.recv(128)
				print 'recv:',data
				choi=data[0]

				if choi=='Q':
					isRun=False
				elif choi=='F':
					sa=data.split(',')
					self.find(sa[1])
				elif choi=='L':
					self.gradeList()
				elif choi=='A':
					sa=data.split(',')
					self.gradeAdd(sa[1],sa[2],int(sa[3]))
				elif choi=='D':
					sa=data.split(',')
					self.gradeDel(sa[1])
				elif choi=='E':
					sa=data.split(',')
					self.gradeEdit(sa[1],sa[2],int(sa[3]))
				else:
					print 'choice error'
		except Exception,e:
			print 'error:',e

		self.save()


if __name__ == '__main__':
	p=p8s('datafile/grade.db',10004)
	p.mainProc()
