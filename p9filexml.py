from xml.etree import ElementTree
import xml.dom.minidom
from p9file import p9file
from grade import Grade

class p9filexml(p9file):
#	def __init__(self,loadName,saveName):
#		self.loadName=loadName
#		self.saveName=saveName

	def load(self):
		with open(self.loadName,'rt') as f:
			tree=ElementTree.parse(f)

		for node in tree.findall('.//grade'):
			id=node.attrib.get('id')
			name=node.attrib.get('name')
			value=node.attrib.get('value')

			g=Grade(id,name,int(value))
			self.grades.append(g)

	def save(self):
		impl=xml.dom.minidom.getDOMImplementation()
		doc=impl.createDocument(None,'grades',None)
		root=doc.documentElement


		for g in self.grades:
			sub=doc.createElement('grade')
			sub.setAttribute('id',g.id)
			sub.setAttribute('name',g.name)
			sub.setAttribute('value',str(g.value))
			root.appendChild(sub)

		f=open(self.saveName,'w')
		doc.writexml(f, addindent='  ', newl='\n',encoding='utf-8')
  		f.close()  


p=p9filexml('datafile/d1.xml','datafile/d11.xml')
p.mainProc()		