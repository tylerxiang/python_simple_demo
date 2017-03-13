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
	datas=[]

	f=file("datafile/t1.txt")
	for line in f.readlines():
		num=int(line)
		datas.append(num)

	print datas
	sort(datas)
	print datas