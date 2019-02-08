file1=open("Street_Centrelines.csv")
file2=open("Bus_Stops.csv")
def accessible(file1,file2):
	count1=0
	count2=0
	count3=0
	for line2 in file2:
		line2=line2.split(",")
		for line1 in file1:
			line1=line1.split(",")
			if line2[7].upper()=="Accessible".upper():
				if line1[10].upper()=="ARTERIAL".upper():
					count1+=1
	print(count1)
	for line2 in file2:
		line2=line2.split(",")
		for line1 in file1:
			line1=line1.split(",")
			if line2[7].upper()=="Non-Standard".upper():
				if line1[10].upper()=="LOCAL STREET".upper():
					count2+=1
	print(count2)
	for line2 in file2:
		line2=line2.split(",")
		for line1 in file1:
			line1=line1.split(",")
			if line2[7].upper()=="Inaccessible".upper():
				if line1[10].upper()=="MINOR COLLECTOR".upper():
					count3+=1
	print(count3)


accessible(file1,file2)
