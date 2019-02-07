file = open("Street_Centrelines.csv","r")

'''#task1
def myfile(file):
  streetData= []
  for line in file:
    line=line.split(",")
    streetData.append((line[2],line[4],line[7],line[8]))
  print(streetData)
myfile(file)
