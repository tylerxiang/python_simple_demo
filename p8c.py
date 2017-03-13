import socket
import grade

class p8c:
	def __init__(self,ip,port):
		self.ip=ip
		self.port=port
		self.sock=None

	def load(self):
		self.sock=socket.create_connection((self.ip,self.port)) 
		print 'server connect ok'

	def save(self):
		self.sock.close()
		print 'server disconnect ok'

	def listBefore(self):
		grades=[]
		self.sock.send('L')
		data=self.sock.recv(2048)
		lines=data.split(';')
		for line in lines:
			sa=line.split(',')
			if len(sa)>2:
				g=grade.Grade(sa[0],sa[1],int(sa[2]))
				grades.append(g)
		return grades

	def gradeList(self):
		grades=self.listBefore()
		for g in grades:
			print g

	def addAfter(self,g):
		cmd='A,%s,%s,%d' % (g.id,g.name,g.value)
		self.sock.send(cmd)
		data=self.sock.recv(2048)
		if data=='ok':
			return 1
		else:
			return 0

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
		cmd='D,%s' % (g.id)
		self.sock.send(cmd)
		data=self.sock.recv(2048)
		if data=='ok':
			return 1
		else:
			return 0

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
		cmd='E,%s,%s,%d' % (g.id,g.name,g.value)
		self.sock.send(cmd)
		data=self.sock.recv(2048)
		if data=='ok':
			return 1
		else:
			return 0

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

		cmd='F,%s' % (grade_id)
		self.sock.send(cmd)
		data=self.sock.recv(2048)
		sa=data.split(',')
		if sa[0]=='ok':
			g=grade.Grade(sa[1],sa[2],int(sa[3]))
		
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
	p=p8c('localhost',10004)
	p.mainProc()
