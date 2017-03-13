import web

urls=(
	'/','gradeList',
	'/add','gradeAdd',
	'/del/(.+)','gradeDel',
	'/edit/(.+)','gradeEdit',
	'/editSave','gradeEditSave',
	)

app=web.application(urls,globals())

render=web.template.render('templates/')
db=web.database(dbn='sqlite',db='datafile/grade.db')

class gradeList:
	def GET(self):		
		grades=db.select('grade')
		return render.list(grades)
class gradeAdd:
	def GET(self):
		return render.add()

	def POST(self):
		i=web.input()
		grade=db.insert('grade',name=i.gradeName,value=i.gradeValue,id=i.gradeId)
		raise web.seeother('/')

class gradeDel:
	def GET(self,id):
		db.delete('grade',where ='id=$id',vars=locals())
		raise web.seeother('/')

class gradeEdit:
	def GET(self,id):
		grade=db.select('grade',where='id=$id',vars=locals())[0]

		sa=[]
		for gg in grade:
			sa.append(gg)
		print('edit~grade',sa)
		return render.edit(grade)

class gradeEditSave:
	def POST(self):
		i=web.input()
		grade=db.update('grade',name=i.gradeName,value=i.gradeValue,where ='id=$gradeId',vars=i)
		raise web.seeother('/')

if __name__ == '__main__':
	app.run()