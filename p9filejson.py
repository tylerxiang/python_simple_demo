# -*- coding: utf-8 -*-

import json
import codecs
from p9file import p9file
from grade import Grade

class p9filejson(p9file):
#	def __init__(self,loadName,saveName):
#		self.loadName=loadName
#		self.saveName=saveName

	def load(self):
		f=open(self.loadName,'r')
		data=f.read()
		f.close()
		root=json.loads(data)
		for g in root['grades']:
			g=Grade(g['id'],g['name'],int(g['value']))
			self.grades.append(g)

	def save(self):
		ga=[]
		for g in self.grades:
			gj={}
			gj['id']=g.id
			gj['name']=g.name
			gj['value']=g.value
			ga.append(gj)
		root={}
		root['grades']=ga
		data=json.dumps(root)

		f = codecs.open(self.saveName, mode="w", encoding="utf-8-sig")
		f.write(data)
  		f.close()  


p=p9filejson('datafile/d1.json','datafile/d11.json')
p.mainProc()		