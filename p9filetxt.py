from p9file import p9file
from grade import Grade

class p9filetxt(p9file):
#	def __init__(self,loadName,saveName):
#		self.loadName=loadName
#		self.saveName=saveName

	def load(self):
		f=file(self.loadName)

		for line in f.readlines():
			sa=line.split(',')
			g=Grade(sa[0],sa[1],int(sa[2]))
			self.grades.append(g)

	def save(self):
		f=file(self.saveName,'w')
		for g in self.grades:
			f.writelines(g.data())
		f.close()


p=p9filetxt('datafile/d1.txt','datafile/d11.txt')
p.mainProc()		