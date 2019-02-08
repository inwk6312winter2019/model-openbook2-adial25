readFile=open("Street_Centrelines.csv")
list=[]
def readData(realFile):
	readFile.readline()
	for line in readFile:
		line=line.split(",")
		list.append((line[2],line[4],line[6],line[7]))
		print(list)
readData(readFile)


readFile=open("Street_Centrelines.csv")
def hist(readFile):
	d = dict()
	readFile.readline()
	for line in readFile:
		line=line.split(",")
		if line[12]  not in d:
			d[line[12]] = 1
		else:
			d[line[12]] += 1
	return d
print(hist(file))


file=open("Street_Centrelines.csv")
def own(file):
	s=set()
	file.readline()
	for line in file:
		line=line.split(",")
		s.add(line[11])
	return s
print(own(file))

file=open("Street_Centrelines.csv")
def street(file):
	z=dict()
	file.readline()
	for line in file:
		line=line.split(",")
		if line[10]  not in z:
			z[line[10]] = 1
		else:
			z[line[10]] += 1
	return z

print(street(file))
