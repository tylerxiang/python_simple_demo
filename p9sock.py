from p9base import p9base
from grade import Grade
import socket

class p9sock(p9base):
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
				g=Grade(sa[0],sa[1],int(sa[2]))
				grades.append(g)
		return grades

	def addAfter(self,g):
		cmd='A,%s,%s,%d' % (g.id,g.name,g.value)
		self.sock.send(cmd)
		data=self.sock.recv(2048)
		if data=='ok':
			return 1
		else:
			return 0

	def delAfter(self,g):
		cmd='D,%s' % (g.id)
		self.sock.send(cmd)
		data=self.sock.recv(2048)
		if data=='ok':
			return 1
		else:
			return 0

	def editAfter(self,g):
		cmd='E,%s,%s,%d' % (g.id,g.name,g.value)
		self.sock.send(cmd)
		data=self.sock.recv(2048)
		if data=='ok':
			return 1
		else:
			return 0

	def find(self,grade_id):		
		g=None

		cmd='F,%s' % (grade_id)
		self.sock.send(cmd)
		data=self.sock.recv(2048)
		sa=data.split(',')
		if sa[0]=='ok':
			g=Grade(sa[1],sa[2],int(sa[3]))
		
		return g

p=p9sock('localhost',10004)
p.mainProc()