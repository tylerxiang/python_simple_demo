import grade

grades=[]

f=file('datafile/d1.txt')

for line in f.readlines():
	sa=line.split(',')
	g=grade.Grade(sa[0],sa[1],int(sa[2]))
	grades.append(g)

for g in grades:
	print g