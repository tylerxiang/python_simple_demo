import sys

for i in range(1,10):
	for j in range(1,10):
		z=i*j
		if z>9:
			sys.stdout.write('%dx%d=%d ' % (i,j,z))
		else:
			sys.stdout.write( '%dx%d=0%d ' % (i,j,z))
	sys.stdout.write('\n')		
