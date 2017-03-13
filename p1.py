import sys

name=sys.argv[1]
sex=sys.argv[2]

if sex == 'w':
	print 'hello Ms. '+name
elif sex == 'm':
	print 'hello Mr. '+name
else:
	print 'error sex'

	