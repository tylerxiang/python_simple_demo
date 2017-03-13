import sys

def sort(datas):
	dataLen=len(datas)-2
	i=0
	while i<dataLen:
		j=dataLen
		while j>=i:
			if(datas[j+1]<datas[j]):
				datas[j],datas[j+1]=datas[j+1],datas[j]
			j-=1
		i+=1

if __name__=='__main__':
	datas1=[]

	for i in range(1,len(sys.argv)):
		num=int(sys.argv[i])
		datas1.append(num)
		
	print datas1

	sort(datas1)

	print datas1